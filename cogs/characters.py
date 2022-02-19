import sqlite3
from time import sleep

import discord
from discord.ext import commands

from data import rivals
from helpers import helpers, hitboxes, mentors

db = sqlite3.connect('data/academy.db')
db.row_factory = sqlite3.Row
cursor = db.cursor()


class Characters(commands.Cog):
    """Display mentors or hitbox information for characters and regions."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='mentors')
    @helpers.in_academy()
    async def all_mentors(self, ctx):
        """List available mentor commands for characters and regions."""
        embed = discord.Embed()
        embed.set_author(name='Hello!', icon_url=ctx.guild.icon_url)
        char_commands = [f'{info["emote"]} → **!{character.lower()}**'
                        for character, info in rivals.characters.items()]
        embed.add_field(
            name="Please choose the character you'd like to be mentored in:",
            value='\n'.join(char_commands),
            inline=False)
        embed.add_field(
            name='If you live in Europe, try this command:',
            value='<:MentorsEurope:547189291969937420> **!EU**',
            inline=False)
        await ctx.send(embed=embed)

    # Region-based mentor commands
    @commands.command(name='EU', aliases=['europe'])
    @helpers.in_academy()
    async def eu_mentors(self, ctx):
        """Display all EU mentors, trial mentors, and advisors."""
        await mentors.mentor_info(ctx, region='Europe')

    # Console-based mentor commands
    @commands.command(name='switch')
    @helpers.in_academy()
    async def switch_mentors(self, ctx):
        """Display all Nintendo Switch mentors, trial mentors, and advisors."""
        await mentors.mentor_info(ctx, console='Switch')
    
    @commands.command(name='xbox')
    @helpers.in_academy()
    async def xbox_mentors(self, ctx):
        """Display all Xbox mentors, trial mentors, and advisors."""
        await mentors.mentor_info(ctx, console='Xbox')
    
    @commands.command(name='keyboard')
    @helpers.in_academy()
    async def keyboard_mentors(self, ctx):
        """Display all Keyboard mentors, trial mentors, and advisors."""
        await mentors.mentor_info(ctx, console='Keyboard')

    # Character commands - mentors and hitboxes
    async def character_command(self, ctx, character, move):
        """Display mentor info for character, or return hitbox info for move."""
        sleep(0.1)  # Delay to avoid bot message appearing before command message
        if not move:  # No args passed, display mentor info in Academy, hurtbox info elsewhere
            ACADEMY_ID = 252352512332529664
            TEST_SERVER_ID = 475599187812155392
            if ctx.guild.id not in [ACADEMY_ID, TEST_SERVER_ID]:
                await hitboxes.move_info(ctx, cursor, character, 'hurtbox')
            elif ctx.channel.name == 'ask-a-mentor':
                embed = discord.Embed(
                    color=0xef5350,
                    description='Mentor commands are not usable in this channel')
                error = await ctx.send(embed=embed)  # Send error message
                sleep(5)
                await ctx.message.delete()  # Delete message of command
                await error.delete()  # Delete error message
            else:  # Mentor command
                await mentors.mentor_info(ctx, character=character)
        else:  # Arg(s) passed, display move info
            await hitboxes.move_info(ctx, cursor, character, move)

    # New WS pack
    @commands.command(name='workshop', aliases=['mollo', 'hodan', 'olympia', 'oly', 'pomme'])
    async def ws_pack(self, ctx, *move):
        """Send notice that Mentorbot isn't updated with the new characters."""
        move = move
        link = ('https://docs.google.com/spreadsheets/d/'
                '19UtK7xG2c-ehxdlhCFKMpM4_IHSG-EXFgXLJaunE79I')
        embed = discord.Embed(
            url=link,
            title='Rivals of Aether Academy Frame Data - Updated for 2.0.8.0',
            description='For up to date frame data info, see the RoAA !framedata document '
                        'linked here.')
        embed.set_author(name='Mentorbot is not updated!', icon_url=self.bot.user.avatar_url)
        embed.set_thumbnail(url='https://i.imgur.com/lwrMohK.png')
        await ctx.send(embed=embed)

    @commands.command(name='zetterburn', aliases=['zetter', 'zet'])
    async def zetterburn(self, ctx, *move):
        """Display Zetterburn mentors, or display info of move given."""
        move = ''.join(move).lower().replace('-', '')
        # Alternate move names
        if move == 'shine':
            move = 'nspecial'
        elif move == 'fireball':
            move = 'fspecial'
        elif move == 'firefox':
            move = 'uspecial'
        await self.character_command(ctx, 'Zetterburn', move)

    @commands.command(name='forsburn', aliases=['fors'])
    async def forsburn(self, ctx, *move):
        """Display Forsburn mentors, or display info of move given."""
        move = ''.join(move).lower().replace('-', '')
        # Alternate move names
        if move in ['cape', 'fcape', 'forwardcape']:
            move = 'fstrong'
        elif move in ['ucape', 'upcape']:
            move = 'ustrong'
        elif move == 'smoke':
            move = 'nspecial'
        elif move in ['clone', 'superclone']:
            move = 'fspecial'
        elif move == 'teleport':
            move = 'uspecial'
        elif move in ['combust', 'inhale', 'cloneattack']:
            move = 'dspecial'
        await self.character_command(ctx, 'Forsburn', move)

    @commands.command(name='clairen')
    async def clairen(self, ctx, *move):
        """Display Clairen mentors, or display info of move given."""
        move = ''.join(move).lower().replace('-', '')
        # Alternate move names
        if move == 'grab':
            move = 'nspecial'
        elif move in ['counter', 'forcefield', 'plasmafield', 'nofunzone']:
            move = 'dspecial'
        await self.character_command(ctx, 'Clairen', move)

    @commands.command(name='orcane', aliases=['orc', 'orca'])
    async def orcane(self, ctx, *move):
        """Display Orcane mentors, or display info of move given."""
        move = ''.join(move).lower().replace('-', '')
        # Alternate move names
        if move == 'bubblebutt':
            move = 'fair'
        elif move in ['droplet', 'puddle', 'puddleshot']:
            move = 'nspecial'
        elif move in['orcahop', 'teleport']:
            move = 'uspecial'
        elif move == 'bubbles':
            move = 'dspecial'
        await self.character_command(ctx, 'Orcane', move)

    @commands.command(name='etalus', aliases=['eta'])
    async def etalus(self, ctx, *move):
        """Display Etalus mentors, or display info of move given."""
        move = ''.join(move).lower().replace('-', '')
        # Alternate move names
        if move == 'slide':
            move = 'dashattack'
        elif move in ['hammer', 'armor', 'armour']:
            move = 'nspecial'
        elif move in ['icicle', 'icicles']:
            move = 'fspecial'
        elif move == 'freeze':
            move = 'dspecial'
        await self.character_command(ctx, 'Etalus', move)

    @commands.command(name='ranno')
    async def ranno(self, ctx, *move):
        """Display Ranno mentors, or display info of move given."""
        move = ''.join(move).lower().replace('-', '')
        # Alternate move names
        if move in ['needles', 'darts', 'needle']:
            move = 'nspecial'
        elif move == 'tongue':
            move = 'fspecial'
        elif move in ['divekick', 'needlestorm', 'poisonspin', 'whirlydirly']:
            move = 'uspecial'
        elif move == 'bubble':
            move = 'dspecial'
        await self.character_command(ctx, 'Ranno', move)

    @commands.command(name='kragg')
    async def kragg(self, ctx, *move):
        """Display Kragg mentors, or display info of move given."""
        move = ''.join(move).lower().replace('-', '')
        # Alternate move names
        if move == 'combos':  # lol
            move = 'fair'
        elif move in ['rock', 'block', 'rockshine']:
            move = 'nspecial'
        elif move == 'rollout':
            move = 'fspecial'
        elif move == 'pillar':
            move = 'uspecial'
        elif move == 'spikes':
            move = 'dspecial'
        await self.character_command(ctx, 'Kragg', move)

    @commands.command(name='maypul')
    async def maypul(self, ctx, *move):
        """Display Maypul mentors, or display info of move given."""
        move = ''.join(move).lower().replace('-', '')
        # Alternate move names
        if move == 'helicopter':
            move = 'uair'
        elif move == 'root':
            move = 'dair'
        elif move in ['seed', 'nut']:
            move = 'nspecial'
        elif move in ['uppercut', 'tether']:
            move = 'uspecial'
        elif move == 'lily':
            move = 'dspecial'
        await self.character_command(ctx, 'Maypul', move)

    @commands.command(name='sylvanos', aliases=['sylv'])
    async def sylvanos(self, ctx, *move):
        """Display Sylvanos mentors, or display info of move given."""
        move = ''.join(move).lower().replace('-', '')
        # Alternate move names
        if move in ['petalwave', 'wave', 'jabjabspecial', 'jabspecial']:
            move == 'jab'
        elif move in ['seed', 'flower']:
            move = 'nspecial'
        elif move == 'beastdash':
            move = 'fspecial'
        elif move == 'burrow':
            move = 'uspecial'
        elif move == 'howl':
            move = 'dspecial'
        await self.character_command(ctx, 'Sylvanos', move)

    @commands.command(name='wrastor')
    async def wrastor(self, ctx, *move):
        """Display Wrastor mentors, or display info of move given."""
        move = ''.join(move).lower().replace('-', '')
        # Alternate move names
        if move in ['clap', 'fclap', 'forwardclap']:
            move = 'fstrong'
        elif move in ['uclap', 'upclap']:
            move = 'ustrong'
        elif move in ['tornado', 'nado']:
            move = 'nspecial'
        elif move == 'slipstream':
            move = 'fspecial'
        await self.character_command(ctx, 'Wrastor', move)

    @commands.command(name='absa')
    async def absa(self, ctx, *move):
        """Display Absa mentors, or display info of move given."""
        move = ''.join(move).lower().replace('-', '')
        # Alternate move names
        if move in ['cloud', 'thunderline', 'cloudpop', 'cloudhop']:
            move = 'nspecial'
        elif move == 'quickattack':
            move = 'uspecial'
        elif move == 'cloudbomb':
            move = 'dspecial'
        await self.character_command(ctx, 'Absa', move)

    @commands.command(name='elliana', aliases=['elli'])
    async def elliana(self, ctx, *move):
        """Display Elliana mentors, or display info of move given."""
        move = ''.join(move).lower().replace('-', '')
        # Alternate move names
        if move in ['hook', 'claw']:
            move == 'utilt'
        elif move == 'steam':
            move = 'fstrong'
        elif move == 'fist':
            move = 'nspecial'
        elif move in ['missile', 'missiles']:
            move = 'fspecial'
        elif move in ['mech', 'eject']:
            move = 'uspecial'
        elif move == 'mine':
            move = 'dspecial'
        await self.character_command(ctx, 'Elliana', move)

    @commands.command(name='ori')
    async def ori(self, ctx, *move):
        """Display Ori mentors, or display info of move given."""
        move = ''.join(move).lower().replace('-', '')
        # Alternate move names
        if (move in ['sein', 'tap', 'seintap', 'taps', 'seintaps', 
                     'spiritflame', 'chargeflame', 'chargesein', 'seincharge']):
            move = 'nspecial'
        elif move in ['lightball', 'orb']:
            move = 'fspecial'
        elif move in ['parasol', 'parachute']:
            move = 'uspecial'
        elif move == 'bash':
            move = 'dspecial'
        await self.character_command(ctx, 'Ori', move)

    @commands.command(name='shovelknight', aliases=['shovel-knight', 'shovel', 'sk'])
    async def shovelknight(self, ctx, *move):
        """Display Shovel Knight mentors, or display info of move given."""
        if not move:
            await self.character_command(ctx, 'Shovel Knight', move)
        # Allow for '!shovel knight [move]' syntax
        if move[0].lower() == 'knight':
            move = move[1:]
        move = ''.join(move).lower().replace('-', '')
        # Alternate move names
        if move == 'dig':
            move = 'dtilt'
        elif move in ['bigdig', 'rock', 'block', 'dirtblock']:
            move = 'ustrong'
        elif move == 'coincapture':
            move = 'nspecial'
        elif move in ['infinidagger', 'propeller']:
            move = 'fspecial'
        elif move == 'anchor':
            move = 'uspecial'
        elif move in ['fishingrod', 'fish']:
            move = 'dspecial'
        elif move == 'shop':
            move = 'taunt'
        await self.character_command(ctx, 'Shovel Knight', move)


def setup(bot):
    bot.add_cog(Characters(bot))
