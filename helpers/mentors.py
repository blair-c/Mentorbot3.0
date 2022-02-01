"""Core functions for Mentorbot's character and region-based mentor commands."""

import discord
from discord.ext import commands

from data import rivals


async def mentor_info(ctx, character=None, region=None, console=None):
    """Display an embed listing the mentors of given character/region."""
    roles = ctx.guild.roles
    kb_sw_xb = {
        discord.utils.get(roles, name='Keyboard'): rivals.consoles['Keyboard']['emote'] + ' ',
        discord.utils.get(roles, name='Switch Mentor'): rivals.consoles['Nintendo Switch']['emote'],
        discord.utils.get(roles, name='Xbox Mentor'): rivals.consoles['Xbox One']['emote']
    }
    if character:
        char_role = discord.utils.get(roles, name=character)
        main_role = discord.utils.get(roles, name=f'{character} (Main)')
        region_roles = [discord.utils.get(roles, name=r) for r in rivals.regions]
        # Active mentors
        active_mentors = [m for m in discord.utils.get(roles, name='Mentors').members
                         if char_role in m.roles or main_role in m.roles]
        sections = {'Mentor': [], 'Trial Mentor': [], 'Advisor': []}
        for status in sections:
            mentor_list = [m for m in active_mentors if discord.utils.get(roles, name=status) in m.roles]
            formatted = []
            for mentor in mentor_list:  # Format
                # Display regions next to each mentor
                regions = [rivals.regions[r.name]['abbreviation'] for r in region_roles if r in mentor.roles]
                display = f'{mentor.mention} **{str(mentor)}** ({"/".join(regions)}) '
                # Display if mentor is available for Switch/Xbox Mentoring, and/or plays on keyboard
                for role, emote in kb_sw_xb.items():
                    if role in mentor.roles:
                        display += emote
                formatted.append(display)
            sections[status] = formatted
        # DND mentors
        dnd_list = [m for m in discord.utils.get(roles, name='DO NOT DISTURB').members
                   if char_role in m.roles or main_role in m.roles]
        formatted = []
        for mentor in dnd_list:  # Format
            # Display regions next to each mentor
            regions = [rivals.regions[r.name]['abbreviation'] for r in region_roles if r in mentor.roles]
            display = f'{mentor.mention} **{str(mentor)}** ({"/".join(regions)}) '
            # Display if mentor is available for Switch/Xbox Mentoring, and/or plays on keyboard
            for role, emote in kb_sw_xb.items():
                if role in mentor.roles:
                    display += emote
            formatted.append(display)
        dnd_list = formatted
        # For display 
        info = rivals.characters[character]
        selection = character

    elif region:
        region_role = discord.utils.get(roles, name=region)
        char_roles = [discord.utils.get(roles, name=c) for c in rivals.characters]
        main_roles = [discord.utils.get(roles, name=f'{c} (Main)') for c in rivals.characters]
        # Active mentors
        active_mentors = [m for m in discord.utils.get(roles, name='Mentors').members
                         if region_role in m.roles]
        sections = {'Mentor': [], 'Trial Mentor': [], 'Advisor': []}
        for status in sections:
            mentor_list = [m for m in active_mentors if discord.utils.get(roles, name=status) in m.roles]
            formatted = []
            for mentor in mentor_list:  # Format
                # Display characters next to each mentor
                mains = [rivals.characters[m.name.replace(' (Main)', '')]['emote'] 
                        for m in main_roles if m in mentor.roles]
                chars = [rivals.characters[c.name]['emote'] for c in char_roles if c in mentor.roles]
                display = f'{mentor.mention} **{str(mentor)}** {"".join(mains + chars)} '
                # Display if mentor is available for Switch/Xbox Mentoring, and/or plays on keyboard
                for role, emote in kb_sw_xb.items():
                    if role in mentor.roles:
                        display += emote
                formatted.append(display)
            sections[status] = formatted
        # DND mentors
        dnd_list = [m for m in discord.utils.get(roles, name='DO NOT DISTURB').members
                   if region_role in m.roles]
        formatted = []
        for mentor in dnd_list:  # Format
            # Display characters next to each mentor
            mains = [rivals.characters[m.name.replace(' (Main)', '')]['emote'] 
                    for m in main_roles if m in mentor.roles]
            chars = [rivals.characters[c.name]['emote'] for c in char_roles if c in mentor.roles]
            display = f'{mentor.mention} **{str(mentor)}** {"".join(mains + chars)} '
            # Display if mentor is available for Switch/Xbox Mentoring, and/or plays on keyboard
            for role, emote in kb_sw_xb.items():
                if role in mentor.roles:
                    display += emote
            formatted.append(display)
        dnd_list = formatted
        # For display
        info = rivals.regions[region]
        selection = info['abbreviation']

    elif console:
        for role, emote in kb_sw_xb.items():
            if console in role.name:
                console_role = role
                console_emote = emote
        region_roles = [discord.utils.get(roles, name=r) for r in rivals.regions]
        char_roles = [discord.utils.get(roles, name=c) for c in rivals.characters]
        main_roles = [discord.utils.get(roles, name=f'{c} (Main)') for c in rivals.characters]
        # Active mentors
        active_mentors = [m for m in discord.utils.get(roles, name='Mentors').members
                         if console_role in m.roles]
        sections = {'Mentor': [], 'Trial Mentor': [], 'Advisor': []}
        for status in sections:
            mentor_list = [m for m in active_mentors if discord.utils.get(roles, name=status) in m.roles]
            formatted = []
            for mentor in mentor_list:  # Format
                # Display region and characters next to each mentor
                regions = [rivals.regions[r.name]['abbreviation'] for r in region_roles if r in mentor.roles]
                mains = [rivals.characters[m.name.replace(' (Main)', '')]['emote'] 
                        for m in main_roles if m in mentor.roles]
                chars = [rivals.characters[c.name]['emote'] for c in char_roles if c in mentor.roles]
                display = f'{mentor.mention} **{str(mentor)}** ({"/".join(regions)}) {"".join(mains + chars)}'
                formatted.append(display)
            sections[status] = formatted
        # DND mentors
        dnd_list = [m for m in discord.utils.get(roles, name='DO NOT DISTURB').members
                   if console_role in m.roles]
        formatted = []
        for mentor in dnd_list:  # Format
            # Display region and characters next to each mentor
            regions = [rivals.regions[r.name]['abbreviation'] for r in region_roles if r in mentor.roles]
            mains = [rivals.characters[m.name.replace(' (Main)', '')]['emote'] 
                    for m in main_roles if m in mentor.roles]
            chars = [rivals.characters[c.name]['emote'] for c in char_roles if c in mentor.roles]
            display = f'{mentor.mention} **{str(mentor)}** ({"/".join(regions)}) {"".join(mains + chars)}'
            formatted.append(display)
        dnd_list = formatted
        # For display
        info = rivals.consoles[console]
        selection = console

    # Display
    embed = discord.Embed(
        color=info['color'],
        title=f"Here's a list of our {selection} mentors and advisors:")
    embed.set_author(name='Great selection!', icon_url=info['icon'])
    for section, mentor_list in sections.items():
        if mentor_list:
            embed.add_field(name=f'{section}s', value='\n'.join(mentor_list), inline=False)
    if dnd_list:
        embed.add_field(name='Do Not Disturb', value='\n'.join(dnd_list), inline=False)
    # Send mentor info
    await ctx.send(embed=embed)
    