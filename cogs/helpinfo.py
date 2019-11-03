import discord
from discord.ext import commands

from helpers import helpers


class HelpInfo(commands.Cog):
    """Help and info commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='info', aliases=['information', 'about'], hidden=True)
    async def info_command(self, ctx):
        """Display information about Mentorbot."""
        embed = discord.Embed(
            description='A custom Discord bot for the Rivals of Aether Academy.')
        embed.set_author(name='About Mentorbot 3.0', icon_url=self.bot.user.avatar_url)
        embed.add_field(
            name='<:yesdefinitely:609053319415201793> Created by yesdefinitely', 
            value='<:twitter:609120999744733204> https://twitter.com/ydefinitely\n'
                  '<:github:609120967280689161> https://github.com/blair-c/Mentorbot3.0', 
            inline=False)
        embed.add_field(
            name='<:SNC:609053198736424960> Frame data info provided by SNC and Sector 7-G', 
            value='<:twitter:609120999744733204> https://twitter.com/SNC_Sector7G\n'
                  '<:discord:609120982543630336> https://discord.gg/qgKqaPX',
            inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='help', aliases=['syntax'], hidden=True)
    async def help_command(self, ctx, *arg):
        """Display information and command syntax for hitbox commands."""
        embed = discord.Embed()
        embed.set_author(name='Hitbox Command Syntax', icon_url=self.bot.user.avatar_url)
        embed.add_field(
            name='`![character] [move]`',
            value='Multiple character and move names are supported, try it out!')
        embed.set_image(url='https://i.imgur.com/iiLINcV.png')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HelpInfo(bot))
