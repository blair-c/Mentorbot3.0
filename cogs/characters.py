import sqlite3

import discord
from discord.ext import commands

from data import rivals
from helpers import hitboxes, mentors

db = sqlite3.connect('data/academy.db')
db.row_factory = sqlite3.Row
cursor = db.cursor()


class Characters(commands.Cog):
    """Display mentors or hitbox information for characters and regions."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='mentors')
    async def all_mentors(self, ctx):
        """List available mentor commands for characters and regions."""
        embed = discord.Embed()
        embed.set_author(name='Hello!', icon_url=ctx.guild.icon_url)
        char_commands = [f'{emote} For {character}, type **!{character.lower()}**'
                        for character, emote in rivals.characters.items()]
        embed.add_field(
            name="Please choose the character you'd like to be mentored in:",
            value='\n'.join(char_commands))
        embed.add_field(
            name='If you live in Europe, try this command:',
            value='<:MentorsEurope:547189291969937420> For Europe, type **!EU**')
        await ctx.send(embed=embed)

    # Region-based mentor commands
    @commands.command(name='EU')
    async def eu_mentors(self, ctx):
        """Display all EU mentors, trial mentors, and advisors."""
        await mentors.mentor_info(ctx, cursor, r='EU')

    # Character commands - mentors and hitboxes
    async def character_command(self, ctx, character, *move):
        """Display mentor info for character, or return hitbox info for move."""
        if not move: # No args passed, display mentor info
            await mentors.mentor_info(ctx, cursor, c=character)
        else: # Arg(s) passed, display move info
            await hitboxes.move_info(ctx, cursor, character, *move)

    @commands.command(name='zetterburn', aliases=['zetter', 'zet'])
    async def zetterburn(self, ctx, *move):
        """Display Zetterburn mentors, or display info of move given."""
        await self.character_command(ctx, 'Zetterburn', *move)

    @commands.command(name='forsburn', aliases=['fors'])
    @commands.guild_only()
    async def forsburn(self, ctx, *move):
        """Display Forsburn mentors, or display info of move given."""
        await self.character_command(ctx, 'Forsburn', *move)

    @commands.command(name='clairen')
    async def clairen(self, ctx, *move):
        """Display Clairen mentors, or display info of move given."""
        await self.character_command(ctx, 'Clairen', *move)

    @commands.command(name='orcane', aliases=['orca'])
    async def orcane(self, ctx, *move):
        """Display Orcane mentors, or display info of move given."""
        await self.character_command(ctx, 'Orcane', *move)

    @commands.command(name='etalus', aliases=['eta'])
    async def etalus(self, ctx, *move):
        """Display Etalus mentors, or display info of move given."""
        await self.character_command(ctx, 'Etalus', *move)

    @commands.command(name='ranno')
    async def ranno(self, ctx, *move):
        """Display Ranno mentors, or display info of move given."""
        await self.character_command(ctx, 'Ranno', *move)

    @commands.command(name='kragg')
    async def kragg(self, ctx, *move):
        """Display Kragg mentors, or display info of move given."""
        await self.character_command(ctx, 'Kragg', *move)

    @commands.command(name='maypul')
    async def maypul(self, ctx, *move):
        """Display Maypul mentors, or display info of move given."""
        await self.character_command(ctx, 'Maypul', *move)

    @commands.command(name='sylvanos', aliases=['sylv'])
    async def sylvanos(self, ctx, *move):
        """Display Sylvanos mentors, or display info of move given."""
        await self.character_command(ctx, 'Sylvanos', *move)

    @commands.command(name='wrastor')
    async def wrastor(self, ctx, *move):
        """Display Wrastor mentors, or display info of move given."""
        await self.character_command(ctx, 'Wrastor', *move)

    @commands.command(name='absa')
    async def absa(self, ctx, *move):
        """Display Absa mentors, or display info of move given."""
        await self.character_command(ctx, 'Absa', *move)

    @commands.command(name='elliana', aliases=['elli'])
    async def elliana(self, ctx, *move):
        """Display Elliana mentors, or display info of move given."""
        await self.character_command(ctx, 'Elliana', *move)

    @commands.command(name='ori')
    async def ori(self, ctx, *move):
        """Display Ori mentors, or display info of move given."""
        await self.character_command(ctx, 'Ori', *move)

    @commands.command(name='shovelknight', aliases=['shovel-knight', 'shovel', 'sk'])
    async def shovelknight(self, ctx, *move):
        """Display Shovel Knight mentors, or display info of move given."""
        if not move:
            await self.character_command(ctx, 'Shovel Knight', *move)
        # Allow for '!shovel knight [move]' syntax
        elif move[0].lower() == 'knight':
            await self.character_command(ctx, 'Shovel Knight', *move[1:])
        else:
            await self.character_command(ctx, 'Shovel Knight', *move)

def setup(bot):
    bot.add_cog(Characters(bot))
