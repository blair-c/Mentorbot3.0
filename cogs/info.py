import json, requests
import os

import discord
from discord import app_commands
from discord.ext import commands


class Info(commands.Cog):
    """Send informational Rivals links and formatted displays."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='about')
    async def about_command(self, interaction: discord.Interaction):
        """About Mentorbot"""
        desc = 'A Discord bot by the Rivals of Aether Academy.'
        desc += f'```ml\n{len(self.bot.guilds):,} servers / {len(self.bot.users):,} users```'
        embed = discord.Embed(description=desc)
        embed.set_author(
            name='About Mentorbot 3.0',
            icon_url=self.bot.user.display_avatar.url)
        embed.add_field(
            name='Developed by blair',
            value='https://github.com/blair-c/Mentorbot3.0',
            inline=False)
        embed.add_field(
            name='Data curated by Sector 7-G',
            value='https://rivals.academy/library',
            inline=False)
        embed.add_field(
            name='Profile photo drawn by Sxolian',
            value='https://twitter.com/Sxolian',
            inline=False)
        await interaction.response.send_message(embed=embed)

    # Sector 7-G Documents
    @app_commands.command(name='framedata')
    async def frame_data_doc(self, interaction: discord.Interaction):
        """SNC's frame data document"""
        link = ('https://docs.google.com/spreadsheets/d/'
                '19UtK7xG2c-ehxdlhCFKMpM4_IHSG-EXFgXLJaunE79I')
        patch = requests.get(url='https://rivals.academy/library/pomme/data.json').json()['patch']
        embed = discord.Embed(
            url=link,
            title=f'Rivals of Aether Academy Frame Data - Updated for {patch}',
            description='Data extracted manually in-game and from dev-mode files by SNC. '
                        'Extra information provided by Menace13 and Youngblood. ')
        embed.set_thumbnail(url='https://i.imgur.com/nMS0QPT.png')
        await interaction.response.send_message(content=link, embed=embed)

    @app_commands.command(name='igl')
    async def igl_google_docs(self, interaction: discord.Interaction):
        """IGL's list of informational graphics, data, and tools"""
        link = 'https://drive.google.com/drive/folders/1krAYYBW4Q8UYrNMXJ7C6T-85w0HCVJiJ'
        embed = discord.Embed(
            url=link,
            title='IGL\'s Lab',
            description='Informational graphics, data, and tools by IGL.')
        embed.set_thumbnail(url='https://i.imgur.com/nN6DAmT.png')
        await interaction.response.send_message(content=link, embed=embed)

    @app_commands.command(name='patchnotes')
    async def patch_notes_doc(self, interaction: discord.Interaction):
        """SNC's collated list of patch notes and undocumented changes"""
        link = ('https://docs.google.com/spreadsheets/d/'
                '1MNe3jg64nzKxAg0Ts8vM0PyMZFoD6Nhc2YPbhOIHzyY')
        embed = discord.Embed(
            url=link,
            title='Rivals of Aether Patch Notes',
            description='Collated by SNC, a list of all of the existing patch notes and '
                        'undocumented changes since day 1 of early access, split into '
                        'separate changes for each character.')
        embed.set_thumbnail(url='https://imgur.com/WtU3xBU.png')
        await interaction.response.send_message(content=link, embed=embed)
    
    # Rivals Data
    @app_commands.command(name='parry')
    async def dodge_data(self, interaction: discord.Interaction):
        """Universal parry, roll, and airdodge frame data"""
        link = 'https://rivals.academy/library/glossary/#dodges'
        embed = discord.Embed(description=
            # Parry
            ('**Parry** ```ml\n'
            'Startup      | 2    \n'
            'Invulnerable | 3-10 \n'
            'Endlag       | 20   \n'
            'FAF          | 31   \n'
            'Cooldown     | 20   \n'
            'successfully parrying removes your ability to parry/roll for 30 frames.```'
            # Roll
            '\n**Roll** ```ml\n'
            'Startup      | 4    \n'
            'Invulnerable | 5-19 \n'
            'Endlag       | 12   \n'
            'FAF          | 31```'
            # Airdodge
            '\n**Airdodge** ```ml\n'
            'Startup      | 2    \n'
            'Invulnerable | 3-15 \n'
            'Endlag       | 12   \n'
            'FAF          | 27```'))
        embed.set_author(name='Universal Dodge Frame Data')
        await interaction.response.send_message(content=link, embed=embed)

    @app_commands.command(name='formulas')
    async def formulas_kb_hs_hp(self, interaction: discord.Interaction):
        """Rivals' knockback, hitstun, and hitpause formulas"""
        link = 'https://rivals.academy/library/glossary/#knockback'
        embed = discord.Embed(description=
            # Knockback
            ('**Knockback** ```ml\n'
             'BKB + (KB_Scaling × Percent_After_Hit × KB_Adj × 0.12)```'
            # Hitstun
            '\n**Hitstun** ```ml\n'
             'Hitstun_Multiplier × ((BKB × (KB_Adj × 2.4 + 1.6)) + '
             '(KB_Scaling × Percent_After_Hit × KB_Adj × 0.312))```'
            # Hitpause
            '\n**Hitpause** ```ml\n'
             'Base_Hitpause + (Hitpause_Scaling × Percent_After_Hit × 0.05) + Extra_Hitpause```'))
        embed.set_author(name='Rivals Formulas')
        await interaction.response.send_message(content=link, embed=embed)

    @app_commands.command(name='angleflippers')
    async def angle_flippers(self, interaction: discord.Interaction):
        """List of angle flipper definitions"""
        link = 'https://rivals.academy/library/glossary/#angle-flippers'
        definitions = ('```glsl\n'
            '0 - Sends at the exact knockback angle every time\n'
            '1 - Sends away from the center of the attacker or projectile\n'
            '2 - Sends toward the center of the attacker or projectile\n'
            '3 - Horizontal knockback sends away from the center of the hitbox\n'
            '4 - Horizontal knockback sends toward the center of the hitbox\n'
            '5 - Horizontal knockback is reversed\n'
            '6 - Horizontal knockback sends away from the center of the attacker or projectile\n'
            '7 - Horizontal knockback sends toward the center of the attacker or projectile\n'
            '8 - Sends away from the center of the hitbox\n'
            '9 - Sends toward the center of the hitbox\n'
            '10 - Sends in the direction the attacker is moving```')
        embed = discord.Embed(title='Angle Flipper Definitions', description=definitions)
        await interaction.response.send_message(content=link, embed=embed)
    
    @app_commands.command(name='teching')
    async def teching(self, interaction: discord.Interaction):
        """Teching frame data comparison"""
        link = 'https://rivals.academy/library/glossary/#teching'
        embed = discord.Embed(description=
            # Tech In Place
            ('**Tech In Place** ```ml\n'
            'Intangible | 1-14       \n'
            'Endlag     | 4          \n'
            'FAF        | 19```'
            # Tech Roll
            '\n**Tech Roll** ```ml\n'
            'Intangible | 1-20    \n'
            'Endlag     | 14      \n'
            'FAF        | 35```'
            # Missed (Hitstun)
            '\n**Missed (Hitstun)** ```ml\n'
            'Endlag | 13            \n'
            'FAF    | 14```'
            # Missed (Tumble)
            '\n**Missed (Tumble)** ```ml\n'
            'Endlag | 7             \n'
            'FAF    | 8```'
            # Wall Tech
            '\n**Wall Tech** ```ml\n'
            'Intangible | 1-15    \n'
            'FAF        | 12      \n'
            'Airdodge/Jump Cancellable 4-11```'
            # Ceiling Tech
            '\n**Ceiling Tech** ```ml\n'
            'Intangible | 1-15       \n'
            'FAF        | 12         \n'
            'IASA Cancellable 1-19```'))
        embed.set_author(name='Universal Teching Frame Data')
        embed.set_image(url='https://cdn.discordapp.com/attachments/'
                            '376248878334214145/1160821640221962341/'
                            'roaknockdownframedata.png')
        await interaction.response.send_message(content=link, embed=embed)

    # Misc.
    @app_commands.command(name='fpsfix')
    async def fps_fix(self, interaction: discord.Interaction):
        """60 fps fix instructions for Nvidia graphics cards"""
        link = 'https://twitter.com/darainbowcuddle/status/1410724611327631364'
        await interaction.response.send_message(link)

    @app_commands.command(name='replays')
    async def how_to_access_your_replays(self, interaction: discord.Interaction):
        """How to access your RoA replays"""
        embed = discord.Embed()
        embed.set_author(
            name='How to Access Your Replays', 
            icon_url=self.bot.user.display_avatar.url)
        embed.add_field(
            name='Method 1:',
            value='1. Press `Win + R`\n'
                  '2. Put in the following: ```%LocalAppData%\\RivalsOfAether\\replays```',
            inline=False)
        embed.add_field(
            name='Method 2:',
            value='1. Make sure "Hidden items" are shown in File Explorer\n'
                  '2. Go to: ```C:\\Users\\yourname\\AppData\\Local\\RivalsofAether\\replays```',
            inline=False)
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Info(bot))
