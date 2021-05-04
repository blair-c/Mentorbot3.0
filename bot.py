import os
import sys
from itertools import cycle

# Discord setup
try:
    import discord
    from discord.ext import commands, tasks
except ImportError:
    print('Discord.py is not installed', file=sys.stderr)
    sys.exit(1)

# Ensure correct Discord.py version
if discord.__version__ != '1.7.2':
    print(f'Discord.py version: {discord.__version__}.\n'
          'Please install version 1.7.2', file=sys.stderr)
    sys.exit(1)

intents = discord.Intents.default()
intents.members = True
intents.integrations = False
intents.webhooks = False
intents.invites = False
intents.voice_states = False
intents.typing = False

bot = commands.Bot(
    command_prefix='!',
    case_insensitive=True,
    intents=intents)
bot.remove_command('help')

extensions = [
    'actionlog',   # Action-log channel functionality
    'characters',  # Mentor and hitbox commands
    'info',        # Help, links, and informational commands
    'moderation',  # Moderation commands
    'roles',       # Role request commands and reaction system
]

statuses = {
    'update_note': 'Currently updating to definitive',
    'academy_link': 'discord.me/mentor',
    'usage_stats': ''  # To be updated in loop
}
index_cycle = cycle(['update_note', 'academy_link', 'usage_stats'])

@tasks.loop(seconds=10)
async def change_bot_activity():
    """Update bot's activity to display message or usage statistics."""
    index = next(index_cycle)
    if index == 'usage_stats':  # Update usage stats if necessary
        statuses['usage_stats'] = f'{len(bot.guilds):,} servers, {len(bot.users):,} users!'
    status = statuses[index]
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
