from typing import Literal

import discord
from discord import app_commands
from discord.ext import commands

from data import rivals


class Mentors(commands.Cog):
    """List mentors and manage those lists."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    ACADEMY_GUILD_ID = 252352512332529664
    TEST_GUILD_ID = 475599187812155392

    @app_commands.command(name='mentors')
    @app_commands.guilds(ACADEMY_GUILD_ID, TEST_GUILD_ID)
    async def mentors_list(self, interaction: discord.Interaction, 
                           character: Literal[tuple(rivals.characters)]):
        """List active mentors for the given character"""
        # Get mentors
        roles = interaction.guild.roles
        character_role = discord.utils.get(roles, name=f'{character} (Main)')
        active_mentors = discord.utils.get(roles, name='Mentors').members
        active_mentors = [m for m in active_mentors if character_role in m.roles]
        # Split into sections
        sections = {'Mentor': [], 'Trial Mentor': [], 'Advisor': []}
        for status in sections:
            mentors = [m for m in active_mentors 
                      if discord.utils.get(roles, name=status) in m.roles]
            # Display regions next to each mentor
            region_roles = [discord.utils.get(roles, name=r) for r in rivals.regions]
            for i, mentor in enumerate(mentors):
                regions = [rivals.regions[r.name]['abbreviation'] for r in region_roles
                          if r in mentor.roles]
                mentors[i] = f'{mentor.mention} **@{str(mentor)}** ({"/".join(regions)})'
            sections[status] = mentors
        # Embed
        info = rivals.characters[character]
        embed = discord.Embed(
            color=info['color'],
            title=f"Here's a list of our {character} mentors and advisors:")
        embed.set_author(name='Great selection!', icon_url=info['icon'])
        for status, mentors in sections.items():
            if mentors:
                embed.add_field(name=f'{status}s', value='\n'.join(mentors), inline=False)
        await interaction.response.send_message(embed=embed)

    # Mentor role management
    def in_teacher_lounge():
        """Check that command is in '#teacher-lounge' channel"""
        def predicate(interaction: discord.Interaction) -> bool:
            return interaction.channel.name == 'teacher-lounge'
        return app_commands.check(predicate)

    async def update_roles(self, member, remove=None, add=None):
        """Remove/add given roles, and return embed of info."""
        desc = f'**Updated roles for {member.mention} {str(member)}:**\n```diff\n'
        if remove:
            await member.remove_roles(remove)
            desc += f'- {remove.name}\n'
            clr = remove.color
        if add:
            await member.add_roles(add)
            desc += f'+ {add.name}'
            clr = add.color
        desc += '```'
        embed = discord.Embed(
            color=clr if clr != discord.Color.default() else 0x202225, 
            description=desc, 
            timestamp=discord.utils.utcnow())
        embed.set_author(name='Roles updated', icon_url=member.avatar.url)
        embed.set_footer(text=f'ID: {member.id}')
        return embed

    @app_commands.command(name='dnd')
    @app_commands.guilds(ACADEMY_GUILD_ID, TEST_GUILD_ID)
    @app_commands.checks.has_any_role('Mentors', 'DO NOT DISTURB')
    @in_teacher_lounge()
    async def do_not_disturb_toggle(self, interaction: discord.Interaction):
        """Toggle 'Do Not Disturb' status removing you from mentor commands"""
        roles = interaction.guild.roles
        mentors_role = discord.utils.get(roles, name='Mentors')
        dnd_role = discord.utils.get(roles, name='DO NOT DISTURB')
        member = interaction.user
        if mentors_role in member.roles:  # Mentors -> DND
            embed = await self.update_roles(member, remove=mentors_role, add=dnd_role)
            try:  # Change nickname
                if member.display_name[:6] != '[DND] ':
                    await member.edit(nick=f'[DND] {member.display_name}')
            except discord.errors.Forbidden:  # Missing permissions
                pass
        elif dnd_role in member.roles:  # DND -> Mentors
            embed = await self.update_roles(member, remove=dnd_role, add=mentors_role)
            try:  # Change nickname
                if member.display_name[6:] == member.name:
                    await member.edit(nick=None)
                elif member.display_name[:6] == '[DND] ':
                    await member.edit(nick=member.display_name[6:])
            except discord.errors.Forbidden:  # Missing permissions
                pass
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name='advisor')
    @app_commands.guilds(ACADEMY_GUILD_ID, TEST_GUILD_ID)
    @app_commands.checks.has_any_role('Mentor', 'Advisor')
    @in_teacher_lounge()
    async def mentor_advisor_toggle(self, interaction: discord.Interaction):
        "Toggle yourself between Mentor/Advisor"
        roles = interaction.guild.roles
        mentor_role = discord.utils.get(roles, name='Mentor')
        advisor_role = discord.utils.get(roles, name='Advisor')
        member = interaction.user
        if mentor_role in member.roles:  # Mentor -> Advisor
            embed = await self.update_roles(member, remove=mentor_role, add=advisor_role)
        elif advisor_role in member.roles:  # Advisor -> Mentor
            embed = await self.update_roles(member, remove=advisor_role, add=mentor_role)
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Mentors(bot))
