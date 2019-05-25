from datetime import datetime, timedelta

import discord
from discord.ext import commands

from helpers import helpers

class Moderation(commands.Cog):
    """Monitor and moderate server members and activity."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='clear', aliases=['purge', 'delet'], hidden=True)
    @commands.has_permissions(manage_messages=True)
    async def delete_n_messages(self, ctx, n: int = 0):
        """Delete last n+1 messages from channel (Limit 100)."""
        await ctx.channel.purge(limit=n+1)

    @commands.command(name='whois', hidden=True)
    @commands.has_permissions(ban_members=True)
    async def display_member_info(self, ctx, *, member: discord.Member):
        """Display information of given member."""
        embed = discord.Embed(
            color=helpers.display_color(member.color),
            description=member.mention,
            timestamp=datetime.now())
        embed.set_author(name=member, icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'ID: {member.id}')
        # Dates of server join and Discord registration
        embed.add_field(
            name='Joined',
            value=f'{member.joined_at:%a, %b %-d, %Y at %-I:%M %p}')
        embed.add_field(
            name='Registered',
            value=f'{member.created_at:%a, %b %-d, %Y at %-I:%M %p}')
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

    @commands.command(name='purgewelcome', hidden=True)
    @commands.has_permissions(kick_members=True)
    async def purge_welcome_channel(self, ctx):
        """Kick inactive members that have not enrolled."""
        embed = discord.Embed()
        embed.set_author(name='Working...')
        await ctx.send(embed=embed)
        # Kick members that have not enrolled and that joined before the past week
        new_members = discord.utils.get(ctx.guild.roles, name='New Member').members
        new_members = [member for member in new_members
                      if member.joined_at < datetime.utcnow() - timedelta(weeks=1)]
        for member in new_members:
            await member.kick(reason='Inactivity')
        # Send message that users were kicked
        embed.set_author(name=f'{len(new_members)} members kicked.')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Moderation(bot))
