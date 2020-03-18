from datetime import datetime, timedelta

import discord
from discord.ext import commands

from helpers import helpers


class ActionLog(commands.Cog):
    """Log info on members joining/leaving, deleted/edited messages, etc."""

    def __init__(self, bot):
        self.bot = bot

    # Channel logging
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        """Log that channel has been created."""
        # Check that action-log channel exists and is viewable
        if not (guild := channel.guild): return
        if not (action_log := discord.utils.get(guild.text_channels, name='action-log')): return
        # Log channel creation
        embed = discord.Embed(
            color=0x7aa2cc,
            description=f'**#{channel.name}**',
            timestamp=(datetime.utcnow()))
        embed.set_author(name='Channel Created', icon_url=guild.icon_url)
        embed.set_footer(text=f'ID: {channel.id}')
        # Send in action-log
        await action_log.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        """Log that channel has been deleted."""
        # Check that action-log channel exists and is viewable
        if not (guild := channel.guild): return
        if not (action_log := discord.utils.get(guild.text_channels, name='action-log')): return
        # Log channel deletion
        embed = discord.Embed(
            color=0xcc7ab6,
            description=f'**#{channel.name}**',
            timestamp=(datetime.utcnow()))
        embed.set_author(name='Channel Deleted', icon_url=guild.icon_url)
        embed.set_footer(text=f'ID: {channel.id}')
        # Send in action-log
        await action_log.send(embed=embed)

    # Role logging
    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        """Log that role has been created."""
        # Check that action-log channel exists and is viewable
        if not (guild := role.guild): return
        if not (action_log := discord.utils.get(guild.text_channels, name='action-log')): return
        # Log role creation
        embed = discord.Embed(
            color=0x7aa2cc,
            description=f'**{role.name}** {role.mention}',
            timestamp=(datetime.utcnow()))
        embed.set_author(name='Role Created', icon_url=guild.icon_url)
        embed.set_footer(text=f'ID: {role.id}')
        # Send in action-log
        await action_log.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        """Log that role has been updated."""
        # Check that action-log channel exists and is viewable
        if not (guild := after.guild): return
        if not (action_log := discord.utils.get(guild.text_channels, name='action-log')): return
        # Log what attributes have been updated
        updated = '```\n'
        if before.name != after.name:  # Name
            updated += f'- Name: {before.name} → {after.name}\n'
        if before.permissions != after.permissions:  # Permissions
            updated += '- Permissions changed\n'
        if before.color != after.color:  # Color
            updated += f'- Color: {after.color}\n'
        if before.hoist != after.hoist:  # Sidebar position
            updated += ('- Now separate on sidebar\n' if after.hoist else 
                        '- No longer separate on sidebar\n')
        if before.mentionable != after.mentionable:  # Pingable
            updated += ('- Now @mentionable\n' if after.mentionable else 
                        '- No longer @mentionable\n')
        # Don't log if none of these have been updated
        if updated == '```\n': return
        # Format
        updated += '```'
        embed = discord.Embed(
            color=0xa07acc,
            description=f'**{after.name}** {after.mention}\n{updated}',
            timestamp=(datetime.utcnow()))
        embed.set_author(name='Role Updated', icon_url=guild.icon_url)
        embed.set_footer(text=f'ID: {after.id}')
        # Send in action-log
        await action_log.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        """Log that role has been deleted."""
        # Check that action-log channel exists and is viewable
        if not (guild := role.guild): return
        if not (action_log := discord.utils.get(guild.text_channels, name='action-log')): return
        # Log role deletion
        embed = discord.Embed(
            color=0xcc7ab6,
            description=f'**{role.name}**',
            timestamp=(datetime.utcnow()))
        embed.set_author(name='Role Deleted', icon_url=guild.icon_url)
        embed.set_footer(text=f'ID: {role.id}')
        # Send in action-log
        await action_log.send(embed=embed)

    # Member logging
    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        """Log that member has been banned."""
        # Check that action-log channel exists and is viewable
        if not guild: return
        if not (action_log := discord.utils.get(guild.text_channels, name='action-log')): return
        # Log member ban
        embed = discord.Embed(
            color=0xa83e1d,
            description=f'**{str(user)}**',
            timestamp=(datetime.utcnow()))
        embed.set_author(name='Member Banned', icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text=f'ID: {user.id}')
        # Send in action-log
        await action_log.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Log that member has joined."""
        # Check that action-log channel exists and is viewable
        if not (guild := member.guild): return
        if not (action_log := discord.utils.get(guild.text_channels, name='action-log')): return
        # Log member join
        embed = discord.Embed(
            color=0x66bb6a,
            description=f'{member.mention}\n**{str(member)}**',
            timestamp=(joined_at := datetime.utcnow()))
        embed.set_author(name='Member Joined', icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'ID: {member.id}')
        # Note if user joined within 1 day of account creation
        if (joined_at - member.created_at) < timedelta(days=1):
            embed.add_field(name='New Account', value=f'Account created within past day')
        # Send in action-log
        await action_log.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        """Display in action-log channel that member has left."""
        # Check that action-log channel exists and is viewable
        if not (guild := member.guild): return
        if not (action_log := discord.utils.get(guild.text_channels, name='action-log')): return
        # Log member removal
        embed = discord.Embed(
            color=0xff7043,
            description=f'{member.mention}\n**{str(member)}**',
            timestamp=datetime.utcnow())
        embed.set_author(name='Member Left', icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'ID: {member.id}')
        # Ping principals if member was a mentor (only in Academy/test server)
        ping = ''
        if guild.id in [252352512332529664, 475599187812155392]:
            roles = guild.roles
            mentor = discord.utils.get(roles, name='Mentor')
            dnd = discord.utils.get(roles, name='DO NOT DISTURB')
            if mentor in member.roles or dnd in member.roles:
                principal = discord.utils.get(roles, name='Principal')
                vice_principal = discord.utils.get(roles, name='Vice Principal')
                ping = f'{principal.mention} {vice_principal.mention}'
        # Send in action-log
        await action_log.send(content=ping, embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        """Display in action-log channel that member's nickname has changed."""
        # Check that action-log channel exists and is viewable
        if not (guild := before.guild): return
        if not (action_log := discord.utils.get(guild.text_channels, name='action-log')): return
        # Ensure that nickname has changed
        if before.nick == after.nick: return
        # Log nickname change
        embed = discord.Embed(
            color=0xfff86e,
            description=f'{before.mention} **nickname changed**',
            timestamp=datetime.utcnow())
        embed.set_author(name=f'{str(before)}', icon_url=before.avatar_url)
        embed.set_footer(text=f'ID: {before.id}')
        # Before nickname change
        embed.add_field(name='Before:', value=f'```{helpers.get_nickname(before)}```',
                        inline=False)
        # After nickname change
        embed.add_field(name='After:', value=f'```{helpers.get_nickname(after)}```',
                        inline=False)
        # Send in action-log
        await action_log.send(embed=embed)

    # Message logging
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        """Display info of deleted message in action-log channel."""
        # Check that action-log channel exists and is viewable
        if not (guild := message.guild): return
        if not (action_log := discord.utils.get(guild.text_channels, name='action-log')): return
        # Log message deletion
        desc = f'**Message by {message.author.mention} deleted in {message.channel.mention}**'
        # Message content may not exist, such as an embed or picture
        if message.clean_content:
            desc += f'```\n{message.clean_content}```'
        embed = discord.Embed(
            color=0xef5350,
            description=desc,
            timestamp=datetime.utcnow())
        embed.set_author(name=f'{str(message.author)}', icon_url=message.author.avatar_url)
        embed.set_footer(text=f'User ID: {message.author.id}')
        # Send in action-log
        await action_log.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        """Display info of edited message in action-log channel."""
        # Check that action-log channel exists and is viewable
        if not (guild := before.guild): return
        if not (action_log := discord.utils.get(guild.text_channels, name='action-log')): return
        # Ensure that message content has changed (ignore embeds)
        if before.content == after.content: return
        # Log message edit
        embed = discord.Embed(
            color=0x5c6bc0,
            description=(f'**Message by {before.author.mention} edited in {before.channel.mention}** '
                         f'[Jump to message]({before.jump_url})'),
            timestamp=datetime.utcnow())
        embed.set_author(name=f'{str(before.author)}', icon_url=before.author.avatar_url)
        embed.set_footer(text=f'User ID: {before.author.id}')
        # Before edit
        if before.content:
            embed.add_field(name='Before:', value=f'```{before.clean_content}```', inline=False)
        # After edit
        if after.content:
            embed.add_field(name='After:', value=f'```{after.clean_content}```', inline=False)
        # Send in action-log
        await action_log.send(embed=embed)


def setup(bot):
    bot.add_cog(ActionLog(bot))
