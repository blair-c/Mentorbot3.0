from datetime import datetime

import discord
from discord.ext import commands

from helpers import helpers


class ActionLog(commands.Cog):
    """Log info on members joining/leaving, deleted/edited messages, etc."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Log that member has joined."""
        # Check that action-log channel exists and is viewable
        if not (guild:= member.guild): return
        if not (action_log := discord.utils.get(guild.text_channels, name='action-log')): return
        # Log member join
        embed = discord.Embed(
            color=0x66bb6a,
            description=f'{member.mention} **{str(member)}**',
            timestamp=datetime.utcnow())
        embed.set_author(name='Member Joined', icon_url=member.avatar_url)
        embed.set_footer(text=f'ID: {member.id}')
        # Send in action-log
        await action_log.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        """Display in action-log channel that member has left."""
        # Check that action-log channel exists and is viewable
        if not (guild:= member.guild): return
        if not (action_log := discord.utils.get(guild.text_channels, name='action-log')): return
        # Log member removal
        embed = discord.Embed(
            color=0xff7043,
            description=f'{member.mention} **{str(member)}**',
            timestamp=datetime.utcnow())
        embed.set_author(name='Member Left', icon_url=member.avatar_url)
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
    async def on_message_delete(self, message):
        """Display info of deleted message in action-log channel."""
        # Check that action-log channel exists and is viewable
        if not (guild:= message.guild): return
        if not (action_log := discord.utils.get(guild.text_channels, name='action-log')): return
        # Ignore messages from boardroom
        if message.channel.name == 'boardroom': return
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
        if not (guild:= before.guild): return
        if not (action_log := discord.utils.get(guild.text_channels, name='action-log')): return
        # Ignore messages from boardroom, and ensure that message content has changed
        if before.channel.name == 'boardroom' or before.content == after.content: return
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

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        """Display in action-log channel that member's nickname has changed."""
        # Check that action-log channel exists and is viewable
        if not (guild:= before.guild): return
        if not (action_log := discord.utils.get(guild.text_channels, name='action-log')): return
        # Ensure that nickname has changed
        if before.nick == after.nick: return
        # Log nickname change
        embed = discord.Embed(
            color=0x7e57c2,
            description=f'{before.mention} **nickname changed**',
            timestamp=datetime.utcnow())
        embed.set_author(name=f'{str(before.author)}', icon_url=before.avatar_url)
        embed.set_footer(text=f'ID: {before.id}')
        # Before nickname change
        embed.add_field(name='Before:', value=f'```{helpers.get_nickname(before)}```',
                        inline=False)
        # After nickname change
        embed.add_field(name='After:', value=f'```{helpers.get_nickname(after)}```',
                        inline=False)
        # Send in action-log
        await action_log.send(embed=embed)


def setup(bot):
    bot.add_cog(ActionLog(bot))
