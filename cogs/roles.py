from datetime import datetime
import sqlite3

import discord
from discord.ext import commands

from data import rivals
from helpers import helpers

db = sqlite3.connect('data/academy.db')
db.row_factory = sqlite3.Row
cursor = db.cursor()


class Roles(commands.Cog):
    """Add and remove roles from users, and update mentor database to reflect changes."""

    def __init__(self, bot):
        self.bot = bot

    # Role toggle commands for mentors
    @commands.command(name='dnd', hidden=True)
    @commands.has_any_role('Mentors', 'DO NOT DISTURB')
    @helpers.in_channel('teacher-lounge')
    async def do_not_disturb_toggle(self, ctx):
        """Toggle member's do not disturb role, and update database."""
        mentors_role = discord.utils.get(ctx.guild.roles, name='Mentors')
        dnd_role = discord.utils.get(ctx.guild.roles, name='DO NOT DISTURB')
        member = ctx.guild.get_member(ctx.author.id)
        # Mentors -> DND
        if mentors_role in ctx.author.roles:
            dnd_value = 1
            # Change nickname
            try:
                if ctx.author.display_name[:6] != '[DND] ':
                    await ctx.author.edit(nick=f'[DND] {ctx.author.display_name}')
            except discord.errors.Forbidden:
                pass
            # Update roles and get embed
            embed = await helpers.update_roles(member, mentors_role, dnd_role)
        # DND -> Mentors
        elif dnd_role in ctx.author.roles:
            dnd_value = 0
            # Change nickname
            try:
                if ctx.author.display_name[6:] == ctx.author.name:
                    await ctx.author.edit(nick=None)
                elif ctx.author.display_name[:6] == '[DND] ':
                    await ctx.author.edit(nick=ctx.author.display_name[6:])
            except discord.errors.Forbidden:
                pass
            # Update roles and get embed
            embed = await helpers.update_roles(member, dnd_role, mentors_role)
        # Update database
        with db:
            cursor.execute(
                '''UPDATE mentors SET do_not_disturb = :value WHERE discord_id = :id''',
                {'value': dnd_value, 'id': ctx.author.id})
        await ctx.send(embed=embed)

    @commands.command(name='advisor', hidden=True)
    @commands.has_role('Mentor')
    @helpers.in_channel('teacher-lounge')
    async def advisor_role_toggle(self, ctx):
        """Toggle member's roles from mentor to advisor, and update database."""
        embed = await helpers.update_roles(
            ctx.guild.get_member(ctx.author.id),
            discord.utils.get(ctx.guild.roles, name='Mentor'),  # Remove
            discord.utils.get(ctx.guild.roles, name='Advisor')) # Add
        # Update database
        with db:
            cursor.execute('''UPDATE mentors SET status = 'Advisor'
                           WHERE discord_id = :id''', {'id': ctx.author.id})
        await ctx.send(embed=embed)

    @commands.command(name='mentor', hidden=True)
    @commands.has_role('Advisor')
    @helpers.in_channel('teacher-lounge')
    async def mentor_role_toggle(self, ctx):
        """Toggle member's roles from advisor to mentor, and update database."""
        embed = await helpers.update_roles(
            ctx.guild.get_member(ctx.author.id),
            discord.utils.get(ctx.guild.roles, name='Advisor'), # Remove
            discord.utils.get(ctx.guild.roles, name='Mentor'))  # Add
        # Update database
        with db:
            cursor.execute('''UPDATE mentors SET status = 'Mentor' WHERE discord_id = :id
                           AND secondaries = 0''' , {'id': ctx.author.id})
                           # Secondaries stay as Advisor status
        await ctx.send(embed=embed)

    # Reaction system for main, secondaries, region, undergrad, and enrollment
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        """Give member character, region, undergrad, or student role on reaction."""
        if payload.user_id == self.bot.user.id: return  # Ignore reactions from Mentorbot
        guild = self.bot.get_guild(payload.guild_id)
        channel = discord.utils.get(guild.text_channels, id=payload.channel_id)
        if channel.name != 'set-your-roles': return  # Ensure set-your-roles channel
        message = await channel.fetch_message(payload.message_id)
        member = guild.get_member(payload.user_id)
        emote = payload.emoji.name
        # Main
        if 'main' in message.content:
            # Remove previous main roles
            mains = [discord.utils.get(guild.roles, name=f'{character} (Main)')
                    for character in rivals.characters]
            await member.remove_roles(*[role for role in mains if role in member.roles])
            # Remove secondary role of main being added
            secondary_role = discord.utils.get(guild.roles, name=emote)
            if secondary_role in member.roles:
                await member.remove_roles(secondary_role)
            # Add new main role
            await member.add_roles(discord.utils.get(guild.roles, name=f'{emote} (Main)'))
        # Secondaries
        elif 'secondaries' in message.content:
            main_role = discord.utils.get(guild.roles, name=f'{emote} (Main)')
            if main_role not in member.roles:
                await member.add_roles(discord.utils.get(guild.roles, name=emote))
        # Region
        elif 'region' in message.content:
            # Remove previous region roles
            regions = [discord.utils.get(guild.roles, name=region) for region in
                      rivals.regions]
            await member.remove_roles(*[role for role in regions if role in member.roles])
            # Add new region role
            await member.add_roles(discord.utils.get(guild.roles, name=emote))
        # RAS
        elif 'amateur' in message.content:
            if emote == 'NA':
                await member.add_roles(discord.utils.get(guild.roles, name='Undergrad'))
            elif emote == 'EU':
                await member.add_roles(discord.utils.get(guild.roles, name='amatEUr'))
        # Enrollment
        elif emote == 'roaa':
            student = discord.utils.get(guild.roles, name='Student')
            if student not in member.roles:
                await member.add_roles(student)
                # Display enrollment in action-log
                embed = discord.Embed(
                    color=helpers.display_color(member),
                    description=f'**{member.mention} has enrolled in '
                                'the Rivals of Aether Academy!**',
                    timestamp=datetime.utcnow())
                embed.set_author(name='Member Enrolled', icon_url=member.avatar_url)
                embed.set_footer(text=f'ID: {payload.user_id}')
                action_log = discord.utils.get(guild.text_channels, name='action-log')
                await action_log.send(embed=embed)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        """Remove member's character, region, or undergrad role on reaction remove."""
        guild = self.bot.get_guild(payload.guild_id)
        channel = discord.utils.get(guild.text_channels, id=payload.channel_id)
        if channel.name != 'set-your-roles': return  # Ensure set-your-roles channel
        message = await channel.fetch_message(payload.message_id)
        member = guild.get_member(payload.user_id)
        emote = payload.emoji.name
        # Main
        if 'main' in message.content:
            await member.remove_roles(discord.utils.get(guild.roles, name=f'{emote} (Main)'))
        # Secondaries
        elif 'secondary' in message.content:
            await member.remove_roles(discord.utils.get(guild.roles, name=emote))
        # RAS
        elif 'amateur' in message.content:
            if emote == 'NA':
                await member.remove_roles(discord.utils.get(guild.roles, name='Undergrad'))
            elif emote == 'EU':
                await member.remove_roles(discord.utils.get(guild.roles, name='amatEUr'))

    @commands.command(name='setyourroles')
    @commands.is_owner()
    @helpers.in_channel('set-your-roles')
    async def set_your_roles_channel_setup(self, ctx):
        """Send and react to messages to set up role reaction system channel."""
        # Delete message of command
        await ctx.message.delete()
        # Introduction
        await ctx.send(
            f'Hello! Welcome to the **{ctx.guild.name}!**\n\n'
            '• **Please add reactions below to set your main, secondaries, and region.**\n'
            '• Reacting too quickly may cause the bot to fail in adding/removing roles.\n'
            '• You might need to react and unreact for the role to be added properly.')
        # Main
        await ctx.send(file=discord.File('images/setyourroles/main.png'))
        msg = await ctx.send(
            '• **Click on a character reaction below to set your main.**\n'
            '• Click on the reaction again to remove a main.\n'
            '• You may only have one main character.')
        for character in rivals.characters:
            await msg.add_reaction(
                discord.utils.get(self.bot.emojis, name=character.replace(' ', '')))
        # Secondaries
        await ctx.send(file=discord.File('images/setyourroles/secondaries.png'))
        msg = await ctx.send(
            '• **Click on a character reaction below to add a secondary.**\n'
            '• Click on the reaction again to remove a secondary.\n'
            '• You may have multiple secondaries.')
        for character in rivals.characters:
            await msg.add_reaction(
                discord.utils.get(self.bot.emojis, name=character.replace(' ', '')))
        # Region
        await ctx.send(file=discord.File('images/setyourroles/region.png'))
        msg = await ctx.send(
            '• **Click on a region reaction below to set your region.**\n'
            '<:WestCoast:547189520781803530> → West Coast\n'
            '<:Midwest:547189509272633355> → Midwest\n'
            '<:EastCoast:547189489861132308> → East Coast\n'
            '<:Europe:547189473432305665> → Europe\n'
            '<:Australia:547189427416596502> → Australia\n'
            '<:SouthAmerica:547189406902124595> → South America\n'
            '<:Asia:547189391399976980> → Asia\n'
            '<:Africa:547189379605725225> → Africa')
        for region in rivals.regions:
            await msg.add_reaction(discord.utils.get(self.bot.emojis, name=region))
        # RAS
        await ctx.send(file=discord.File('images/setyourroles/ras.png'))
        msg = await ctx.send(
            '• **If you would like to be notified for our weekly amateur tournaments '
               ' (Rivals Amateur Series), please click on a region reaction below.**\n'
            '• Click on the reaction again to opt out of notifications.\n'
            '<:NorthAmerica:547189311527845907> → North America\n'
            '<:Europe:547189473432305665> → Europe')
        for region in ['NorthAmerica', 'Europe']:
            await msg.add_reaction(discord.utils.get(self.bot.emojis, name=region))
        # Enroll
        await ctx.send(file=discord.File('images/setyourroles/enroll.png'))
        msg = await ctx.send(
            '• **Is this the only channel you can see?**\n'
            '• Click the <:roaa:547193471191089179> reaction below to enroll in the '
            'server and view the rest of the channels!')
        await msg.add_reaction(discord.utils.get(self.bot.emojis, name='roaa'))

    @commands.command(name='addstudent', hidden=True)
    @commands.is_owner()
    async def add_student_roles(self, ctx):
        """One-time setup to add Student role to users without Student or New Member"""
        student = discord.utils.get(ctx.guild.roles, name='Student')
        new_member = discord.utils.get(ctx.guild.roles, name='New Member')
        for member in ctx.guild.members:
            if student not in member.roles and new_member not in member.roles:
                await member.add_roles(student)


def setup(bot):
    bot.add_cog(Roles(bot))
