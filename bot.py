import os
import sys
from itertools import cycle

try:
    import discord
    from discord.ext import commands, tasks
except ImportError:
    print('Discord.py is not installed', file=sys.stderr)
    sys.exit(1)

# Ensure correct Discord.py version
if discord.__version__ != '1.2.5':
    print(f'Discord.py version: {discord.__version__}.\n'
          'Please install version 1.2.5', file=sys.stderr)
    sys.exit(1)

bot = commands.Bot(
    command_prefix='!',
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

index_cycle = cycle([0, 1])

@tasks.loop(seconds=10)
async def change_bot_activity():
    """Update bot's activity to display message or usage statistics."""
    statuses = [
        'Updated to patch 1.4.17!',
        f'{len(bot.guilds)} servers, {len(bot.users)} users!']
    status = statuses[next(index_cycle)]
    await bot.change_presence(activity=discord.Game(status))

@bot.event
async def on_ready():
    """Set bot activity, and display bot info when fully prepared."""
    change_bot_activity.start()
    print(f'Logged in as {bot.user.name}\nUser ID: {bot.user.id}')

if __name__ == '__main__':
    for cog in extensions:
        try:
            bot.load_extension(f'cogs.{cog}')  # Dot path to cogs subdirectory
            print(f'Loaded {cog} cog...')
        except Exception as e:
            print(f'Failed to load {cog} cog.\n'
                  f'[{type(e).__name__}: {e}]', file=sys.stderr)
            sys.exit(1)
    print('Logging in...')
    bot.run(os.environ.get('TOKEN'))  # API Key from environment
