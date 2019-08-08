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
        embed = discord.Embed(description='A custom Discord bot for the Rivals of Aether Academy.')
        embed.set_author(
            name='About Mentorbot 3.0', 
            icon_url=self.bot.user.avatar_url)
        embed.add_field(
            name='<:yesdefinitely:609053319415201793> Created by yesdefinitely', 
            value='<:twitter:609049225560457216> https://twitter.com/ydefinitely\n'
                  '<:github:609047166417109005> https://github.com/blair-c/Mentorbot3.0', 
            inline=False)
        embed.add_field(
            name='<:SNC:609053198736424960> Frame data info provided by SNC and Sector 7-G', 
            value='<:twitter:609049225560457216> https://twitter.com/SNC_Sector7G\n'
                  '<:discord:609047933685465178> https://discord.gg/qgKqaPX',
            inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='help', aliases=['commands'], hidden=True)
    @helpers.in_channel('bot-stuff')
    async def help_command(self, ctx, *arg):
        """Display information and command syntax for public commands."""
        embed = discord.Embed()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HelpInfo(bot))
