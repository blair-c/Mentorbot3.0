import discord
from discord.ext import commands

from bot import extensions


class Owner(commands.Cog):
    """Load, unload, and reload cogs; or logout bot."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def load_cog(self, ctx, *, cog: str):
        """Load given cog."""
        cog = cog.replace(' ', '')
        embed = discord.Embed()
        try:
            self.bot.load_extension(f'cogs.{cog}') # Dot path to cogs subdirectory
            embed.set_author(name=f'Loaded {cog} cog.')
        except Exception as e:
            embed.add_field(name=f'Could not load "{cog}" cog.',
                            value=f'{type(e).__name__}: {e}')
        await ctx.send(embed=embed)

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def unload_cog(self, ctx, *, cog: str):
        """Unload given cog."""
        cog = cog.replace(' ', '')
        embed = discord.Embed()
        try:
            self.bot.unload_extension(f'cogs.{cog}') # Dot path to cogs subdirectory
            embed.set_author(name=f'Unoaded {cog} cog.')
        except Exception as e:
            embed.add_field(name=f'Could not unload "{cog}" cog.',
                            value=f'{type(e).__name__}: {e}')
        await ctx.send(embed=embed)

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def reload_cog(self, ctx, *, cog: str):
        """Reload given cog."""
        cog = cog.replace(' ', '')
        embed = discord.Embed()
        try:
            self.bot.unload_extension(f'cogs.{cog}') # Dot path to cogs subdirectory
            self.bot.load_extension(f'cogs.{cog}')
            embed.set_author(name=f'Reloaded {cog} cog.')
        except Exception as e:
            embed.add_field(name=f'"{cog}" cog could not be reloaded.',
                            value=f'{type(e).__name__}: {e}')
        await ctx.send(embed=embed)

    @commands.command(name='restart', hidden=True)
    @commands.is_owner()
    async def reload_cogs(self, ctx):
        """Reload all cogs in startup extensions."""
        embed = discord.Embed()
        embed.set_author(name='Restarting...')
        await ctx.send(embed=embed)
        for cog in extensions:
            try:
                self.bot.unload_extension(f'cogs.{cog}') # Dot path to cogs subdirectory
                self.bot.load_extension(f'cogs.{cog}')
            except Exception as e:
                embed.set_author(name='Restart failed.')
                embed.add_field(name=f'"{cog}" cog could not be reloaded.',
                                value=f'{type(e).__name__}: {e}')
                await ctx.send(embed=embed)
                return
        # Success
        embed.set_author(name='Restarted successfully.')
        await ctx.send(embed=embed)

    @commands.command(name='logout', hidden=True)
    @commands.is_owner()
    async def logout(self, ctx):
        """Log Mentorbot out of Discord."""
        embed = discord.Embed()
        embed.set_author(name='Logging out.')
        await ctx.send(embed=embed)
        await self.bot.logout()


def setup(bot):
    bot.add_cog(Owner(bot))
