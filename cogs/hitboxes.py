from typing import Literal

import discord
from discord import app_commands
from discord.ext import commands

from helpers import hitboxes

import sqlite3
db = sqlite3.connect('data/academy.db')
db.row_factory = sqlite3.Row
cursor = db.cursor()


class Hitboxes(commands.Cog):
    """"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    moves = [
        'Jab', 'Dash Attack',
        'Up Tilt', 'Down Tilt', 'Forward Tilt',
        'Up Strong', 'Down Strong', 'Forward Strong', 
        'Neutral Air', 'Up Air', 'Down Air', 'Forward Air', 'Back Air',
        'Neutral Special', 'Up Special', 'Down Special', 'Side Special'
    ]
    moves = dict.fromkeys(moves)  # Dict of keys moves and values None

    # Zetterburn
    zet_moves = moves.copy()
    zet_moves['Neutral Special'] = 'Shine'
    zet_moves['Side Special'] = 'Fireball'
    zet_moves = [f'{move} ({name})' if name else move  # Formatted list
                 for move, name in zet_moves.items()]
    zet_moves = Literal[tuple(zet_moves)]  # To pass into command as choices

    @app_commands.command(name='zetterburn', extras=moves)
    async def zetterburn(self, interaction: discord.Interaction, attack: zet_moves):
        """Zetterburn frame data and hitbox info"""
        for orig in interaction.command.extras:  # Original moves w/o char-specific names
            if orig in attack:
                await hitboxes.move_info(interaction, cursor, 'Zetterburn', orig)
                break

    # Forsburn
    fors_moves = moves.copy()
    fors_moves['Up Strong'] = 'Cape'
    fors_moves['Forward Strong'] = 'Cape'
    fors_moves['Neutral Special'] = 'Smoke'
    fors_moves['Up Special'] = 'Teleport'
    fors_moves['Down Special'] = 'Clone Pop/Combust'
    fors_moves['Side Special'] = 'Clone'
    fors_moves = [f'{move} ({name})' if name else move  # Formatted list
                  for move, name in fors_moves.items()]
    fors_moves = Literal[tuple(fors_moves)]  # To pass into command as choices

    @app_commands.command(name='forsburn', extras=moves)
    async def forsburn(self, interaction: discord.Interaction, attack: fors_moves):
        """Forsburn frame data and hitbox info"""
        for orig in interaction.command.extras:  # Original moves w/o char-specific names
            if orig in attack:
                await hitboxes.move_info(interaction, cursor, 'Forsburn', orig)
                break

    # Clairen
    clairen_moves = moves.copy()
    clairen_moves['Neutral Special'] = 'Grab/Throw'
    clairen_moves['Down Special'] = 'Counter/Plasma Field'
    clairen_moves = [f'{move} ({name})' if name else move  # Formatted list
                     for move, name in clairen_moves.items()]
    clairen_moves = Literal[tuple(clairen_moves)]  # To pass into command as choices

    @app_commands.command(name='clairen', extras=moves)
    async def clairen(self, interaction: discord.Interaction, attack: clairen_moves):
        """Clairen frame data and hitbox info"""
        for orig in interaction.command.extras:  # Original moves w/o char-specific names
            if orig in attack:
                await hitboxes.move_info(interaction, cursor, 'Clairen', orig)
                break

    # Orcane
    orca_moves = moves.copy()
    orca_moves['Forward Air'] = 'Bubblebutt'
    orca_moves['Neutral Special'] = 'Droplet'
    orca_moves['Down Special'] = 'Bubbles'
    orca_moves['Up Special'] = 'Teleport'
    orca_moves = [f'{move} ({name})' if name else move  # Formatted list
                  for move, name in orca_moves.items()]
    orca_moves = Literal[tuple(orca_moves)]  # To pass into command as choices

    @app_commands.command(name='orcane', extras=moves)
    async def orcane(self, interaction: discord.Interaction, attack: orca_moves):
        """Orcane frame data and hitbox info"""
        for orig in interaction.command.extras:  # Original moves w/o char-specific names
            if orig in attack:
                await hitboxes.move_info(interaction, cursor, 'Orcane', orig)
                break

    # Etalus
    eta_moves = moves.copy()
    eta_moves['Neutral Special'] = 'Hammer'
    eta_moves['Down Special'] = 'Freeze'
    eta_moves['Side Special'] = 'Icicles'
    eta_moves = [f'{move} ({name})' if name else move  # Formatted list
                 for move, name in eta_moves.items()]
    eta_moves = Literal[tuple(eta_moves)]  # To pass into command as choices

    @app_commands.command(name='etalus', extras=moves)
    async def etalus(self, interaction: discord.Interaction, attack: eta_moves):
        """Etalus frame data and hitbox info"""
        for orig in interaction.command.extras:  # Original moves w/o char-specific names
            if orig in attack:
                await hitboxes.move_info(interaction, cursor, 'Etalus', orig)
                break

    # Ranno
    ranno_moves = moves.copy()
    ranno_moves['Neutral Special'] = 'Needles'
    ranno_moves['Down Special'] = 'Bubble'
    ranno_moves['Side Special'] = 'Tongue'
    ranno_moves = [f'{move} ({name})' if name else move  # Formatted list
                   for move, name in ranno_moves.items()]
    ranno_moves = Literal[tuple(ranno_moves)]  # To pass into command as choices

    @app_commands.command(name='ranno', extras=moves)
    async def ranno(self, interaction: discord.Interaction, attack: ranno_moves):
        """Ranno frame data and hitbox info"""
        for orig in interaction.command.extras:  # Original moves w/o char-specific names
            if orig in attack:
                await hitboxes.move_info(interaction, cursor, 'Ranno', orig)
                break

    # Kragg
    moves['Taunt'] = None  # Add Taunt
    kragg_moves = moves.copy()
    kragg_moves['Neutral Special'] = 'Rock/Shine'
    kragg_moves['Up Special'] = 'Pillar'
    kragg_moves = [f'{move} ({name})' if name else move  # Formatted list
                   for move, name in kragg_moves.items()]
    kragg_moves = Literal[tuple(kragg_moves)]  # To pass into command as choices

    @app_commands.command(name='kragg', extras=moves)
    async def kragg(self, interaction: discord.Interaction, attack: kragg_moves):
        """Kragg frame data and hitbox info"""
        for orig in interaction.command.extras:  # Original moves w/o char-specific names
            if orig in attack:
                await hitboxes.move_info(interaction, cursor, 'Kragg', orig)
                break

    del moves['Taunt']  # Remove Taunt

    # Maypul
    maypul_moves = moves.copy()
    maypul_moves['Down Air'] = 'Root'
    maypul_moves['Neutral Special'] = 'Seed'
    maypul_moves['Down Special'] = 'Lily'
    maypul_moves['Up Special'] = 'Tether/Uppercut'
    maypul_moves = [f'{move} ({name})' if name else move  # Formatted list
                    for move, name in maypul_moves.items()]
    maypul_moves = Literal[tuple(maypul_moves)]  # To pass into command as choices

    @app_commands.command(name='maypul', extras=moves)
    async def maypul(self, interaction: discord.Interaction, attack: maypul_moves):
        """Maypul frame data and hitbox info"""
        for orig in interaction.command.extras:  # Original moves w/o char-specific names
            if orig in attack:
                await hitboxes.move_info(interaction, cursor, 'Maypul', orig)
                break

    # Sylvanos
    sylv_moves = moves.copy()
    sylv_moves['Jab'] = 'Petal Wave'
    sylv_moves['Neutral Special'] = 'Seed/Flower'
    sylv_moves['Up Special'] = 'Burrow/Bite'
    sylv_moves['Down Special'] = 'Howl'
    sylv_moves['Side Special'] = 'Beast Dash'
    sylv_moves = [f'{move} ({name})' if name else move  # Formatted list
                  for move, name in sylv_moves.items()]
    sylv_moves = Literal[tuple(sylv_moves)]  # To pass into command as choices

    @app_commands.command(name='sylvanos', extras=moves)
    async def sylvanos(self, interaction: discord.Interaction, attack: sylv_moves):
        """Sylvanos frame data and hitbox info"""
        for orig in interaction.command.extras:  # Original moves w/o char-specific names
            if orig in attack:
                await hitboxes.move_info(interaction, cursor, 'Sylvanos', orig)
                break

    # Wrastor
    wrastor_moves = moves.copy()
    wrastor_moves['Up Strong'] = 'Clap'
    wrastor_moves['Forward Strong'] = 'Clap'
    wrastor_moves['Neutral Special'] = 'Tornado'
    wrastor_moves['Side Special'] = 'Slipstream'
    wrastor_moves = [f'{move} ({name})' if name else move  # Formatted list
                     for move, name in wrastor_moves.items()]
    wrastor_moves = Literal[tuple(wrastor_moves)]  # To pass into command as choices

    @app_commands.command(name='wrastor', extras=moves)
    async def wrastor(self, interaction: discord.Interaction, attack: wrastor_moves):
        """Wrastor frame data and hitbox info"""
        for orig in interaction.command.extras:  # Original moves w/o char-specific names
            if orig in attack:
                await hitboxes.move_info(interaction, cursor, 'Wrastor', orig)
                break

    # Absa
    absa_moves = moves.copy()
    absa_moves['Neutral Special'] = 'Cloud/Thunderline'
    absa_moves['Down Special'] = 'Cloud Bomb'
    absa_moves['Side Special'] = 'Cloud'
    absa_moves = [f'{move} ({name})' if name else move  # Formatted list
                  for move, name in absa_moves.items()]
    absa_moves = Literal[tuple(absa_moves)]  # To pass into command as choices

    @app_commands.command(name='absa', extras=moves)
    async def absa(self, interaction: discord.Interaction, attack: absa_moves):
        """Absa frame data and hitbox info"""
        for orig in interaction.command.extras:  # Original moves w/o char-specific names
            if orig in attack:
                await hitboxes.move_info(interaction, cursor, 'Absa', orig)
                break

    # Elliana
    elli_moves = moves.copy()
    elli_moves['Up Strong'] = 'Steam'
    elli_moves['Down Strong'] = 'Steam'
    elli_moves['Forward Strong'] = 'Steam'
    elli_moves['Neutral Special'] = 'Fist'
    elli_moves['Up Special'] = 'Eject Mech'
    elli_moves['Down Special'] = 'Mine'
    elli_moves['Side Special'] = 'Missile'
    elli_moves = [f'{move} ({name})' if name else move  # Formatted list
                  for move, name in elli_moves.items()]
    elli_moves = Literal[tuple(elli_moves)]  # To pass into command as choices

    @app_commands.command(name='elliana', extras=moves)
    async def elliana(self, interaction: discord.Interaction, attack: elli_moves):
        """Elliana frame data and hitbox info"""
        for orig in interaction.command.extras:  # Original moves w/o char-specific names
            if orig in attack:
                await hitboxes.move_info(interaction, cursor, 'Elliana', orig)
                break

    # Ori
    ori_moves = moves.copy()
    ori_moves['Neutral Special'] = 'Sein Charge/Taps'
    ori_moves['Up Special'] = 'Parasol'
    ori_moves['Down Special'] = 'Bash'
    ori_moves['Side Special'] = 'Light Orb'
    ori_moves = [f'{move} ({name})' if name else move  # Formatted list
                 for move, name in ori_moves.items()]
    ori_moves = Literal[tuple(ori_moves)]  # To pass into command as choices

    @app_commands.command(name='ori', extras=moves)
    async def ori(self, interaction: discord.Interaction, attack: ori_moves):
        """Ori frame data and hitbox info"""
        for orig in interaction.command.extras:  # Original moves w/o char-specific names
            if orig in attack:
                await hitboxes.move_info(interaction, cursor, 'Ori', orig)
                break

    # TODO: touch up this system & implementation
    # Shovel Knight
    moves['Taunt'] = None  # Add Taunt
    sk_moves = moves.copy()
    sk_moves['Up Strong'] = 'Rock'
    sk_moves['Neutral Special'] = 'Coin Capture'
    sk_moves['Horn'] = None
    sk_moves['Mobile Gear'] = None
    sk_moves['Ghost Gloves'] = None
    sk_moves['Up Special'] = 'Anchor'
    sk_moves['Down Special'] = 'Fish'
    sk_moves['Side Special'] = 'Infinidagger'
    sk_moves['Taunt'] = 'Shop'
    sk_moves = [f'{move} ({name})' if name else move  # Formatted list
                for move, name in sk_moves.items()]
    sk_moves = Literal[tuple(sk_moves)]  # To pass into command as choices

    @app_commands.command(name='sk', extras=moves)
    async def shovel_knight(self, interaction: discord.Interaction, attack: sk_moves):
        """Shovel Knight frame data and hitbox info"""
        for orig in interaction.command.extras:  # Original moves w/o char-specific names
            if orig in attack:
                await hitboxes.move_info(interaction, cursor, 'Shovel Knight', orig)
                break
        else:  # Neutralb runes
            await hitboxes.move_info(interaction, cursor, 'Shovel Knight', attack)


async def setup(bot: commands.Bot):
    await bot.add_cog(Hitboxes(bot))
