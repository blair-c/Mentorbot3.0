from datetime import datetime

import discord
from discord.ext import commands

from helpers import helpers

class Moderation(commands.Cog):
    """Monitor and moderate server members and activity."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='clear', aliases=['delete', 'purge'], hidden=True)
    @commands.has_permissions(manage_messages=True)
    @helpers.in_academy()
    async def delete_n_messages(self, ctx, n: int = 0):
        """Delete last n messages from channel (Limit 100)."""
        await ctx.message.delete() # Delete message of command
        deleted = await ctx.channel.purge(limit=n)
        if ctx.channel.name == 'boardroom': return  # Don't display deletions from boardroom
        # Bulk message deletion embed
        desc = f'**{len(deleted)} messages deleted in ' \
               f'{ctx.channel.mention} by {ctx.author.mention}**\n'
        for msg in reversed(deleted):
            desc += f'\n**by {msg.author.mention} {str(msg.author)}'
            # Message content may not exist, such as an embed or picture
            if msg.clean_content:
                desc += f':**\n```{msg.clean_content}```'
            else: 
                desc += '**\n```(No message content)```'
        embed = discord.Embed(color=0xb71c1c, description=desc)
        embed.set_author(name='Bulk Message Deletion', icon_url=ctx.author.avatar_url)
        action_log = discord.utils.get(ctx.guild.text_channels, name='action-log')
        await action_log.send(embed=embed)

    @commands.command(name='whois', hidden=True)
    @commands.has_permissions(ban_members=True)
    async def display_member_info(self, ctx, *, member: discord.Member):
        """Display information of given member."""
        embed = discord.Embed(
            color=member.color,
            description=member.mention,
            timestamp=datetime.utcnow())
        embed.set_author(name=member, icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'ID: {member.id}')
        # Dates of server join and Discord registration
        embed.add_field(
            name='Joined',
            value=f'{member.joined_at:%a, %b %d, %Y at %I:%M %p}')
        embed.add_field(
            name='Registered',
            value=f'{member.created_at:%a, %b %d, %Y at %I:%M %p}')
        # Member's status (eg. online, offline, invisible, etc.)
        embed.add_field(name='Status', value=member.status, inline=False)
        # Member's roles, excluding @everyone role
        roles = [role.mention for role in reversed(member.roles)][:-1]
        if roles:
            embed.add_field(name=f'Roles [{len(roles)}]', value=' '.join(roles), inline=False)
        # Get member's key permissions, if any
        perms = member.guild_permissions
        key_perms = {
            'Administrator': perms.administrator,
            'Manage Server': perms.manage_guild,
            'Manage Roles': perms.manage_roles,
            'Manage Channels': perms.manage_channels,
            'Kick Members': perms.kick_members,
            'Ban Members': perms.ban_members,
            'Mention Everyone': perms.mention_everyone,
            'Manage Nicknames': perms.manage_nicknames,
            'Manage Emojis': perms.manage_emojis,
            'Manage Webhooks': perms.manage_webhooks}
        key_perms = ', '.join([k for k, v in key_perms.items() if v])
        if key_perms:
            embed.add_field(name='Key Permissions', value=key_perms, inline=False)
        # Get member's acknowledgements, if any
        if member == ctx.guild.owner:
            acknowledgement = 'Server Owner'
        elif perms.administrator:
            acknowledgement = 'Server Admin'
        elif perms.manage_guild:
            acknowledgement = 'Server Manager'
        elif perms.ban_members:
            acknowledgement = 'Server Moderator'
        else:
            acknowledgement = None
        # Add acknowledgement
        if acknowledgement:
            embed.add_field(name='Acknowledgements', value=acknowledgement, inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Moderation(bot))
