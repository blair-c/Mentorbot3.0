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
        """Log that member has joined, and give them New Member role."""
        await member.add_roles(discord.utils.get(member.guild.roles, name='New Member'))
        embed = discord.Embed(
            description=f'**{member.mention} has joined the Rivals of Aether Academy!**',
            timestamp=datetime.now())
        embed.set_author(name='Member Joined', icon_url=member.avatar_url)
        embed.set_footer(text=f'ID: {member.id}')
        action_log = discord.utils.get(member.guild.text_channels, name='action-log')
        await action_log.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        """Display in action-log channel that member has left."""
        embed = discord.Embed(
            color=helpers.display_color(member.color),
            description=f'**{member.mention} has left the Rivals of Aether Academy :(**',
            timestamp=datetime.now())
        embed.set_author(name='Member Left', icon_url=member.avatar_url)
        embed.set_footer(text=f'ID: {member.id}')
        # Send in action-log
        action_log = discord.utils.get(member.guild.text_channels, name='action-log')
        await action_log.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        """Display info of deleted message in action-log channel."""
        if message.channel.name == 'boardroom': return # Ignore messages from boardroom
        embed = discord.Embed(
            color=helpers.display_color(message.author.color),
            description=f'**Message by {message.author.mention} deleted in '
                        f'{message.channel.mention}**',
            timestamp=datetime.now())
        embed.set_author(name='Message Deleted', icon_url=message.author.avatar_url)
        embed.set_footer(text=f'User ID: {message.author.id}')
        # Message content may not exist, such as an embed or picture
        if message.content:
            embed.add_field(name='Message:', value=f'```{message.content}```')
        action_log = discord.utils.get(message.guild.text_channels, name='action-log')
        await action_log.send(embed=embed)

    @commands.Cog.listener()
    async def on_raw_bulk_message_delete(self, payload):
        """"""
        guild = self.bot.get_guild(payload.guild_id)
        channel = discord.utils.get(guild.text_channels, id=payload.channel_id)
        if channel.name == 'boardroom': return # Ignore deletions from boardroom
        embed = discord.Embed(
            color=0xffffff,
            description=f'**{len(payload.message_ids)} messages deleted in '
                        f'{channel.mention}**')
        embed.set_author(name='Bulk Message Deletion')
        action_log = discord.utils.get(guild.text_channels, name='action-log')
        await action_log.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        """Display info of edited message in action-log channel."""
        # Ignore messages from boardroom, and ensure that message content has changed
        if before.channel.name == 'boardroom' or before.content == after.content: return
        embed = discord.Embed(
            color=helpers.display_color(before.author.color),
            description=f'**Message by {before.author.mention} edited in '
                        f'{before.channel.mention}**',
            timestamp=datetime.now())
        embed.set_author(name='Message Edited', icon_url=before.author.avatar_url)
        embed.set_footer(text=f'User ID: {before.author.id}')
        # Before edit
        if before.content:
            embed.add_field(name='Before:', value=f'```{before.content}```', inline=False)
        # After edit
        if after.content:
            embed.add_field(name='After:', value=f'```{after.content}```', inline=False)
        action_log = discord.utils.get(before.guild.text_channels, name='action-log')
        try:
            await action_log.send(embed=embed)
        except discord.errors.HTTPException:
            pass # Suppress invalid form body error

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        """Display in action-log channel that member's nickname has changed."""
        if before.nick == after.nick: return # Ensure that nickname has changed
        embed = discord.Embed(
            color=helpers.display_color(before.color),
            description=f'**{before.mention} nickname changed**',
            timestamp=datetime.now())
        embed.set_author(name=f'Nickname Changed', icon_url=before.avatar_url)
        embed.set_footer(text=f'ID: {before.id}')
        # Before nickname change
        embed.add_field(name='Before:', value=f'```{helpers.get_nickname(before)}```',
                        inline=False)
        # After nickname change
        embed.add_field(name='After:', value=f'```{helpers.get_nickname(after)}```',
                        inline=False)
        action_log = discord.utils.get(before.guild.text_channels, name='action-log')
        await action_log.send(embed=embed)


def setup(bot):
    bot.add_cog(ActionLog(bot))
