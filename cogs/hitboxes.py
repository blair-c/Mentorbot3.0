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
    def __init__(self, name: str, embed: discord.Embed, user: discord.User):
        self.embed = embed
        self.user = user
        super().__init__(label=name, style=discord.ButtonStyle.gray)

    async def callback(self, interaction):
        if self.user == interaction.user:
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
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Zetterburn Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/zetterburn#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Zetterburn Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/zetterburn#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Zetterburn Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/zetterburn#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Zetterburn Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/zetterburn#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Zetterburn Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/zetterburn#neutral-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Zetterburn Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            link = 'https://rivals.academy/library/zetterburn#forward-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Zetterburn Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/zetterburn#back-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Zetterburn Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/zetterburn#up-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Zetterburn Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/zetterburn#down-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Zetterburn Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong':
            move = char.forwardStrong
            link = 'https://rivals.academy/library/zetterburn#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Zetterburn Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Strong':
            move = char.upStrong
            link = 'https://rivals.academy/library/zetterburn#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Zetterburn Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Strong':
            move = char.downStrong
            link = 'https://rivals.academy/library/zetterburn#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Zetterburn Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Special/B (Shine)':
            move = char.neutralSpecial
            link = 'https://rivals.academy/library/zetterburn#neutral-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Zetterburn Neutral Special: Shine', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Side Special/B (Fireball)':
            move = char.sideSpecial
            link = 'https://rivals.academy/library/zetterburn#side-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Zetterburn Side Special: Fireball', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Special/B':
            move = char.upSpecial
            link = 'https://rivals.academy/library/zetterburn#up-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
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
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Forsburn Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/forsburn#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Forsburn Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/forsburn#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Forsburn Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/forsburn#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Forsburn Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/forsburn#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Forsburn Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/forsburn#neutral-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Forsburn Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            link = 'https://rivals.academy/library/forsburn#forward-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Forsburn Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/forsburn#back-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Forsburn Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/forsburn#up-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Forsburn Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/forsburn#down-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Forsburn Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong (Cape)':
            move = char.forwardStrong
            link = 'https://rivals.academy/library/forsburn#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Forsburn Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Strong (Cape)':
            move = char.upStrong
            link = 'https://rivals.academy/library/forsburn#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Forsburn Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Strong':
            move = char.downStrong
            link = 'https://rivals.academy/library/forsburn#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Forsburn Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        # elif attack == 'Neutral Special/B (Smoke)':
        #     move = char.neutralSpecial
        #     link = 'https://rivals.academy/library/forsburn#neutral-special'
        #     desc = link
        #     embed = discord.Embed(color=info['color'], description=desc)
        #     embed.set_image(url=move[0].image.highRes)
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
            view.add_item(MoveSelect(name='Non-Empowered', embed=embed, user=interaction.user))
            # Super Clone
            link = 'https://rivals.academy/library/forsburn#side-special-empowered-super-clone'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Forsburn Empowered Side Special: Super Clone', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Empowered: Super Clone', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Up Special/B':
            move = char.upSpecial
            link = 'https://rivals.academy/library/forsburn#up-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
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
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Clairen Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/clairen#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Clairen Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/clairen#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Clairen Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/clairen#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Clairen Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/clairen#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Clairen Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/clairen#neutral-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Clairen Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            link = 'https://rivals.academy/library/clairen#forward-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Clairen Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/clairen#back-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Clairen Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/clairen#up-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Clairen Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/clairen#down-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Clairen Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong':
            move = char.forwardStrong
            link = 'https://rivals.academy/library/clairen#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Clairen Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Strong':
            move = char.upStrong
            link = 'https://rivals.academy/library/clairen#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Clairen Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Strong':
            move = char.downStrong
            link = 'https://rivals.academy/library/clairen#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Clairen Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Special/B (Grab)':
            move = char.neutralSpecial
            link = 'https://rivals.academy/library/clairen#neutral-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Clairen Neutral Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Side Special/B':
            move = char.sideSpecial
            link = 'https://rivals.academy/library/clairen#side-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Clairen Side Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Special/B':
            move = char.upSpecial
            link = 'https://rivals.academy/library/clairen#up-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Clairen Up Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Special/B (Counter/Plasma Field)':
            move = char.downSpecial
            link = 'https://rivals.academy/library/clairen#down-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
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
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Mollo Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/mollo#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Mollo Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/mollo#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Mollo Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/mollo#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Mollo Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/mollo#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Mollo Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/mollo#neutral-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Mollo Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            link = 'https://rivals.academy/library/mollo#forward-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Mollo Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/mollo#back-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Mollo Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/mollo#up-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Mollo Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/mollo#down-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
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
            view.add_item(MoveSelect(name='No Bomb', embed=embed, user=interaction.user))
            # Bomb Toss
            link = 'https://rivals.academy/library/mollo#forward-strong-bomb-toss'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Mollo Forward Strong: Bomb Toss', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Bomb Toss', embed=embed2, user=interaction.user))
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
            view.add_item(MoveSelect(name='No Bomb', embed=embed, user=interaction.user))
            # Bomb Toss
            link = 'https://rivals.academy/library/mollo#up-strong-bomb-toss'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Mollo Up Strong: Bomb Toss', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Bomb Toss', embed=embed2, user=interaction.user))
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
            view.add_item(MoveSelect(name='No Bomb', embed=embed, user=interaction.user))
            # Bomb Toss
            link = 'https://rivals.academy/library/mollo#down-strong-bomb-toss'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Mollo Down Strong: Bomb Toss', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Bomb Toss', embed=embed2, user=interaction.user))
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
            view.add_item(MoveSelect(name='Bomb Pull', embed=embed, user=interaction.user))
            # Cherry Bomb
            link = 'https://rivals.academy/library/mollo#neutral-special-cherry-bomb-explosion'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Mollo Neutral Special: Cherry Bomb Explosion', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Cherry Bomb', embed=embed2, user=interaction.user))
            # Firecracker
            link = 'https://rivals.academy/library/mollo#neutral-special-firecracker-explosion'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[2].image.highRes)
            embed2.set_author(name='Mollo Neutral Special: Firecracker Explosion', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Firecracker', embed=embed2, user=interaction.user))
            # Flashbang
            link = 'https://rivals.academy/library/mollo#neutral-special-flashbang-explosion'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[3].image.highRes)
            embed2.set_author(name='Mollo Neutral Special: Flashbang Explosion', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Flashbang', embed=embed2, user=interaction.user))
            # Finisher Bomb
            link = 'https://rivals.academy/library/mollo#neutral-special-finisher-bomb-explosion'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[4].image.highRes)
            embed2.set_author(name='Mollo Neutral Special: Finisher Bomb Explosion', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Finisher Bomb', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Side Special/B (Flare Gun)':
            move = char.sideSpecial
            link = 'https://rivals.academy/library/mollo#side-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Mollo Side Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Special/B':
            move = char.upSpecial
            link = 'https://rivals.academy/library/mollo#up-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Mollo Up Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Special/B (Bat)':
            move = char.downSpecial
            link = 'https://rivals.academy/library/mollo#down-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
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
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Orcane Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/orcane#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Orcane Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/orcane#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Orcane Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/orcane#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Orcane Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/orcane#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Orcane Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air (Bounce)':
            move = char.neutralAir
            link = 'https://rivals.academy/library/orcane#neutral-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Orcane Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air (Bubblebutt)':
            move = char.forwardAir
            link = 'https://rivals.academy/library/orcane#forward-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Orcane Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/orcane#back-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Orcane Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air (Bellyflop)':
            move = char.upAir
            link = 'https://rivals.academy/library/orcane#up-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Orcane Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/orcane#down-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
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
            view.add_item(MoveSelect(name='No Puddle', embed=embed, user=interaction.user))
            # Puddle Empowered
            link = 'https://rivals.academy/library/orcane#forward-strong-puddle-empowered'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Orcane Forward Strong: Puddle Empowered', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Puddle Empowered', embed=embed2, user=interaction.user))
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
            view.add_item(MoveSelect(name='No Puddle', embed=embed, user=interaction.user))
            # Puddle Empowered
            link = 'https://rivals.academy/library/orcane#up-strong-puddle-empowered'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Orcane Up Strong: Puddle Empowered', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Puddle Empowered', embed=embed2, user=interaction.user))
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
            view.add_item(MoveSelect(name='No Puddle', embed=embed, user=interaction.user))
            # Puddle Empowered
            link = 'https://rivals.academy/library/orcane#down-strong-puddle-empowered'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Orcane Down Strong: Puddle Empowered', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Puddle Empowered', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Neutral Special/B (Droplet)':
            move = char.neutralSpecial
            link = 'https://rivals.academy/library/orcane#neutral-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
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
            view.add_item(MoveSelect(name='No Puddle', embed=embed, user=interaction.user))
            # Puddle Empowered
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Orcane Side Special: Puddle Empowered', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Puddle Empowered', embed=embed2, user=interaction.user))
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
            view.add_item(MoveSelect(name='Droplet', embed=embed, user=interaction.user))
            # Bubbles
            link = 'https://rivals.academy/library/orcane#down-special-bubbles'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Orcane Down Special: Bubbles', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Bubbles', embed=embed2, user=interaction.user))
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
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Etalus Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/etalus#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Etalus Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/etalus#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Etalus Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/etalus#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Etalus Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/etalus#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Etalus Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/etalus#neutral-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Etalus Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            link = 'https://rivals.academy/library/etalus#forward-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Etalus Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/etalus#back-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Etalus Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/etalus#up-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Etalus Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/etalus#down-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
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
            view.add_item(MoveSelect(name='No Armor', embed=embed, user=interaction.user))
            # Ice Armored
            link = 'https://rivals.academy/library/etalus#forward-strong-ice-armored'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Etalus Forward Strong: Ice Armored', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Ice Armored', embed=embed2, user=interaction.user))
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
            view.add_item(MoveSelect(name='No Armor', embed=embed, user=interaction.user))
            # Ice Armored
            link = 'https://rivals.academy/library/etalus#up-strong-ice-armored'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Etalus Up Strong: Ice Armored', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Ice Armored', embed=embed2, user=interaction.user))
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
            view.add_item(MoveSelect(name='No Armor', embed=embed, user=interaction.user))
            # Ice Armored
            link = 'https://rivals.academy/library/etalus#down-strong-ice-armored'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Etalus Down Strong: Ice Armored', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Ice Armored', embed=embed2, user=interaction.user))
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
            embed.set_image(url=move[0].image.highRes)
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
            view.add_item(MoveSelect(name='No Armor', embed=embed, user=interaction.user))
            # Ice Armored
            link = 'https://rivals.academy/library/etalus#up-special-ice-armored'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Etalus Up Special: Ice Armored', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Ice Armored', embed=embed2, user=interaction.user))
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
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ranno Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/ranno#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ranno Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/ranno#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ranno Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/ranno#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ranno Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/ranno#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ranno Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/ranno#neutral-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ranno Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            link = 'https://rivals.academy/library/ranno#forward-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ranno Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/ranno#back-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ranno Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/ranno#up-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ranno Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/ranno#down-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ranno Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong':
            move = char.forwardStrong
            link = 'https://rivals.academy/library/ranno#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ranno Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Strong':
            move = char.upStrong
            link = 'https://rivals.academy/library/ranno#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ranno Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Strong':
            move = char.downStrong
            link = 'https://rivals.academy/library/ranno#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ranno Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Special/B (Darts/Needles)':
            move = char.neutralSpecial
            link = 'https://rivals.academy/library/ranno#neutral-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
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
            view.add_item(MoveSelect(name='Lunge/Divekick', embed=embed, user=interaction.user))
            # Needle Storm
            link = 'https://rivals.academy/library/ranno#up-special-needle-storm'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Ranno Up Special: Needle Storm', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Needle Storm', embed=embed2, user=interaction.user))
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
            embed.set_image(url=move[0].image.highRes)
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
            view.add_item(MoveSelect(name='Uncharged', embed=embed, user=interaction.user))
            # EX Charged
            link = 'https://rivals.academy/library/hodan#dash-attack-ex-charged'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Hodan Dash Attack: EX Charged', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='EX Charged', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/hodan#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
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
            view.add_item(MoveSelect(name='Uncharged', embed=embed, user=interaction.user))
            # EX Charged
            link = 'https://rivals.academy/library/hodan#dash-attack-ex-charged'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Hodan Up Tilt: EX Charged', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='EX Charged', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/hodan#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Hodan Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/hodan#neutral-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
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
            view.add_item(MoveSelect(name='Uncharged', embed=embed, user=interaction.user))
            # EX Charged
            link = 'https://rivals.academy/library/hodan#forward-air-ex-charged'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Hodan Forward Air: EX Charged', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='EX Charged', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/hodan#back-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Hodan Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/hodan#up-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Hodan Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/hodan#down-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Hodan Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong':
            move = char.forwardStrong
            link = 'https://rivals.academy/library/hodan#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Hodan Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Strong':
            move = char.upStrong
            link = 'https://rivals.academy/library/hodan#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Hodan Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Strong (Parry)':
            move = char.downStrong
            view = View()
            # Uncharged
            link = 'https://rivals.academy/library/hodan#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Hodan Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Uncharged', embed=embed, user=interaction.user))
            # EX Charged
            link = 'https://rivals.academy/library/hodan#down-strong-ex-charged'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Hodan Down Strong: EX Charged', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='EX Charged', embed=embed2, user=interaction.user))
            # EX Charged (Parry Success)
            link = 'https://rivals.academy/library/hodan#down-strong-ex-charged'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[2].image.highRes)
            embed2.set_author(name='Hodan Down Strong: EX Charged (Parry Success)', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='EX Parry Success', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Neutral Special/B (Spin)':
            move = char.neutralSpecial
            link = 'https://rivals.academy/library/hodan#neutral-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
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
            view.add_item(MoveSelect(name='Uncharged', embed=embed, user=interaction.user))
            # EX Charged
            link = 'https://rivals.academy/library/hodan#side-special-ex-charged'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Hodan Side Special: EX Charged', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='EX Charged', embed=embed2, user=interaction.user))
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
            view.add_item(MoveSelect(name='Uncharged', embed=embed, user=interaction.user))
            # EX Charged
            link = 'https://rivals.academy/library/hodan#up-special-ex-charged'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Hodan Up Special: EX Charged', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='EX Charged', embed=embed2, user=interaction.user))
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
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Kragg Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/kragg#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Kragg Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/kragg#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Kragg Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/kragg#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Kragg Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/kragg#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Kragg Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/kragg#neutral-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Kragg Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            link = 'https://rivals.academy/library/kragg#forward-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Kragg Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/kragg#back-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Kragg Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/kragg#up-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Kragg Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/kragg#down-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Kragg Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong':
            move = char.forwardStrong
            link = 'https://rivals.academy/library/kragg#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Kragg Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Strong':
            move = char.upStrong
            link = 'https://rivals.academy/library/kragg#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Kragg Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Strong':
            move = char.downStrong
            link = 'https://rivals.academy/library/kragg#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
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
            view.add_item(MoveSelect(name='Rock Pull/Pickup', embed=embed, user=interaction.user))
            # Rock Throw
            link = 'https://rivals.academy/library/kragg#neutral-special-rock-throw'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Kragg Neutral Special: Rock Throw', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Rock Throw', embed=embed2, user=interaction.user))
            # Rock Shards
            link = 'https://rivals.academy/library/kragg#neutral-special-rock-shards'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[2].image.highRes)
            embed2.set_author(name='Kragg Neutral Special: Rock Shards', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Rock Shards', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Side Special/B':
            move = char.sideSpecial
            link = 'https://rivals.academy/library/kragg#side-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Kragg Side Special', icon_url=info['icon'], url=link)
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
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Kragg Down Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Rock Spikes', embed=embed, user=interaction.user))
            # Rock Shards
            link = 'https://rivals.academy/library/kragg#down-special-aerial-stomp'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Kragg Aerial Down Special', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Aerial Stomp', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Taunt':
            move = char.taunt
            link = 'https://rivals.academy/library/kragg#taunt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Kragg Taunt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)

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
        resp = requests.get(url='https://rivals.academy/library/maypul/data.json')
        char = Box(resp.json())
        info = rivals.characters['Maypul']
        if attack == 'Jab':
            move = char.jab
            link = 'https://rivals.academy/library/maypul#jab'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Maypul Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/maypul#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Maypul Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/maypul#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Maypul Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/maypul#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Maypul Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/maypul#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Maypul Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/maypul#neutral-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Maypul Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            link = 'https://rivals.academy/library/maypul#forward-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Maypul Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/maypul#back-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Maypul Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/maypul#up-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Maypul Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air (Root)':
            move = char.downAir
            link = 'https://rivals.academy/library/maypul#down-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Maypul Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong':
            move = char.forwardStrong
            link = 'https://rivals.academy/library/maypul#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Maypul Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Strong':
            move = char.upStrong
            link = 'https://rivals.academy/library/maypul#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Maypul Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Strong':
            move = char.downStrong
            link = 'https://rivals.academy/library/maypul#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Maypul Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Special/B (Seed)':
            move = char.neutralSpecial
            link = 'https://rivals.academy/library/maypul#neutral-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Maypul Neutral Special: Seed', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Side Special/B':
            move = char.sideSpecial
            link = 'https://rivals.academy/library/maypul#side-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Maypul Side Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Special/B (Tether/Uppercut)':
            move = char.upSpecial
            view = View()
            # Uppercut
            link = 'https://rivals.academy/library/maypul#up-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Maypul Up Special: Uppercut', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Uppercut', embed=embed, user=interaction.user))
            # Tether
            link = 'https://rivals.academy/library/maypul#up-special-tether'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Maypul Up Special: Tether', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Tether', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Down Special/B (Lily)':
            move = char.downSpecial
            view = View()
            # Lily
            link = 'https://rivals.academy/library/maypul#down-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[1].image.highRes)
            embed.set_author(name='Maypul Down Special: Lily', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Lily', embed=embed, user=interaction.user))
            # Aerial
            link = 'https://rivals.academy/library/maypul#down-special-aerial'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[2].image.highRes)
            embed2.set_author(name='Maypul Aerial Down Special', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Aerial', embed=embed2, user=interaction.user))
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
        resp = requests.get(url='https://rivals.academy/library/sylvanos/data.json')
        char = Box(resp.json())
        info = rivals.characters['Sylvanos']
        if attack == 'Jab (Petal Wave)':
            move = char.jab
            view = View()
            # Jab 1-3
            link = 'https://rivals.academy/library/sylvanos#jab'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Sylvanos Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Jab 1-3', embed=embed, user=interaction.user))
            # Jab Special
            link = 'https://rivals.academy/library/sylvanos#jab-jab-special-finisher'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Sylvanos Jab Special: Petal Wave', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Jab Special', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/sylvanos#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Sylvanos Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt (Seed/Flower)':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/sylvanos#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Sylvanos Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/sylvanos#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Sylvanos Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/sylvanos#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Sylvanos Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/sylvanos#neutral-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Maypul Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            link = 'https://rivals.academy/library/sylvanos#forward-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Sylvanos Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air (Pin)':
            move = char.backAir
            link = 'https://rivals.academy/library/sylvanos#back-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Sylvanos Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/sylvanos#up-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Sylvanos Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/sylvanos#down-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Sylvanos Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong':
            move = char.forwardStrong
            link = 'https://rivals.academy/library/sylvanos#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Sylvanos Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Strong':
            move = char.upStrong
            link = 'https://rivals.academy/library/sylvanos#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Sylvanos Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Strong':
            move = char.downStrong
            link = 'https://rivals.academy/library/sylvanos#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Sylvanos Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Special/B (Seed/Flower)':
            move = char.neutralSpecial
            link = 'https://rivals.academy/library/sylvanos#neutral-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Sylvanos Neutral Special: Seed', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Side Special/B (Beast Dash)':
            move = char.sideSpecial
            link = 'https://rivals.academy/library/sylvanos#side-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Sylvanos Side Special: Beast Dash', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Special/B (Burrow)':
            move = char.upSpecial
            view = View()
            # Dive
            link = 'https://rivals.academy/library/sylvanos#up-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Sylvanos Up Special: Dive', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Dive', embed=embed, user=interaction.user))
            # Burrow/Emerge
            link = 'https://rivals.academy/library/sylvanos#up-special-burrow-emerge'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Sylvanos Up Special: Burrow/Emerge', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Burrow/Emerge', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Down Special/B (Howl)':
            move = char.downSpecial
            link = 'https://rivals.academy/library/sylvanos#down-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Sylvanos Down Special: Howl', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)

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
        resp = requests.get(url='https://rivals.academy/library/olympia/data.json')
        char = Box(resp.json())
        info = rivals.characters['Olympia']
        if attack == 'Jab':
            move = char.jab
            link = 'https://rivals.academy/library/olympia#jab'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Olympia Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/olympia#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Olympia Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/olympia#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Olympia Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/olympia#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Olympia Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/olympia#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Olympia Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/olympia#neutral-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Olympia Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            link = 'https://rivals.academy/library/olympia#forward-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Olympia Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/olympia#back-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Olympia Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/olympia#up-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Olympia Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/olympia#down-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Olympia Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong':
            move = char.forwardStrong
            link = 'https://rivals.academy/library/olympia#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Olympia Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Strong':
            move = char.upStrong
            link = 'https://rivals.academy/library/olympia#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Olympia Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Strong':
            move = char.downStrong
            link = 'https://rivals.academy/library/olympia#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Olympia Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Special/B (Gem/Crystal)':
            move = char.neutralSpecial
            view = View()
            # Throw Gem
            link = 'https://rivals.academy/library/olympia#neutral-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Olympia Neutral Special: Throw Gem', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Throw Gem', embed=embed, user=interaction.user))
            # Activate Gem Field
            link = 'https://rivals.academy/library/olympia#neutral-special-activate-gem-field'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Olympia Neutral Special: Activate Gem Field', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Activate Gem Field', embed=embed2, user=interaction.user))
            # Crystallize (Break Out)
            link = 'https://rivals.academy/library/olympia#neutral-special-crystallize-break-out'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[2].image.highRes)
            embed2.set_author(name='Olympia Neutral Special: Crystallize (Break Out)', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Crystallize', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Side Special/B':
            move = char.sideSpecial
            link = 'https://rivals.academy/library/olympia#side-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Olympia Side Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Special/B':
            move = char.upSpecial
            link = 'https://rivals.academy/library/olympia#up-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Olympia Up Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Special/B (Focus Punch)':
            move = char.downSpecial
            view = View()
            # Focus Punch
            link = 'https://rivals.academy/library/olympia#down-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Olympia Down Special: Focus Punch', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Focus Punch', embed=embed, user=interaction.user))
            # Crystallize (Break Out)
            link = 'https://rivals.academy/library/olympia#down-special-crystallize-break-out'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Olympia Down Special: Crystallize (Break Out)', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Crystallize', embed=embed2, user=interaction.user))
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
        resp = requests.get(url='https://rivals.academy/library/wrastor/data.json')
        char = Box(resp.json())
        info = rivals.characters['Wrastor']
        if attack == 'Jab':
            move = char.jab
            link = 'https://rivals.academy/library/wrastor#jab'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Wrastor Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/wrastor#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Wrastor Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/wrastor#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Wrastor Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/wrastor#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Wrastor Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/wrastor#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Wrastor Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/wrastor#neutral-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Wrastor Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            link = 'https://rivals.academy/library/wrastor#forward-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Wrastor Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/wrastor#back-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Wrastor Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/wrastor#up-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Wrastor Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/wrastor#down-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Wrastor Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong (Clap)':
            move = char.forwardStrong
            link = 'https://rivals.academy/library/wrastor#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Wrastor Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Strong (Clap)':
            move = char.upStrong
            link = 'https://rivals.academy/library/wrastor#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Wrastor Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Strong':
            move = char.downStrong
            link = 'https://rivals.academy/library/wrastor#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Wrastor Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Special/B (Tornado)':
            move = char.neutralSpecial
            link = 'https://rivals.academy/library/wrastor#neutral-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Wrastor Neutral Special: Tornado', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Side Special/B (Slipstream)':
            move = char.sideSpecial
            link = 'https://rivals.academy/library/wrastor#side-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Wrastor Side Special: Slipstream', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Special/B':
            move = char.upSpecial
            link = 'https://rivals.academy/library/wrastor#up-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Wrastor Up Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Special/B':
            move = char.downSpecial
            link = 'https://rivals.academy/library/wrastor#down-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Wrastor Down Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)

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
        resp = requests.get(url='https://rivals.academy/library/absa/data.json')
        char = Box(resp.json())
        info = rivals.characters['Absa']
        if attack == 'Jab':
            move = char.jab
            link = 'https://rivals.academy/library/absa#jab'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Absa Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/absa#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Absa Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            view = View()
            # Ftilt1
            link = 'https://rivals.academy/library/absa#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Absa Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Ftilt1', embed=embed, user=interaction.user))
            # Ftilt2
            link = 'https://rivals.academy/library/absa#forward-tilt-lightning-whip-ftilt2'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Absa Forward Tilt: Lightning Whip', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Ftilt2', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/absa#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Absa Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/absa#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Absa Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/absa#neutral-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Absa Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            view = View()
            # No Cloud
            link = 'https://rivals.academy/library/absa#forward-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Absa Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='No Cloud', embed=embed, user=interaction.user))
            # Cloud Kick
            link = 'https://rivals.academy/library/absa#forward-air-cloud-kick'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Absa Forward Air: Cloud Kick', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Cloud Kick', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Back Air':
            move = char.backAir
            view = View()
            # No Cloud
            link = 'https://rivals.academy/library/absa#back-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Absa Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='No Cloud', embed=embed, user=interaction.user))
            # Cloud Kick
            link = 'https://rivals.academy/library/absa#back-air-cloud-kick'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Absa Back Air: Cloud Kick', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Cloud Kick', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/absa#up-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Absa Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            view = View()
            # No Cloud
            link = 'https://rivals.academy/library/absa#down-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Absa Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='No Cloud', embed=embed, user=interaction.user))
            # Cloud Kick
            link = 'https://rivals.academy/library/absa#down-air-cloud-kick'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Absa Down Air: Cloud Kick', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Cloud Kick', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Forward Strong':
            move = char.forwardStrong
            link = 'https://rivals.academy/library/absa#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Absa Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Strong':
            move = char.upStrong
            link = 'https://rivals.academy/library/absa#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Absa Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Strong':
            move = char.downStrong
            link = 'https://rivals.academy/library/absa#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Absa Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Special/B (Cloud Hop/Pop/Thunder Line)':
            move = char.neutralSpecial
            view = View()
            # Cloud Hop/Pop
            link = 'https://rivals.academy/library/absa#neutral-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Absa Neutral Special: Cloud', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Cloud Hop/Pop', embed=embed, user=interaction.user))
            # Thunder Line
            link = 'https://rivals.academy/library/absa#neutral-special-thunder-line'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Absa Neutral Special: Thunder Line', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Thunder Line', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Side Special/B (Cloud)':
            move = char.sideSpecial
            link = 'https://rivals.academy/library/absa#side-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Absa Side Special: Cloud', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Special/B (Quick Attack)':
            move = char.upSpecial
            link = 'https://rivals.academy/library/absa#up-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Absa Up Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Special/B (Cloud Bomb)':
            move = char.downSpecial
            view = View()
            # Cloud Bomb
            link = 'https://rivals.academy/library/absa#down-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Absa Down Special: Cloud Bomb', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Cloud Bomb', embed=embed, user=interaction.user))
            # Charged to Absa
            link = 'https://rivals.academy/library/absa#down-special-charged-to-absa'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Absa Down Special: Charged to Absa', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Charged to Absa', embed=embed2, user=interaction.user))
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
        resp = requests.get(url='https://rivals.academy/library/elliana/data.json')
        char = Box(resp.json())
        info = rivals.characters['Elliana']
        if attack == 'Jab':
            move = char.jab
            link = 'https://rivals.academy/library/elliana#jab'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Elliana Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/elliana#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Elliana Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/elliana#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Elliana Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/elliana#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Elliana Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/elliana#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Elliana Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/elliana#neutral-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Elliana Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            link = 'https://rivals.academy/library/elliana#forward-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Elliana Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/elliana#back-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Back Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/elliana#up-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Elliana Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/elliana#down-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Elliana Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong (Steam)':
            move = char.forwardStrong
            view = View()
            # Steam
            link = 'https://rivals.academy/library/elliana#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Elliana Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Steam', embed=embed, user=interaction.user))
            # Overheated
            link = 'https://rivals.academy/library/elliana#forward-strong-overheated'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Elliana Overheated Forward Strong', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Overheated', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Up Strong (Steam)':
            move = char.upStrong
            view = View()
            # Steam
            link = 'https://rivals.academy/library/elliana#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Elliana Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Steam', embed=embed, user=interaction.user))
            # Overheated
            link = 'https://rivals.academy/library/elliana#up-strong-overheated'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Elliana Up Forward Strong', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Overheated', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Down Strong (Steam)':
            move = char.downStrong
            view = View()
            # Steam
            link = 'https://rivals.academy/library/down#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Elliana Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Steam', embed=embed, user=interaction.user))
            # Overheated
            link = 'https://rivals.academy/library/elliana#down-strong-overheated'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Elliana Overheated Down Strong', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Overheated', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Neutral Special/B (Fist)':
            move = char.neutralSpecial
            link = 'https://rivals.academy/library/elliana#neutral-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Elliana Neutral Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Side Special/B (Missile)':
            move = char.sideSpecial
            view = View()
            # Uncharged
            link = 'https://rivals.academy/library/elliana#side-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Elliana Side Special: Missile', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Uncharged', embed=embed, user=interaction.user))
            # Charged
            link = 'https://rivals.academy/library/elliana#side-special-charged-missile'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Elliana Side Special: Charged Missile', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Charged', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Up Special/B (Eject/Mech)':
            move = char.upSpecial
            view = View()
            # Eject/Rebuild
            link = 'https://rivals.academy/library/elliana#up-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Elliana Up Special: Eject/Rebuild', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Eject/Rebuild', embed=embed, user=interaction.user))
            # Mech Explosion
            link = 'https://rivals.academy/library/elliana#up-special-charged-missile'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Elliana Up Special: Mech Explosion', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Mech Explosion', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Down Special/B (Mine)':
            move = char.downSpecial
            view = View()
            # Plant Mine
            link = 'https://rivals.academy/library/elliana#down-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Elliana Down Special: Plant Mine', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Plant Mine', embed=embed, user=interaction.user))
            # Mine Explosion
            link = 'https://rivals.academy/library/elliana#down-special-mine-explosion'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Elliana Down Special: Mine Explosion', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Mine Explosion', embed=embed2, user=interaction.user))
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
        resp = requests.get(url='https://rivals.academy/library/pomme/data.json')
        char = Box(resp.json())
        info = rivals.characters['Pomme']
        if attack == 'Jab':
            move = char.jab
            link = 'https://rivals.academy/library/pomme#jab'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Pomme Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/pomme#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Pomme Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/pomme#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Pomme Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/pomme#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Pomme Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/pomme#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Pomme Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/pomme#neutral-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Pomme Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            link = 'https://rivals.academy/library/pomme#forward-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Pomme Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/pomme#back-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Pomme Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/pomme#up-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Pomme Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/pomme#down-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Pomme Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong':
            move = char.forwardStrong
            link = 'https://rivals.academy/library/pomme#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Pomme Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Strong':
            move = char.upStrong
            link = 'https://rivals.academy/library/pomme#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Pomme Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Strong':
            move = char.downStrong
            link = 'https://rivals.academy/library/pomme#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Pomme Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Special/B (Notes)':
            move = char.neutralSpecial
            link = 'https://rivals.academy/library/pomme#neutral-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Pomme Neutral Special: Tornado', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Side Special/B (Vince)':
            move = char.sideSpecial
            link = 'https://rivals.academy/library/pomme#side-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Pomme Side Special: Vince', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Special/B':
            move = char.upSpecial
            link = 'https://rivals.academy/library/pomme#up-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Pomme Up Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Special/B (Harmony Field)':
            move = char.downSpecial
            link = 'https://rivals.academy/library/pomme#down-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Pomme Down Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Taunt (Mic Drop)':
            move = char.taunt
            link = 'https://rivals.academy/library/pomme#taunt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Pomme Taunt: Mic Drop', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)

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
        resp = requests.get(url='https://rivals.academy/library/ori/data.json')
        char = Box(resp.json())
        info = rivals.characters['Ori']
        if attack == 'Jab':
            move = char.jab
            link = 'https://rivals.academy/library/ori#jab'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ori Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/ori#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ori Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/ori#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ori Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/ori#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ori Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/ori#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ori Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/ori#neutral-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ori Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            link = 'https://rivals.academy/library/ori#forward-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ori Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/ori#back-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ori Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/ori#up-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ori Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/ori#down-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ori Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong':
            move = char.forwardStrong
            view = View()
            # No Sein
            link = 'https://rivals.academy/library/ori#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ori Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='No Sein', embed=embed, user=interaction.user))
            # Sein Team-Up
            link = 'https://rivals.academy/library/elliana#forward-strong-sein-team-up'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Ori Team-Up Forward Strong', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Sein Team Up', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Up Strong':
            move = char.upStrong
            view = View()
            # No Sein
            link = 'https://rivals.academy/library/ori#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ori Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='No Sein', embed=embed, user=interaction.user))
            # Sein Team-Up
            link = 'https://rivals.academy/library/up#forward-strong-sein-team-up'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Ori Team-Up Up Strong', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Sein Team Up', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Down Strong':
            move = char.downStrong
            view = View()
            # No Sein
            link = 'https://rivals.academy/library/ori#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ori Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='No Sein', embed=embed, user=interaction.user))
            # Sein Team-Up
            link = 'https://rivals.academy/library/elliana#down-strong-sein-team-up'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Ori Team-Up Down Strong', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Sein Team Up', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Neutral Special/B (Sein Taps/Charged Flame)':
            move = char.neutralSpecial
            view = View()
            # Taps
            link = 'https://rivals.academy/library/ori#neutral-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ori Neutral Special: Taps', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Taps', embed=embed, user=interaction.user))
            # Charged
            link = 'https://rivals.academy/library/ori#neutral-special-charged-flame'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Ori Neutral Special: Charged Flame', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Charged Flame', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Side Special/B (Light Orb)':
            move = char.sideSpecial
            link = 'https://rivals.academy/library/ori#side-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ori Side Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Special/B (Parasol)':
            move = char.upSpecial
            link = 'https://rivals.academy/library/ori#up-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ori Up Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Special/B (Bash)':
            move = char.downSpecial
            link = 'https://rivals.academy/library/ori#down-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Ori Down Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)

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
        resp = requests.get(url='https://rivals.academy/library/shovel-knight/data.json')
        char = Box(resp.json())
        info = rivals.characters['Shovel Knight']
        if attack == 'Jab':
            move = char.jab
            link = 'https://rivals.academy/library/shovel-knight#jab'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Shovel Knight Jab', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Dash Attack':
            move = char.dashAttack
            link = 'https://rivals.academy/library/shovel-knight#dash-attack'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Shovel Knight Dash Attack', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Tilt':
            move = char.forwardTilt
            link = 'https://rivals.academy/library/shovel-knight#forward-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Shovel Knight Forward Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Tilt':
            move = char.upTilt
            link = 'https://rivals.academy/library/shovel-knight#up-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Shovel Knight Up Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Tilt':
            move = char.downTilt
            link = 'https://rivals.academy/library/shovel-knight#down-tilt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Shovel Knight Down Tilt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Air':
            move = char.neutralAir
            link = 'https://rivals.academy/library/shovel-knight#neutral-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Shovel Knight Neutral Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Air':
            move = char.forwardAir
            link = 'https://rivals.academy/library/shovel-knight#forward-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Shovel Knight Forward Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Back Air':
            move = char.backAir
            link = 'https://rivals.academy/library/shovel-knight#back-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Shovel Knight Back Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Air':
            move = char.upAir
            link = 'https://rivals.academy/library/shovel-knight#up-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Shovel Knight Up Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Air':
            move = char.downAir
            link = 'https://rivals.academy/library/shovel-knight#down-air'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Shovel Knight Down Air', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Forward Strong':
            move = char.forwardStrong
            link = 'https://rivals.academy/library/shovel-knight#forward-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Shovel Knight Forward Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Up Strong (Rock)':
            move = char.upStrong
            view = View()
            # No Rock
            link = 'https://rivals.academy/library/shovel-knight#up-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Shovel Knight Up Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='No Rock', embed=embed, user=interaction.user))
            # Rock
            link = 'https://rivals.academy/library/shovel-knight#up-strong-rock'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Shovel Knight Up Strong Rock', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Rock', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Down Strong':
            move = char.downStrong
            link = 'https://rivals.academy/library/shovel-knight#down-strong'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Shovel Knight Down Strong', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Neutral Special/B (War Horn/Mobile Gear/Ghost Gloves)':
            move = char.neutralSpecial
            view = View()
            # Coin Capture
            # link = 'https://rivals.academy/library/shovel-knight#neutral-special'
            # desc = link
            # embed = discord.Embed(color=info['color'], description=desc)
            # embed.set_author(name='Shovel Knight Neutral Special: Coin Capture', icon_url=info['icon'], url=link)
            # embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            # view.add_item(MoveSelect(name='Coin Capture', embed=embed))
            # War Horn
            link = 'https://rivals.academy/library/shovel-knight#neutral-special-war-horn'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[1].image.highRes)
            embed.set_author(name='Shovel Knight Neutral Special: War Horn', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='War Horn', embed=embed, user=interaction.user))
            # Mobile Gear
            link = 'https://rivals.academy/library/shovel-knight#neutral-special-mobile-gear'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[2].image.highRes)
            embed2.set_author(name='Shovel Knight Neutral Special: Mobile Gear', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Mobile Gear', embed=embed2, user=interaction.user))
            # Ghost Gloves
            link = 'https://rivals.academy/library/shovel-knight#neutral-special-ghost-gloves'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[3].image.highRes)
            embed2.set_author(name='Shovel Knight Neutral Special: Ghost Gloves', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Ghost Gloves', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Side Special/B (Infinidagger)':
            move = char.sideSpecial
            view = View()
            # Charge
            link = 'https://rivals.academy/library/shovel-knight#side-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Shovel Knight Side Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Charge', embed=embed, user=interaction.user))
            # Infinidagger
            link = 'https://rivals.academy/library/shovel-knight#side-special-infinidagger'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Shovel Knight Side Special: Infinidagger', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Infinidagger', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Up Special/B':
            move = char.upSpecial
            link = 'https://rivals.academy/library/shovel-knight#up-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Shovel Knight Up Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)
        elif attack == 'Down Special/B':
            move = char.downSpecial
            view = View()
            # Anchor
            link = 'https://rivals.academy/library/shovel-knight#down-special'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Shovel Knight Down Special', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Anchor', embed=embed, user=interaction.user))
            # Infinidagger
            link = 'https://rivals.academy/library/shovel-knight#down-special-treasure-pile'
            desc = link
            embed2 = discord.Embed(color=info['color'], description=desc)
            embed2.set_image(url=move[1].image.highRes)
            embed2.set_author(name='Shovel Knight Down Special: Treasure Pile', icon_url=info['icon'], url=link)
            embed2.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            view.add_item(MoveSelect(name='Treasure Pile', embed=embed2, user=interaction.user))
            await interaction.response.send_message(embed=embed, view=view)
        elif attack == 'Taunt':
            move = char.taunt
            link = 'https://rivals.academy/library/shovel-knight#taunt'
            desc = link
            embed = discord.Embed(color=info['color'], description=desc)
            embed.set_image(url=move[0].image.highRes)
            embed.set_author(name='Shovel Knight Taunt', icon_url=info['icon'], url=link)
            embed.set_footer(text=f'Up-to-date as of Patch {char.patch}')
            await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Hitboxes(bot))
