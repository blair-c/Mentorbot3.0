import discord
from discord.ext import commands

from helpers import helpers


class HelpInfo(commands.Cog):
    """Help and info commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='info', aliases=['information', 'about'], hidden=True)
    @helpers.in_channel('bot-stuff')
    async def info_command(self, ctx):
        """Display information about Mentorbot."""
        embed = discord.Embed()
        embed.set_author(name='About Mentorbot 3.0', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name='help', aliases=['commands'], hidden=True)
    @helpers.in_channel('bot-stuff')
    async def help_command(self, ctx, *arg):
        """Display information and command syntax for public commands."""
        embed = discord.Embed()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HelpInfo(bot))
