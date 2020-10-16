"""Core functions for Mentorbot's character and region-based mentor commands."""

import discord
from discord.ext import commands

from bot import db
from data import rivals


async def mentor_info(ctx, character=None, region=None):
    """Display an embed listing the mentors of given character/region."""
    # Get character/region name, color, and icon url
    if region == 'EU':
        info = {'color': 3294334, 'icon': 'https://imgur.com/WPMrAhN.png'}
        selection = 'EU'
    else:
        info = rivals.characters[character]
        selection = character
    # Create embed
    embed = discord.Embed(
        color=info['color'],
        title=f"Here's a list of our {selection} mentors and advisors:")
    embed.set_author(name='Great selection!', icon_url=info['icon'])
    bot = ctx.bot
    # Active
    sections = {'Mentor': 'Mentors', 'Trial': 'Trial Mentors', 'Advisor': 'Advisors'}
    for data_name, display in sections.items():
        mentors = mentors_of_status(bot, data_name, character=character, region=region)
        if mentors:
            embed.add_field(name=display, value=mentors, inline=False)
    # DND
    dnd = dnd_mentors(bot, character=character, region=region)
    if dnd:
        embed.add_field(name='Do Not Disturb', value=dnd, inline=False)
    # Send mentor info
    await ctx.send(embed=embed)


def mentors_of_status(bot, status, character=None, region=None):
    """Return mentors of given status and character/region for embed."""
    mentors = []
    if character:
        # sql = """SELECT discord_id, name, region, switch, xbox FROM mentors WHERE status
                #  = %(status)s AND characters LIKE %(character)s ESCAPE '' AND NOT do_not_disturb"""
        # data = {'status': status, 'character': f'%{character}%'}
        # db.execute(sql, data)
        db.execute("""SELECT discord_id, name, region, switch, xbox FROM mentors WHERE status =
                   %(status)s AND characters LIKE %(character)s ESCAPE '' AND NOT do_not_disturb""",
                   {'status': status, 'character': f'%{character}%'})
        for row in db.fetchall():
            try:
                mentor = bot.get_user(row['discord_id'])
                mentors.append(f"{mentor.mention} **{str(mentor)}** ({row['region']})")
            except AttributeError:  # catch if user ID isn't found, eg. left the server
                mentors.append(f"{row['name']} ({row['region']})")
            # :switch:, :xbox: emotes next to names
            if row['switch']:
                mentors[-1] += '<:switch:759539694937309186>'
            elif row['xbox']:
                mentors[-1] += '<:xbox:759539695553085460>'
    elif region:
        db.execute('''SELECT discord_id, name, characters, switch, xbox FROM mentors WHERE 
                   status = %(status)s AND region = %(region)s AND do_not_disturb = 0''',
                   {'status': status, 'region': region})
        for row in db.fetchall():
            try:
                mentor = bot.get_user(row['discord_id'])
                mentors.append(f"{mentor.mention} **{str(mentor)}** ({row['characters']})")
            except AttributeError:  # catch if user ID isn't found, eg. left the server
                mentors.append(f"{row['name']} ({row['characters']})")
            # :switch:, :xbox: emotes next to names
            if row['switch']:
                mentors[-1] += '<:switch:759539694937309186>'
            elif row['xbox']:
                mentors[-1] += '<:xbox:759539695553085460>'
    return '\n'.join(mentors)


def dnd_mentors(bot, character=None, region=None):
    """Return DND mentors of given character/region for embed."""
    mentors = []
    if character:
        db.execute('''SELECT discord_id, name, region, switch, xbox FROM mentors WHERE
                   characters LIKE %(character)s AND do_not_disturb = 1''',
                   {'character': f'%{character}%'})
        for row in db.fetchall():
            try:
                mentor = bot.get_user(row['discord_id'])
                mentors.append(f"{mentor.mention} **{str(mentor)}** ({row['region']})")
            except AttributeError:  # catch if user ID isn't found, eg. left the server
                mentors.append(f"{row['name']} ({row['region']})")
            # :switch:, :xbox: emotes next to names
            if row['switch']:
                mentors[-1] += '<:switch:759539694937309186>'
            elif row['xbox']:
                mentors[-1] += '<:xbox:759539695553085460>'
    elif region:
        db.execute('''SELECT discord_id, name, characters, switch, xbox FROM mentors WHERE 
                   region = %(region)s AND do_not_disturb = 1''', {'region': region})
        for row in db.fetchall():
            try:
                mentor = bot.get_user(row['discord_id'])
                mentors.append(f"{mentor.mention} **{str(mentor)}** ({row['characters']})")
            except AttributeError:  # catch if user ID isn't found, eg. left the server
                mentors.append(f"{row['name']} ({row['characters']})")
            # :switch:, :xbox: emotes next to names
            if row['switch']:
                mentors[-1] += '<:switch:759539694937309186>'
            elif row['xbox']:
                mentors[-1] += '<:xbox:759539695553085460>'
    return '\n'.join(mentors)

