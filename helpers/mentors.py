"""Core functions for Mentorbot's character and region-based mentor commands."""

import discord
from discord.ext import commands

from helpers import helpers


async def mentor_info(ctx, cursor, c=None, r=None):
    """Display an embed listing the mentors of given character/region."""
    # Get character/region name, color, and icon url
    info = helpers.character_info(cursor, character=c, region=r)
    # Create embed
    embed = discord.Embed(
        color=info['color'],
        title=f"Here's a list of our {info['name']} mentors and advisors:")
    embed.set_author(name='Great selection!', icon_url=info['icon'])
    # Mentors
    mentors = mentors_of_status(ctx, cursor, 'Mentor', c=c, r=r)
    if mentors:
        embed.add_field(name='Mentors', value=mentors, inline=False)
    # Trial Mentors
    trial_mentors = mentors_of_status(ctx, cursor, 'Trial', c=c, r=r)
    if trial_mentors:
        embed.add_field(name='Trial Mentors', value=trial_mentors, inline=False)
    # Advisors
    advisors = mentors_of_status(ctx, cursor, 'Advisor', c=c, r=r)
    if advisors:
        embed.add_field(name='Advisors', value=advisors, inline=False)
    # Send mentor info
    await ctx.send(embed=embed)


def mentors_of_status(ctx, cursor, status, c=None, r=None):
    """Return mentors of given status and character/region for embed."""
    character_region = helpers.character_info(cursor, character=c, region=r)['name']
    if c:  # If character was given
        # cursor.execute('''SELECT discord_id, region FROM mentors WHERE status = :status
        #                AND characters LIKE :character = 1 AND do_not_disturb = 0''',
        #                {'status': status, 'character': f'%{character_region}%'})
        #mentors = [f"{ctx.bot.get_user(row['discord_id']).mention} ({row['region']})"
        #          for row in cursor.fetchall()]
        cursor.execute('''SELECT name, region FROM mentors WHERE status = :status
                       AND characters LIKE :character = 1 AND do_not_disturb = 0''',
                       {'status': status, 'character': f'%{character_region}%'})
        mentors = [f"{row['name']} ({row['region']})" for row in cursor.fetchall()]
    elif r:  # If region was given
        # cursor.execute('''SELECT discord_id, characters FROM mentors WHERE status =
        #                :status AND region = :region AND do_not_disturb = 0''',
        #                {'status': status, 'region': character_region})
        #mentors = [f"{ctx.bot.get_user(row['discord_id']).mention} ({row['characters']})"
        #          for row in cursor.fetchall()]
        cursor.execute('''SELECT name, characters FROM mentors WHERE status =
                       :status AND region = :region AND do_not_disturb = 0''',
                       {'status': status, 'region': character_region})
        mentors = [f"{row['name']} ({row['characters']})" for row in cursor.fetchall()]
    return '\n'.join(mentors)
