import os
import sys
from itertools import cycle
from typing import Literal

try:
    import discord
    from discord.ext import commands, tasks
except ImportError:
    print('Discord.py is not installed', file=sys.stderr)
    sys.exit(1)

correct_ver = '2.0.1'
if discord.__version__ != correct_ver:
    print(f'Discord.py version: {discord.__version__}.\n'
          f'Please install version {correct_ver}', file=sys.stderr)
    sys.exit(1)


class MyBot(commands.Bot):

    def __init__(self, *, intents: discord.Intents):
        super().__init__(command_prefix=commands.when_mentioned, intents=intents)
    
    async def setup_hook(self):
        cogs = [
            'actionlog',  # (Limited functionality with update)
            'hitboxes',  # Frame data and hitbox commands
            'info',      # Links and informational commands
            'mentors',   # Mentor list and management commands
            'meta',      # About, help, and misc. commands
            'roles',     # Roles channel setup and functionality
        ]
        for cog in cogs:
            await self.load_extension(f'cogs.{cog}')
            print(f'Loaded {cog} cog...')


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

# Start
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('discord.me/mentor'))
    print(f'Logged in as {bot.user}\nUser ID: {bot.user.id}\n'
          f'{len(bot.guilds):,} guilds / {len(bot.users):,} users')

if __name__ == '__main__':
    bot.run(os.getenv('TOKEN'))  # API Key from environment
