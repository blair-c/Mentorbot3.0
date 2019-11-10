import os
import sys

try:
    import discord
    from discord.ext import commands, tasks
except ImportError:
    print('Discord.py is not installed', file=sys.stderr)
    sys.exit(1)

# Ensure correct Discord.py version
if discord.__version__ != '1.2.4':
    print(f'Discord.py version: {discord.__version__}.\n'
          'Please install version 1.2.4', file=sys.stderr)
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

@tasks.loop(seconds=10)
async def change_bot_activity():
    """Change bot's activity to show usage statistics."""
    stats = f'{len(bot.guilds)} servers | {len(bot.users)} users'
    activity = discord.Activity(
        name=stats,
        url='https://github.com/blair-c/Mentorbot3.0',
        state=':jackie:',
        details=stats)
    await bot.change_presence(activity=activity)

@bot.event
async def on_ready():
    """Change bot activity, and display bot info when fully prepared."""
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
