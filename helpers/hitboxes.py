"""Core functions for mentorbot's hitbox commands."""

import discord
from discord.ext import commands
from tabulate import tabulate

from helpers import helpers


async def move_info(ctx, cursor, character, move):
    """Display frame data and hitbox info of move given."""
    # Get character info
    character_info = helpers.character_info(cursor, character=character)
    # Get move ID and display name
    move = cursor.execute(
        '''SELECT id, display_name FROM moves WHERE name1 = :move OR name2 = :move
           OR name3 = :move OR name4 = :move OR name5 = :move OR name6 = :move''', 
           {'move': move}).fetchone()
    # Get move info
    move_info = cursor.execute(
        '''SELECT * FROM hitboxes WHERE char_id = :char_id AND move_id = :move_id''',
        {'char_id': character_info['id'], 'move_id': move['id']}).fetchall()
    # Add move info to embed
    columns = {
        'Cost': 'cost',
        'Startup': 'startup',
        'Active': 'active',
        'Intangible': 'intangible',
        'Invulnerable': 'invulnerable',
        'Armored': 'armored',
        'Endlag': 'endlag',
        'Endlag (Hit)': 'endlag_hit',
        'Endlag (Whiff)': 'endlag_whiff',
        'Landing Lag (Hit)': 'landing_lag_hit',
        'Landing Lag (Whiff)': 'landing_lag_whiff',
        'FAF': 'faf',
        'Cooldown': 'cooldown',
        'Damage': 'damage',
        'Sourspot Damage': 'sourspot_damage',
        'Sweetspot Damage': 'sweetspot_damage',
        'Tipper Damage': 'tipper_damage',
        # For hurtbox commands
        'Height': 'height',
        'Width': 'width',
    }
    move_display = ''
    for row in move_info:
        # Each column may or may not exist
        hit_info = [[display_name, row[column]]
                   for display_name, column in columns.items() if row[column]]
        # Certain tables will not have a hit identifier above them
        if row['hit']:
            move_display += f"\n**{row['hit']}**"
        # Add table of hit info
        move_display += (
            '```ml\n'
            f"{tabulate(hit_info, tablefmt='presto')}\n".replace('\n ', '\n'))  # Strip left-hand whitespace
        if row['notes']:
            move_display += row['notes']
        move_display += '```'
    embed = discord.Embed(color=character_info['color'], description=move_display)
    embed.set_author(name=f"{character} {move['display_name']}",
                     icon_url=character_info['icon'])
    # Some moves may be missing an image
    if move_info[0]['image']:
        embed.set_image(url=move_info[0]['image'])
    # Display different footer for hitbox/hurtbox commands
    if move['id'] == 0:
        more_info_command = '!hurtboxdata'
    else:
        more_info_command = '!framedata'
    embed.set_footer(text=f'See {more_info_command} document for full details.')
    # Send move info embed
    await ctx.send(embed=embed)
