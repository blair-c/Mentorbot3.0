import json, requests
from typing import Literal

import discord
from discord import app_commands
from discord.ui import Button, View
from discord.ext import commands
from tabulate import tabulate

from data import rivals


class MoveSelect(Button):
    """"""
    def __init__(self, name: str, embed: discord.Embed, user: discord.User):
        self.embed = embed
        self.user = user
        super().__init__(label=name, style=discord.ButtonStyle.gray)

    async def callback(self, interaction):
        if self.user == interaction.user:
            await interaction.response.edit_message(embed=self.embed)
        else:
            return


def move_display(character: str, move: str, user: discord.User):
    """Return an embed and interactive view for a character's move."""
    char = character.lower().replace(' ', '-')
    resp = requests.get(url=f'https://rivals.academy/library/{char}/data.json')
    data = resp.json()
    info = rivals.characters[character]
    move = move.split(' (')[0].replace('/B', '')
    
    variants = []
    for variant in data[move[0].lower() + move[1:].replace(' ', '')]:
        image = variant.get('image')
        if image:
            image = image['highRes']
        else:
            continue # Skip variant if no image

        link = f"https://rivals.academy/library/{char}#{move.lower().replace(' ', '-')}"
        button_name = ''
        name = variant.get('name')
        if name:
            name = name.replace(':', '')
            link += f"-{name.lower().replace(' ', '-')}"
            name = name.replace('Empowered ', '').replace(' Explosion', '')
            if name == 'Bomb':
                name = 'Bomb Pull'
            button_name = name
        if len(variants) == 0:
            if char == 'orcane':
                button_name = 'No Puddle'
            elif char == 'forsburn':
                button_name = 'Non-Empowered'
            elif char == 'mollo' and 'Strong' in move:
                button_name = 'No Bomb'
            elif char == 'etalus':
                button_name = 'No Armor'
            elif char == 'ranno':
                button_name = 'Lunge/Divekick'
            elif char == 'hodan':
                button_name = 'Uncharged'
            elif char == 'kragg':
                button_name = 'Rock Pull/Pickup'
            elif char == 'absa':
                if move == 'Neutral Special':
                    button_name = 'Cloud Hop/Pop'
                else:
                    button_name = 'No Cloud'
            elif char == 'ori':
                button_name = 'No Sein'
            elif char == 'shovel-knight':
                if move == 'Side Special':
                    button_name = 'Charge'
                elif move == 'Down Special':
                    button_name = 'Anchor'
        
        embed = discord.Embed(color=info['color'], description=f'**Full info:** {link}')
        embed.set_image(url=image)
        title = f'{character} {move}'
        if name:
            title += f': {name}'
        embed.set_author(name=title, icon_url=info['icon'], url=link)
        embed.set_footer(text=f"Up-to-date as of Patch {data['patch']}")

        variants.append({'name': button_name, 'embed': embed})

    view = View()
    if len(variants) > 1:
        for embed in variants:
            view.add_item(MoveSelect(name=embed['name'], embed=embed['embed'], user=user))

    return variants[0]['embed'], view

class Hitboxes(commands.Cog):
    """Send displays of frame data, character, and hitbox info."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Zetterburn
    moves = Literal[
        'Jab', 'Dash Attack',
        'Down Tilt', 'Up Tilt', 'Forward Tilt',
        'Neutral Air', 'Down Air', 'Up Air', 'Forward Air', 'Back Air',
        'Down Strong', 'Up Strong', 'Forward Strong', 
        'Up Special/B', 'Neutral Special/B (Shine)',
        'Down Special/B', 'Side Special/B (Fireball)'
    ]

    @app_commands.command(name='zetterburn')
    async def zetterburn(self, interaction: discord.Interaction, attack: moves):
        """Zetterburn frame data and hitbox info"""
        embed, view = move_display('Zetterburn', attack, interaction.user)
        await interaction.response.send_message(embed=embed, view=view)

    # Forsburn
    moves = Literal[
        'Jab', 'Dash Attack',
        'Down Tilt', 'Up Tilt', 'Forward Tilt',
        'Neutral Air', 'Down Air', 'Up Air', 'Forward Air', 'Back Air',
        'Down Strong', 'Up Strong (Cape)', 'Forward Strong (Cape)', 
        'Up Special/B', #'Neutral Special/B (Smoke)',
        'Down Special/B (Combust)', 'Side Special/B (Clone)'
    ]

    @app_commands.command(name='forsburn')
    async def forsburn(self, interaction: discord.Interaction, attack: moves):
        """Forsburn frame data and hitbox info"""
        embed, view = move_display('Forsburn', attack, interaction.user)
        await interaction.response.send_message(embed=embed, view=view)

    # Clairen
    moves = Literal[
        'Jab', 'Dash Attack',
        'Down Tilt', 'Up Tilt', 'Forward Tilt',
        'Neutral Air', 'Down Air', 'Up Air', 'Forward Air', 'Back Air',
        'Down Strong', 'Up Strong', 'Forward Strong', 
        'Up Special/B', 'Neutral Special/B (Grab)',
        'Down Special/B (Counter/Plasma Field)', 'Side Special/B'
    ]

    @app_commands.command(name='clairen')
    async def clairen(self, interaction: discord.Interaction, attack: moves):
        """Clairen frame data and hitbox info"""
        embed, view = move_display('Clairen', attack, interaction.user)
        await interaction.response.send_message(embed=embed, view=view)

    # Mollo
    moves = Literal[
        'Jab (Spray Paint)', 'Dash Attack',
        'Down Tilt', 'Up Tilt', 'Forward Tilt',
        'Neutral Air', 'Down Air', 'Up Air', 'Forward Air', 'Back Air',
        'Down Strong', 'Up Strong', 'Forward Strong', 
        'Up Special/B', 'Neutral Special/B (Bomb Pull/Cherry/Firecracker/Flashbang/Finisher)',
        'Down Special/B (Bat)', 'Side Special/B (Flare Gun)'
    ]

    @app_commands.command(name='mollo')
    async def mollo(self, interaction: discord.Interaction, attack: moves):
        """Mollo frame data and hitbox info"""
        embed, view = move_display('Mollo', attack, interaction.user)
        await interaction.response.send_message(embed=embed, view=view)

    # Orcane
    moves = Literal[
        'Jab', 'Dash Attack',
        'Down Tilt', 'Up Tilt', 'Forward Tilt',
        'Neutral Air (Bounce)', 'Down Air', 'Up Air (Bellyflop)', 'Forward Air (Bubblebutt)', 'Back Air',
        'Down Strong', 'Up Strong', 'Forward Strong', 
        'Up Special/B (Teleport)', 'Neutral Special/B (Droplet)',
        'Down Special/B (Bubbles/Puddle)', 'Side Special/B'
    ]

    @app_commands.command(name='orcane')
    async def orcane(self, interaction: discord.Interaction, attack: moves):
        """Orcane frame data and hitbox info"""
        embed, view = move_display('Orcane', attack, interaction.user)
        await interaction.response.send_message(embed=embed, view=view)

    # Etalus
    moves = Literal[
        'Jab', 'Dash Attack',
        'Down Tilt', 'Up Tilt', 'Forward Tilt',
        'Neutral Air', 'Down Air', 'Up Air', 'Forward Air', 'Back Air',
        'Down Strong', 'Up Strong', 'Forward Strong', 
        'Up Special/B', 'Neutral Special/B (Hammer)',
        'Down Special/B (Freeze)', 'Side Special/B (Icicles)'
    ]

    @app_commands.command(name='etalus')
    async def etalus(self, interaction: discord.Interaction, attack: moves):
        """Etalus frame data and hitbox info"""
        embed, view = move_display('Etalus', attack, interaction.user)
        await interaction.response.send_message(embed=embed, view=view)

    # Ranno
    moves = Literal[
        'Jab', 'Dash Attack',
        'Down Tilt', 'Up Tilt', 'Forward Tilt',
        'Neutral Air', 'Down Air', 'Up Air', 'Forward Air', 'Back Air',
        'Down Strong', 'Up Strong', 'Forward Strong', 
        'Up Special/B (Divekick/Needle Storm)', 'Neutral Special/B (Darts/Needles)',
        'Down Special/B (Bubble)', 'Side Special/B (Tongue)'
    ]

    @app_commands.command(name='ranno')
    async def ranno(self, interaction: discord.Interaction, attack: moves):
        """Ranno frame data and hitbox info"""
        embed, view = move_display('Ranno', attack, interaction.user)
        await interaction.response.send_message(embed=embed, view=view)

    # Hodan
    moves = Literal[
        'Jab', 'Dash Attack',
        'Down Tilt', 'Up Tilt', 'Forward Tilt',
        'Neutral Air', 'Down Air', 'Up Air', 'Forward Air', 'Back Air',
        'Down Strong (Parry)', 'Up Strong', 'Forward Strong', 
        'Up Special/B', 'Neutral Special/B (Spin)',
        'Down Special/B (Mud Slam/Bury)', 'Side Special/B (Sweat Spirit)'
    ]

    @app_commands.command(name='hodan')
    async def hodan(self, interaction: discord.Interaction, attack: moves):
        """Hodan frame data and hitbox info"""
        embed, view = move_display('Hodan', attack, interaction.user)
        await interaction.response.send_message(embed=embed, view=view)

    # Kragg
    moves = Literal[
        'Jab', 'Dash Attack',
        'Down Tilt', 'Up Tilt', 'Forward Tilt',
        'Neutral Air', 'Down Air', 'Up Air', 'Forward Air', 'Back Air',
        'Down Strong', 'Up Strong', 'Forward Strong', 
        'Up Special/B (Pillar)', 'Neutral Special/B (Rock Pull/Shine/Throw/Shards)',
        'Down Special/B (Spikes/Stomp)', 'Side Special/B',
        'Taunt'
    ]

    @app_commands.command(name='kragg')
    async def kragg(self, interaction: discord.Interaction, attack: moves):
        """Kragg frame data and hitbox info"""
        embed, view = move_display('Kragg', attack, interaction.user)
        await interaction.response.send_message(embed=embed, view=view)

    # Maypul
    moves = Literal[
        'Jab', 'Dash Attack',
        'Down Tilt', 'Up Tilt', 'Forward Tilt',
        'Neutral Air', 'Down Air (Root)', 'Up Air', 'Forward Air', 'Back Air',
        'Down Strong', 'Up Strong', 'Forward Strong', 
        'Up Special/B (Tether/Uppercut)', 'Neutral Special/B (Seed)',
        'Down Special/B (Lily)', 'Side Special/B',
    ]

    @app_commands.command(name='maypul')
    async def maypul(self, interaction: discord.Interaction, attack: moves):
        """Maypul frame data and hitbox info"""
        embed, view = move_display('Maypul', attack, interaction.user)
        await interaction.response.send_message(embed=embed, view=view)

    # Sylvanos
    moves = Literal[
        'Jab (Petal Wave)', 'Dash Attack',
        'Down Tilt', 'Up Tilt', 'Forward Tilt (Seed/Flower)',
        'Neutral Air', 'Down Air', 'Up Air', 'Forward Air', 'Back Air (Pin)',
        'Down Strong', 'Up Strong', 'Forward Strong', 
        'Up Special/B (Burrow)', 'Neutral Special/B (Seed/Flower)',
        'Down Special/B (Howl)', 'Side Special/B (Beast Dash)',
    ]

    @app_commands.command(name='sylvanos')
    async def sylvanos(self, interaction: discord.Interaction, attack: moves):
        """Sylvanos frame data and hitbox info"""
        embed, view = move_display('Sylvanos', attack, interaction.user)
        await interaction.response.send_message(embed=embed, view=view)

    # Olympia
    moves = Literal[
        'Jab', 'Dash Attack',
        'Down Tilt', 'Up Tilt', 'Forward Tilt',
        'Neutral Air', 'Down Air', 'Up Air', 'Forward Air', 'Back Air',
        'Down Strong', 'Up Strong', 'Forward Strong', 
        'Up Special/B', 'Neutral Special/B (Gem/Crystal)',
        'Down Special/B (Focus Punch)', 'Side Special/B',
    ]

    @app_commands.command(name='olympia')
    async def olympia(self, interaction: discord.Interaction, attack: moves):
        """Olympia frame data and hitbox info"""
        embed, view = move_display('Olympia', attack, interaction.user)
        await interaction.response.send_message(embed=embed, view=view)

    # Wrastor
    moves = Literal[
        'Jab', 'Dash Attack',
        'Down Tilt', 'Up Tilt', 'Forward Tilt',
        'Neutral Air', 'Down Air', 'Up Air', 'Forward Air', 'Back Air',
        'Down Strong', 'Up Strong (Clap)', 'Forward Strong (Clap)', 
        'Up Special/B', 'Neutral Special/B (Tornado)',
        'Down Special/B', 'Side Special/B (Slipstream)'
    ]

    @app_commands.command(name='wrastor')
    async def wrastor(self, interaction: discord.Interaction, attack: moves):
        """Wrastor frame data and hitbox info"""
        embed, view = move_display('Wrastor', attack, interaction.user)
        await interaction.response.send_message(embed=embed, view=view)

    # Absa
    moves = Literal[
        'Jab', 'Dash Attack',
        'Down Tilt', 'Up Tilt', 'Forward Tilt',
        'Neutral Air', 'Down Air', 'Up Air', 'Forward Air', 'Back Air',
        'Down Strong', 'Up Strong', 'Forward Strong', 
        'Up Special/B (Quick Attack)', 'Neutral Special/B (Cloud Hop/Pop/Thunder Line)',
        'Down Special/B (Cloud Bomb)', 'Side Special/B (Cloud)',
    ]

    @app_commands.command(name='absa')
    async def absa(self, interaction: discord.Interaction, attack: moves):
        """Absa frame data and hitbox info"""
        embed, view = move_display('Absa', attack, interaction.user)
        await interaction.response.send_message(embed=embed, view=view)

    # Elliana
    moves = Literal[
        'Jab', 'Dash Attack',
        'Down Tilt', 'Up Tilt', 'Forward Tilt',
        'Neutral Air', 'Down Air', 'Up Air', 'Forward Air', 'Back Air',
        'Down Strong (Steam)', 'Up Strong (Steam)', 'Forward Strong (Steam)', 
        'Up Special/B (Eject/Mech)', 'Neutral Special/B (Fist)',
        'Down Special/B (Mine)', 'Side Special/B (Missile)',
    ]

    @app_commands.command(name='elliana')
    async def elliana(self, interaction: discord.Interaction, attack: moves):
        """Elliana frame data and hitbox info"""
        embed, view = move_display('Elliana', attack, interaction.user)
        await interaction.response.send_message(embed=embed, view=view)

    # Pomme
    moves = Literal[
        'Jab', 'Dash Attack',
        'Down Tilt', 'Up Tilt', 'Forward Tilt',
        'Neutral Air', 'Down Air', 'Up Air', 'Forward Air', 'Back Air',
        'Down Strong', 'Up Strong', 'Forward Strong', 
        'Up Special/B', 'Neutral Special/B (Notes)',
        'Down Special/B (Harmony Field)', 'Side Special/B (Vince)',
        'Taunt (Mic Drop)'
    ]

    @app_commands.command(name='pomme')
    async def pomme(self, interaction: discord.Interaction, attack: moves):
        """Pomme frame data and hitbox info"""
        embed, view = move_display('Pomme', attack, interaction.user)
        await interaction.response.send_message(embed=embed, view=view)

    # Ori
    moves = Literal[
        'Jab', 'Dash Attack',
        'Down Tilt', 'Up Tilt', 'Forward Tilt',
        'Neutral Air', 'Down Air', 'Up Air', 'Forward Air', 'Back Air',
        'Down Strong', 'Up Strong', 'Forward Strong', 
        'Up Special/B (Parasol)', 'Neutral Special/B (Sein Taps/Charged Flame)',
        'Down Special/B (Bash)', 'Side Special/B (Light Orb)',
        'Taunt'
    ]

    @app_commands.command(name='ori')
    async def ori(self, interaction: discord.Interaction, attack: moves):
        """Ori frame data and hitbox info"""
        embed, view = move_display('Ori', attack, interaction.user)
        await interaction.response.send_message(embed=embed, view=view)

    # Shovel Knight
    moves = Literal[
        'Jab', 'Dash Attack',
        'Down Tilt', 'Up Tilt', 'Forward Tilt',
        'Neutral Air', 'Down Air', 'Up Air', 'Forward Air', 'Back Air',
        'Down Strong', 'Up Strong (Rock)', 'Forward Strong', 
        'Up Special/B', 'Neutral Special/B (War Horn/Mobile Gear/Ghost Gloves)',
        'Down Special/B', 'Side Special/B (Infinidagger)',
        'Taunt'
    ]

    @app_commands.command(name='shovelknight')
    async def shovelknight(self, interaction: discord.Interaction, attack: moves):
        """Shovel Knight frame data and hitbox info"""
        embed, view = move_display('Shovel Knight', attack, interaction.user)
        await interaction.response.send_message(embed=embed, view=view)


async def setup(bot: commands.Bot):
    await bot.add_cog(Hitboxes(bot))
