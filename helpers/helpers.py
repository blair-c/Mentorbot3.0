"""Helper functions for mentorbot events and commands."""

from datetime import datetime

import discord
from discord.ext import commands


# Helper Functions
def character_info(cursor, character=None, region=None):
    """Return id, name, color, and icon url of given character/region."""
    if character:  # If character was given
        return cursor.execute(
            '''SELECT * FROM characters WHERE name = :character''',
            {'character': character.title()}).fetchone()
    elif region:  # If region was given
        return cursor.execute(
            '''SELECT * FROM characters WHERE name = :region''',
            {'region': region.upper()}).fetchone()


def character_role(guild, cursor, character, main=False):
    """Return role of character with name given."""
    character = cursor.execute(
        '''SELECT name FROM characters WHERE name = :character''',
        {'character': character.title()}).fetchone()
    if main:
        return discord.utils.get(guild.roles, f"{character['name']} (Main)")
    else:
        return discord.utils.get(guild.roles, character['name'])


def get_nickname(member):
    """Return member's nickname, and if it is their default name."""
    if member.nick:
        return member.nick
    else:
        return f'{member.display_name} (No nickname)'


def sidebar_color(color):
    """Return default sidebar color for default role and member colors."""
    if color == discord.Color.default():
        return 0x202225
    else:
        return color


async def update_roles(member, remove, add):
    """Remove/add given roles, and return embed of info."""
    await member.remove_roles(remove)
    await member.add_roles(add)
    embed = discord.Embed(
        color=sidebar_color(add.color),
        description=f'**Updated roles for {member.mention}:**\n'
                    '```diff\n'
                    f'- {remove.name}\n'
                    f'+ {add.name}```',
        timestamp=datetime.utcnow())
    embed.set_author(name='Roles updated', icon_url=member.avatar_url)
    embed.set_footer(text=f'ID: {member.id}')
    return embed


# Helper Command Checks
def in_academy():
    """Check that command is in Adademy or Mentorbot Test Server."""
    async def predicate(ctx):
        return ctx.message.guild.id in [252352512332529664, 475599187812155392]
    return commands.check(predicate)


def in_channel(name):
    """Check that command is in channel of given name."""
    async def predicate(ctx):
        return ctx.channel == discord.utils.get(ctx.guild.text_channels, name=name)
    return commands.check(predicate)
