import discord
from discord import app_commands
from discord.ext import commands


class Meta(commands.Cog):
    """Send information about Mentorbot and Academy."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='about')
    async def info_command(self, interaction: discord.Interaction):
        """About Mentorbot"""
        embed = discord.Embed(
            description=f'{len(self.bot.guilds):,} servers, {len(self.bot.users):,} users!')
        embed.set_author(
            name='A custom Discord bot by the Rivals of Aether Academy.',
            icon_url=self.bot.user.avatar.url)
        embed.add_field(
            name='Created by blair',
            value='https://github.com/blair-c/Mentorbot3.0',
            inline=False)
        embed.add_field(
            name='Frame data info provided by SNC and Sector 7-G',
            value='https://twitter.com/SNC_Sector7G\n'
                  'https://discord.gg/qgKqaPX',
            inline=False)
        embed.add_field(
            name='Profile photo drawn by Sxolian',
            value='https://twitter.com/SxolianArt',
            inline=False)
        await interaction.response.send_message(embed=embed)

    # @app_commands.command(name='help')
    # async def help_command(self, interaction, discord.Interaction):
    #     """"""


async def setup(bot: commands.Bot):
    await bot.add_cog(Meta(bot))
