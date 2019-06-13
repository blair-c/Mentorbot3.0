import os
import sys

try:
    import discord
    from discord.ext import commands
except ImportError:
    print('Discord.py is not installed', file=sys.stderr)
    sys.exit(1)

# Ensure correct Discord.py version
if discord.__version__ != '1.2.2':
    print(f'Discord.py version: {discord.__version__}.\n'
          'Please install version 1.2.2', file=sys.stderr)
    sys.exit(1)

bot = commands.Bot(
    command_prefix='!',
    description='A Discord bot for the Rivals of Aether Academy.',
    case_insensitive=True)
bot.remove_command('help')

extensions = [
    'actionlog',   # Action-log channel functionality
    'characters',  # Mentor and hitbox commands
    'helpinfo',    # Help and info commands
    'links',       # Links and informational commands
    'moderation',  # Moderation commands
    'owner',       # Bot upkeep commands
    'roles',       # Role request commands and reaction system
]

@bot.event
async def on_ready():
    """Display bot info when bot is fully prepared."""
    print(f'Logged in as {bot.user.name}\nUser ID: {bot.user.id}')

@bot.check
async def globally_block_dms(ctx):
    """Global check to block DMs."""
    return ctx.guild is not None

if __name__ == '__main__':
    for cog in extensions:
        try:
            bot.load_extension(f'cogs.{cog}') # Dot path to cogs subdirectory
            print(f'Loaded {cog} cog...')
        except Exception as e:
            print(f'Failed to load {cog} cog.\n'
                  f'[{type(e).__name__}: {e}]', file=sys.stderr)
            sys.exit(1)
    print('Logging in...')
    bot.run(os.environ.get('TOKEN')) # API Key from environment
