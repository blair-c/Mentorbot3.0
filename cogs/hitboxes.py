import json, requests
from typing import Literal

from box import Box
import discord
from discord import app_commands
from discord.ui import Button, View
from discord.ext import commands
from tabulate import tabulate

from data import rivals


class MoveSelect(Button):
    """"""
    def __init__(self, name: str, embed: discord.Embed):
        self.embed = embed
        super().__init__(label=name, style=discord.ButtonStyle.gray)

    async def callback(self, interaction):
        await interaction.response.edit_message(embed=self.embed)


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
        resp = requests.get(url='https://rivals.academy/library/zetterburn/data.json')
        char = Box(resp.json())
        info = rivals.characters['Zetterburn']
        if attack == 'Jab':
            move = char.jab
            link = 'https://rivals.academy/library/zetterburn#jab'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Zetterburn Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/zetterburn#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Zetterburn Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/zetterburn#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Zetterburn Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/zetterburn#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Zetterburn Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/zetterburn#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Zetterburn Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/zetterburn#neutral-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Zetterburn Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            link = 'https://rivals.academy/library/zetterburn#forward-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Zetterburn Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/zetterburn#back-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Zetterburn Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/zetterburn#up-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Zetterburn Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/zetterburn#down-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Zetterburn Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong':
            move = char.forwardStrong
            link = 'https://rivals.academy/library/zetterburn#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Zetterburn Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Strong':
            move = char.upStrong
            link = 'https://rivals.academy/library/zetterburn#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Zetterburn Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Strong':
            move = char.downStrong
            link = 'https://rivals.academy/library/zetterburn#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Zetterburn Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Special/B (Shine)':
            move = char.neutralSpecial
            link = 'https://rivals.academy/library/zetterburn#neutral-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Zetterburn Neutral Special: Shine', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Side Special/B (Fireball)':
            move = char.sideSpecial
            link = 'https://rivals.academy/library/zetterburn#side-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Zetterburn Side Special: Fireball', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Special/B':
            move = char.upSpecial
            link = 'https://rivals.academy/library/zetterburn#up-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Zetterburn Up Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Special/B':
            move = char.downSpecial
            link = 'https://rivals.academy/library/zetterburn#down-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Zetterburn Down Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)

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
        resp = requests.get(url='https://rivals.academy/library/forsburn/data.json')
        char = Box(resp.json())
        info = rivals.characters['Forsburn']
        if attack == 'Jab':
            move = char.jab
            link = 'https://rivals.academy/library/forsburn#jab'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Forsburn Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/forsburn#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Forsburn Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/forsburn#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Forsburn Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/forsburn#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Forsburn Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/forsburn#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Forsburn Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/forsburn#neutral-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Forsburn Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            link = 'https://rivals.academy/library/forsburn#forward-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Forsburn Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/forsburn#back-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Forsburn Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/forsburn#up-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Forsburn Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/forsburn#down-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Forsburn Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong (Cape)':
            move = char.forwardStrong
            link = 'https://rivals.academy/library/forsburn#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Forsburn Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Strong (Cape)':
            move = char.upStrong
            link = 'https://rivals.academy/library/forsburn#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Forsburn Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Strong':
            move = char.downStrong
            link = 'https://rivals.academy/library/forsburn#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Forsburn Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        # elif attack == 'Neutral Special/B (Smoke)':
        #     move = char.neutralSpecial
        #     link = 'https://rivals.academy/library/forsburn#neutral-special'
        #     desc = link
        #     embed = discord.Embed(color=info['color'], description=desc)
        #     embed.set_image(url=move.image.highRes)
        #     embed.set_author(name='Forsburn Neutral Special', icon_url=info['icon'], url=link)
        #     embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
        #     await interaction.response.send_message(embed=embed)
        elif attack == 'Side Special/B (Clone)':
            move = char.sideSpecial
            view = View()
            # Clone
            link = 'https://rivals.academy/library/forsburn#side-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Forsburn Side Special: Clone', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Non-Empowered', embed=embed))
            # Super Clone
            link = 'https://rivals.academy/library/forsburn#side-special-empowered-super-clone'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Forsburn Empowered Side Special: Super Clone', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Empowered: Super Clone', embed=embed2))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Up Special/B':
            move = char.upSpecial
            link = 'https://rivals.academy/library/forsburn#up-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Forsburn Up Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Special/B (Combust)':
            move = char.downSpecial
            link = 'https://rivals.academy/library/forsburn#down-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[1].image.highRes)
            embed.set_author(name='Forsburn Down Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)

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
        resp = requests.get(url='https://rivals.academy/library/clairen/data.json')
        char = Box(resp.json())
        info = rivals.characters['Clairen']
        if attack == 'Jab':
            move = char.jab
            link = 'https://rivals.academy/library/clairen#jab'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Clairen Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/clairen#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Clairen Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/clairen#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Clairen Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/clairen#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Clairen Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/clairen#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Clairen Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/clairen#neutral-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Clairen Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            link = 'https://rivals.academy/library/clairen#forward-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Clairen Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/clairen#back-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Clairen Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/clairen#up-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Clairen Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/clairen#down-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Clairen Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong':
            move = char.forwardStrong
            link = 'https://rivals.academy/library/clairen#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Clairen Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Strong':
            move = char.upStrong
            link = 'https://rivals.academy/library/clairen#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Clairen Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Strong':
            move = char.downStrong
            link = 'https://rivals.academy/library/clairen#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Clairen Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Special/B (Grab)':
            move = char.neutralSpecial
            link = 'https://rivals.academy/library/clairen#neutral-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Clairen Neutral Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Side Special/B':
            move = char.sideSpecial
            link = 'https://rivals.academy/library/clairen#side-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Clairen Side Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Special/B':
            move = char.upSpecial
            link = 'https://rivals.academy/library/clairen#up-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Clairen Up Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Special/B (Counter/Plasma Field)':
            move = char.downSpecial
            link = 'https://rivals.academy/library/clairen#down-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[1].image.highRes)
            embed.set_author(name='Clairen Down Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)

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
        resp = requests.get(url='https://rivals.academy/library/mollo/data.json')
        char = Box(resp.json())
        info = rivals.characters['Mollo']
        if attack == 'Jab (Spray Paint)':
            move = char.jab
            link = 'https://rivals.academy/library/mollo#jab'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Mollo Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/mollo#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Mollo Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/mollo#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Mollo Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/mollo#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Mollo Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/mollo#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Mollo Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/mollo#neutral-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Mollo Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            link = 'https://rivals.academy/library/mollo#forward-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Mollo Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/mollo#back-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Mollo Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/mollo#up-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Mollo Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/mollo#down-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Mollo Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong':
            move = char.forwardStrong
            view = View()
            # No Bomb
            link = 'https://rivals.academy/library/mollo#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Mollo Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='No Bomb', embed=embed))
            # Bomb Toss
            link = 'https://rivals.academy/library/mollo#forward-strong-bomb-toss'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Mollo Forward Strong: Bomb Toss', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Bomb Toss', embed=embed2))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Up Strong':
            move = char.upStrong
            view = View()
            # No Bomb
            link = 'https://rivals.academy/library/mollo#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Mollo Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='No Bomb', embed=embed))
            # Bomb Toss
            link = 'https://rivals.academy/library/mollo#up-strong-bomb-toss'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Mollo Up Strong: Bomb Toss', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Bomb Toss', embed=embed2))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Down Strong':
            move = char.downStrong
            view = View()
            # No Bomb
            link = 'https://rivals.academy/library/mollo#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Mollo Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='No Bomb', embed=embed))
            # Bomb Toss
            link = 'https://rivals.academy/library/mollo#down-strong-bomb-toss'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Mollo Down Strong: Bomb Toss', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Bomb Toss', embed=embed2))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Neutral Special/B (Bomb Pull/Cherry/Firecracker/Flashbang/Finisher)':
            move = char.neutralSpecial
            view = View()
            # Bomb Pull
            link = 'https://rivals.academy/library/mollo#neutral-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Mollo Neutral Special: Bomb Pull', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Bomb Pull', embed=embed))
            # Cherry Bomb
            link = 'https://rivals.academy/library/mollo#neutral-special-cherry-bomb-explosion'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Mollo Neutral Special: Cherry Bomb Explosion', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Cherry Bomb', embed=embed2))
            # Firecracker
            link = 'https://rivals.academy/library/mollo#neutral-special-firecracker-explosion'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[2].image.highRes)
            embed2.set_author(name='Mollo Neutral Special: Firecracker Explosion', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Firecracker', embed=embed2))
            # Flashbang
            link = 'https://rivals.academy/library/mollo#neutral-special-flashbang-explosion'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[3].image.highRes)
            embed2.set_author(name='Mollo Neutral Special: Flashbang Explosion', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Flashbang', embed=embed2))
            # Finisher Bomb
            link = 'https://rivals.academy/library/mollo#neutral-special-finisher-bomb-explosion'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[4].image.highRes)
            embed2.set_author(name='Mollo Neutral Special: Finisher Bomb Explosion', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Finisher Bomb', embed=embed2))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Side Special/B (Flare Gun)':
            move = char.sideSpecial
            link = 'https://rivals.academy/library/mollo#side-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Mollo Side Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Special/B':
            move = char.upSpecial
            link = 'https://rivals.academy/library/mollo#up-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Mollo Up Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Special/B (Bat)':
            move = char.downSpecial
            link = 'https://rivals.academy/library/mollo#down-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Mollo Down Special: Bat', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)

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
        resp = requests.get(url='https://rivals.academy/library/orcane/data.json')
        char = Box(resp.json())
        info = rivals.characters['Orcane']
        if attack == 'Jab':
            move = char.jab
            link = 'https://rivals.academy/library/orcane#jab'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Orcane Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/orcane#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Orcane Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/orcane#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Orcane Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/orcane#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Orcane Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/orcane#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Orcane Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air (Bounce)':
            move = char.neutralAir
            link = 'https://rivals.academy/library/orcane#neutral-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Orcane Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air (Bubblebutt)':
            move = char.forwardAir
            link = 'https://rivals.academy/library/orcane#forward-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Orcane Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/orcane#back-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Orcane Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air (Bellyflop)':
            move = char.upAir
            link = 'https://rivals.academy/library/orcane#up-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Orcane Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/orcane#down-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Orcane Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong':
            move = char.forwardStrong
            view = View()
            # No Puddle
            link = 'https://rivals.academy/library/orcane#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Orcane Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='No Puddle', embed=embed))
            # Puddle Empowered
            link = 'https://rivals.academy/library/orcane#forward-strong-puddle-empowered'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Orcane Forward Strong: Puddle Empowered', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Puddle Empowered', embed=embed2))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Up Strong':
            move = char.upStrong
            view = View()
            # No Puddle
            link = 'https://rivals.academy/library/orcane#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Orcane Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='No Puddle', embed=embed))
            # Puddle Empowered
            link = 'https://rivals.academy/library/orcane#up-strong-puddle-empowered'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Orcane Up Strong: Puddle Empowered', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Puddle Empowered', embed=embed2))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Down Strong':
            move = char.downStrong
            view = View()
            # No Puddle
            link = 'https://rivals.academy/library/orcane#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Orcane Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='No Puddle', embed=embed))
            # Puddle Empowered
            link = 'https://rivals.academy/library/orcane#down-strong-puddle-empowered'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Orcane Down Strong: Puddle Empowered', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Puddle Empowered', embed=embed2))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Neutral Special/B (Droplet)':
            move = char.neutralSpecial
            link = 'https://rivals.academy/library/orcane#neutral-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Orcane Neutral Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Side Special/B':
            move = char.sideSpecial
            view = View()
            # No Puddle
            link = 'https://rivals.academy/library/orcane#side-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Orcane Side Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='No Puddle', embed=embed))
            # Puddle Empowered
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Orcane Side Special: Puddle Empowered', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Puddle Empowered', embed=embed2))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Up Special/B (Teleport)':
            move = char.upSpecial
            link = 'https://rivals.academy/library/orcane#up-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Orcane Up Special: Teleport', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Special/B (Bubbles/Puddle)':
            move = char.downSpecial
            view = View()
            # Droplet/Puddle
            link = 'https://rivals.academy/library/orcane#down-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Orcane Down Special: Droplet/Puddle', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Droplet', embed=embed))
            # Bubbles
            link = 'https://rivals.academy/library/orcane#down-special-bubbles'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Orcane Down Special: Bubbles', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Bubbles', embed=embed2))
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
        resp = requests.get(url='https://rivals.academy/library/etalus/data.json')
        char = Box(resp.json())
        info = rivals.characters['Etalus']
        if attack == 'Jab':
            move = char.jab
            link = 'https://rivals.academy/library/etalus#jab'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Etalus Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/etalus#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Etalus Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/etalus#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Etalus Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/etalus#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Etalus Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/etalus#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Etalus Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/etalus#neutral-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Etalus Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            link = 'https://rivals.academy/library/etalus#forward-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Etalus Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/etalus#back-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Etalus Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/etalus#up-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Etalus Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/etalus#down-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Etalus Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong':
            move = char.forwardStrong
            view = View()
            # No Armor
            link = 'https://rivals.academy/library/etalus#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Etalus Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='No Armor', embed=embed))
            # Ice Armored
            link = 'https://rivals.academy/library/etalus#forward-strong-ice-armored'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Etalus Forward Strong: Ice Armored', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Ice Armored', embed=embed2))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Up Strong':
            move = char.upStrong
            view = View()
            # No Armor
            link = 'https://rivals.academy/library/etalus#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Etalus Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='No Armor', embed=embed))
            # Ice Armored
            link = 'https://rivals.academy/library/etalus#up-strong-ice-armored'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Etalus Up Strong: Ice Armored', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Ice Armored', embed=embed2))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Down Strong':
            move = char.downStrong
            view = View()
            # No Armor
            link = 'https://rivals.academy/library/etalus#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Etalus Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='No Armor', embed=embed))
            # Ice Armored
            link = 'https://rivals.academy/library/etalus#down-strong-ice-armored'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Etalus Down Strong: Ice Armored', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Ice Armored', embed=embed2))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Neutral Special/B (Hammer)':
            move = char.neutralSpecial
            link = 'https://rivals.academy/library/etalus#neutral-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Etalus Neutral Special: Hammer', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Side Special/B (Icicles)':
            move = char.sideSpecial
            link = 'https://rivals.academy/library/etalus#side-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Etalus Side Special: Icicles', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Special/B':
            move = char.upSpecial
            view = View()
            # No Armor
            link = 'https://rivals.academy/library/etalus#up-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Etalus Up Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='No Armor', embed=embed))
            # Ice Armored
            link = 'https://rivals.academy/library/etalus#up-special-ice-armored'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Etalus Up Special: Ice Armored', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Ice Armored', embed=embed2))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Down Special/B (Freeze)':
            move = char.downSpecial
            link = 'https://rivals.academy/library/etalus#down-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Etalus Down Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)

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
        resp = requests.get(url='https://rivals.academy/library/ranno/data.json')
        char = Box(resp.json())
        info = rivals.characters['Ranno']
        if attack == 'Jab':
            move = char.jab
            link = 'https://rivals.academy/library/ranno#jab'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Ranno Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/ranno#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Ranno Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/ranno#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Ranno Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/ranno#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Ranno Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/ranno#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Ranno Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/ranno#neutral-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Ranno Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            link = 'https://rivals.academy/library/ranno#forward-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Ranno Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/ranno#back-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Ranno Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/ranno#up-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Ranno Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/ranno#down-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Ranno Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong':
            move = char.forwardStrong
            link = 'https://rivals.academy/library/ranno#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Ranno Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Strong':
            move = char.upStrong
            link = 'https://rivals.academy/library/ranno#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Ranno Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Strong':
            move = char.downStrong
            link = 'https://rivals.academy/library/ranno#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Ranno Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Special/B (Darts/Needles)':
            move = char.neutralSpecial
            link = 'https://rivals.academy/library/ranno#neutral-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Ranno Neutral Special: Poison Darts', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Side Special/B (Tongue)':
            move = char.sideSpecial
            link = 'https://rivals.academy/library/ranno#side-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ranno Side Special: Tongue', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Special/B (Divekick/Needle Storm)':
            move = char.upSpecial
            view = View()
            # Lunge/Divekick
            link = 'https://rivals.academy/library/ranno#up-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ranno Up Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Lunge/Divekick', embed=embed))
            # Needle Storm
            link = 'https://rivals.academy/library/ranno#up-special-needle-storm'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Ranno Up Special: Needle Storm', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Needle Storm', embed=embed2))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Down Special/B (Bubble)':
            move = char.downSpecial
            link = 'https://rivals.academy/library/ranno#down-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ranno Down Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)

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
        resp = requests.get(url='https://rivals.academy/library/hodan/data.json')
        char = Box(resp.json())
        info = rivals.characters['Hodan']
        if attack == 'Jab':
            move = char.jab
            link = 'https://rivals.academy/library/hodan#jab'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Hodan Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            view = View()
            # Uncharged
            link = 'https://rivals.academy/library/hodan#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Hodan Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Uncharged', embed=embed))
            # EX Charged
            link = 'https://rivals.academy/library/hodan#dash-attack-ex-charged'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Hodan Dash Attack: EX Charged', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='EX Charged', embed=embed2))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/hodan#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Hodan Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            view = View()
            # Uncharged
            link = 'https://rivals.academy/library/hodan#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Hodan Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Uncharged', embed=embed))
            # EX Charged
            link = 'https://rivals.academy/library/hodan#dash-attack-ex-charged'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Hodan Up Tilt: EX Charged', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='EX Charged', embed=embed2))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/hodan#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Hodan Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/hodan#neutral-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Hodan Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            view = View()
            # Uncharged
            link = 'https://rivals.academy/library/hodan#forward-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Hodan Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Uncharged', embed=embed))
            # EX Charged
            link = 'https://rivals.academy/library/hodan#forward-air-ex-charged'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Hodan Forward Air: EX Charged', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='EX Charged', embed=embed2))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/hodan#back-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Hodan Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/hodan#up-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Hodan Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/hodan#down-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Hodan Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong':
            move = char.forwardStrong
            link = 'https://rivals.academy/library/hodan#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Hodan Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Strong':
            move = char.upStrong
            link = 'https://rivals.academy/library/hodan#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Hodan Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Strong (Parry)':
            move = char.downStrong
            # Uncharged
            link = 'https://rivals.academy/library/hodan#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Hodan Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Uncharged', embed=embed))
            # EX Charged
            link = 'https://rivals.academy/library/hodan#down-strong-ex-charged'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Hodan Down Strong: EX Charged', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='EX Charged', embed=embed2))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Neutral Special/B (Spin)':
            move = char.neutralSpecial
            link = 'https://rivals.academy/library/hodan#neutral-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Hodan Neutral Special: Spin', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Side Special/B (Sweat Spirit)':
            move = char.sideSpecial
            view = View()
            # Uncharged
            link = 'https://rivals.academy/library/hodan#side-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Hodan Side Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Uncharged', embed=embed))
            # EX Charged
            link = 'https://rivals.academy/library/hodan#side-special-ex-charged'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Hodan Side Special: EX Charged', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='EX Charged', embed=embed2))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Up Special/B':
            move = char.upSpecial
            view = View()
            # Uncharged
            link = 'https://rivals.academy/library/hodan#up-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Hodan Up Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Uncharged', embed=embed))
            # EX Charged
            link = 'https://rivals.academy/library/hodan#up-special-ex-charged'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Hodan Up Special: EX Charged', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='EX Charged', embed=embed2))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Down Special/B (Mud Slam/Bury)':
            move = char.downSpecial
            link = 'https://rivals.academy/library/hodan#down-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Hodan Down Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)

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
        resp = requests.get(url='https://rivals.academy/library/kragg/data.json')
        char = Box(resp.json())
        info = rivals.characters['Kragg']
        if attack == 'Jab':
            move = char.jab
            link = 'https://rivals.academy/library/kragg#jab'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Kragg Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/kragg#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Kragg Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/kragg#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Kragg Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/kragg#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Kragg Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/kragg#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Kragg Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/kragg#neutral-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Kragg Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            link = 'https://rivals.academy/library/kragg#forward-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Kragg Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/kragg#back-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Kragg Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/kragg#up-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Kragg Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/kragg#down-Air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Kragg Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong':
            move = char.forwardStrong
            link = 'https://rivals.academy/library/kragg#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Kragg Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Strong':
            move = char.upStrong
            link = 'https://rivals.academy/library/kragg#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Kragg Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Strong':
            move = char.downStrong
            link = 'https://rivals.academy/library/kragg#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Kragg Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Special/B (Rock Pull/Shine/Throw/Shards)':
            move = char.neutralSpecial
            view = View()
            # Rock Pull/Pickup/Shine
            link = 'https://rivals.academy/library/kragg#neutral-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Kragg Neutral Special: Rock', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Rock Pull/Pickup', embed=embed))
            # Rock Throw
            link = 'https://rivals.academy/library/kragg#neutral-special-rock-throw'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Kragg Neutral Special: Rock Throw', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Rock Throw', embed=embed2))
            # Rock Shards
            link = 'https://rivals.academy/library/kragg#neutral-special-rock-shards'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[2].image.highRes)
            embed2.set_author(name='Kragg Neutral Special: Rock Shards', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Rock Shards', embed=embed2))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Side Special/B':
            move = char.sideSpecial
            link = 'https://rivals.academy/library/kragg#side-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Kragg Side Special: Fireball', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Special/B (Pillar)':
            move = char.upSpecial
            link = 'https://rivals.academy/library/kragg#up-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Kragg Up Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Special/B (Spikes/Stomp)':
            move = char.downSpecial
            view = View()
            # Rock Throw
            link = 'https://rivals.academy/library/kragg#down-special'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[0].image.highRes)
            embed2.set_author(name='Kragg Down Special: Rock Throw', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Spikes', embed=embed2))
            # Rock Shards
            link = 'https://rivals.academy/library/kragg#down-special-aerial-stomp'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Kragg Down Special: Aerial Stomp', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Aerial', embed=embed2))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Taunt':
            move = char.taunt
            link = 'https://rivals.academy/library/kragg#taunt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move.image.highRes)
            embed.set_author(name='Kragg Taunt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)

    # # Maypul
    # may_moves = moves.copy()
    # may_moves['Down Air'] = 'Root'
    # may_moves['Neutral Special'] = 'Seed'
    # may_moves['Down Special'] = 'Lily'
    # may_moves['Up Special'] = 'Tether/Uppercut'
    # may_moves = [f'{move} ({name})' if name else move  # Formatted list
    #                 for move, name in may_moves.items()]
    # maypmoves = Literal[tuple(may_moves)]  # To pass into command as choices

    # @app_commands.command(name='maypul')
    # async def maypul(self, interaction: discord.Interaction, attack: may_moves):
    #     """Maypul frame data and hitbox info"""
    #     return

    # # Sylvanos
    # sylv_moves = moves.copy()
    # sylv_moves['Jab'] = 'Petal Wave'
    # sylv_moves['Neutral Special'] = 'Seed/Flower'
    # sylv_moves['Down Special'] = 'Howl'
    # sylv_moves['Up Special'] = 'Burrow/Bite'
    # sylv_moves['Side Special'] = 'Beast Dash'
    # sylv_moves = [f'{move} ({name})' if name else move  # Formatted list
    #               for move, name in sylv_moves.items()]
    # sylv_moves = Literal[tuple(sylv_moves)]  # To pass into command as choices

    # @app_commands.command(name='sylvanos')
    # async def sylvanos(self, interaction: discord.Interaction, attack: sylv_moves):
    #     """Sylvanos frame data and hitbox info"""
    #     return

    # # Wrastor
    # wras_moves = moves.copy()
    # wras_moves['Up Strong'] = 'Clap'
    # wras_moves['Forward Strong'] = 'Clap'
    # wras_moves['Neutral Special'] = 'Tornado'
    # wras_moves['Side Special'] = 'Slipstream'
    # wras_moves = [f'{move} ({name})' if name else move  # Formatted list
    #                  for move, name in wras_moves.items()]
    # wras_moves = Literal[tuple(wras_moves)]  # To pass into command as choices

    # @app_commands.command(name='wrastor')
    # async def wrastor(self, interaction: discord.Interaction, attack: wras_moves):
    #     """Wrastor frame data and hitbox info"""
    #     return

    # # Absa
    # absa_moves = moves.copy()
    # absa_moves['Neutral Special'] = 'Cloud/Thunderline'
    # absa_moves['Down Special'] = 'Cloud Bomb'
    # absa_moves['Side Special'] = 'Cloud'
    # absa_moves = [f'{move} ({name})' if name else move  # Formatted list
    #               for move, name in absa_moves.items()]
    # absa_moves = Literal[tuple(absa_moves)]  # To pass into command as choices

    # @app_commands.command(name='absa')
    # async def absa(self, interaction: discord.Interaction, attack: absa_moves):
    #     """Absa frame data and hitbox info"""
    #     return

    # # Elliana
    # elli_moves = moves.copy()
    # elli_moves['Down Strong'] = 'Steam'
    # elli_moves['Up Strong'] = 'Steam'
    # elli_moves['Forward Strong'] = 'Steam'
    # elli_moves['Neutral Special'] = 'Fist'
    # elli_moves['Down Special'] = 'Mine'
    # elli_moves['Up Special'] = 'Eject Mech'
    # elli_moves['Side Special'] = 'Missile'
    # elli_moves = [f'{move} ({name})' if name else move  # Formatted list
    #               for move, name in elli_moves.items()]
    # elli_moves = Literal[tuple(elli_moves)]  # To pass into command as choices

    # @app_commands.command(name='elliana')
    # async def elliana(self, interaction: discord.Interaction, attack: elli_moves):
    #     """Elliana frame data and hitbox info"""
    #     return

    # # Ori
    # ori_moves = moves.copy()
    # ori_moves['Neutral Special'] = 'Sein Taps/Charged Spirit Flame'
    # ori_moves['Down Special'] = 'Bash'
    # ori_moves['Up Special'] = 'Parasol'
    # ori_moves['Side Special'] = 'Light Orb'
    # ori_moves = [f'{move} ({name})' if name else move  # Formatted list
    #              for move, name in ori_moves.items()]
    # ori_moves = Literal[tuple(ori_moves)]  # To pass into command as choices

    # @app_commands.command(name='ori')
    # async def ori(self, interaction: discord.Interaction, attack: ori_moves):
    #     """Ori frame data and hitbox info"""
    #     return

    # # TODO: touch up this system & implementation
    # # Shovel Knight
    # moves['Taunt'] = None  # Add Taunt
    # sk_moves = moves.copy()
    # sk_moves['Up Strong'] = 'Rock'
    # sk_moves['Neutral Special'] = 'Coin Capture/Horn/Mobile Gear/Ghost Gloves'
    # sk_moves['Down Special'] = 'Fish'
    # sk_moves['Up Special'] = 'Anchor'
    # sk_moves['Side Special'] = 'Infinidagger'
    # sk_moves['Taunt'] = 'Shop'
    # sk_moves = [f'{move} ({name})' if name else move  # Formatted list
    #            for move, name in sk_moves.items()]
    # sk_moves = Literal[tuple(sk_moves)]  # To pass into command as choices

    # @app_commands.command(name='shovelknight')
    # async def shovel_knight(self, interaction: discord.Interaction, attack: sk_moves):
    #     """Shovel Knight frame data and hitbox info"""
    #     return


async def setup(bot: commands.Bot):
    await bot.add_cog(Hitboxes(bot))
