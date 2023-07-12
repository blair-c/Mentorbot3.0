import os
import sys
from typing import Literal

import box
import discord
from discord.ext import commands
import tabulate

print(f'Python {sys.version}\n'
      f'discord.py {discord.__version__} | '
      f'python-box {box.__version__} | '
      f'tabulate {tabulate.__version__}')


class MyBot(commands.Bot):

    def __init__(self, *, intents: discord.Intents):
        super().__init__(command_prefix=commands.when_mentioned, intents=intents)
    
    async def setup_hook(self):
        cogs = [
            'hitboxes',  # Frame data and hitbox commands
            'info',      # Links, info, and utility commands
            'mentors',   # Mentor list and management commands
            'roles',     # Roles channel setup and functionality
        ]
        for cog in cogs:
            await self.load_extension(f'cogs.{cog}')
            print(f'Loaded {cog} cog...')
        print(f'Logged in as {bot.user}\nUser ID: {bot.user.id}')


intents = discord.Intents.default()
intents.members = True
bot = MyBot(intents=intents)
bot.remove_command('help')

@bot.command()
@commands.guild_only()
@commands.is_owner()
async def sync(ctx: commands.Context, scope: Literal['global', 'guild']):
    """Sync global or guild commands"""
    async with ctx.channel.typing():
        if scope == 'global':
            synced = await ctx.bot.tree.sync()
            txt = 'globally'
        elif scope == 'guild':
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
            txt = 'to the current guild'
    await ctx.send(f'Synced {len(synced)} commands {txt}')

if __name__ == '__main__':
    bot.run(os.getenv('TOKEN'))  # API Key from environment
