import discord
from discord.ext import commands


class Links(commands.Cog):
    """Send informational Rivals links."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='AAAA', aliases=['dropdashing', 'dropdash'])
    async def aaaa_dashing_link(self, ctx):
        """Link to clip of the 'AAAA dashing' advanced technique."""
        link = ('https://gifsound.com/?'
                'gfycat=ApprehensiveConventionalFrilledlizard&v=kyUtGNIFx5c&s=7')
        embed = discord.Embed(
            url=link, title='AAAA Dashing', description='Also known as dropdashing.')
        embed.set_thumbnail(
            url='https://thumbs.gfycat.com/'
                'ApprehensiveConventionalFrilledlizard-size_restricted.gif')
        await ctx.send(content=link, embed=embed)

    @commands.command(name='babydashing', aliases=['babydash'])
    async def babydashing_link(self, ctx):
        """Link to video covering the 'babydashing' advanced technique."""
        await ctx.send('https://www.youtube.com/watch?v=BW1M8zx_KGM')

    @commands.command(name='bairhitfall', aliases=['bair-hitfall'])
    async def bair_hitfall_tutorial(self, ctx):
        """Link to clip of and instructions for the 'hitfalling' tutorial."""
        await ctx.send('TODO')

    @commands.command(name='knockback-formula', aliases=['knockbackformula', 'knockback', 'kb'])
    async def formula_knockback(self, ctx, *formula):
        """Send display of Rivals' knockback formula."""
        formula = ('```ml\n'
                   'BKB + Damage * Knockback_Scaling * 0.12 * Knockback_Adj```')
        embed = discord.Embed(title='Knockback Formula', description=formula)
        await ctx.send(embed=embed)

    @commands.command(name='hitpause-formula', aliases=['hitpauseformula', 'hitpause'])
    async def formula_hitpause(self, ctx, *formula):
        """Send display of Rivals' hitpause formula."""
        formula = ('```ml\n'
                   'Base_Hitpause + Damage * Hitpause_scaling * .05```')
        embed = discord.Embed(title='Hitpause Formula', description=formula)
        await ctx.send(embed=embed)

    @commands.command(name='hitstun-formula', aliases=['hitstunformula', 'hitstun'])
    async def formula_hitstun(self, ctx, *formula):
        """Send display of Rivals' hitstun formula."""
        formula = ('```ml\n'
                   'BKB * 4 * ((Knockback_Adj - 1) * 0.6 + 1) + Damage * '
                   '0.12 * Knockback_scaling * 4 * 0.65 * Knockback_Adj```')
        embed = discord.Embed(title='Hitstun Formula', description=formula)
        await ctx.send(embed=embed)

    @commands.command(name='frame-data', aliases=['framedata'])
    async def frame_data_doc(self, ctx):
        """Link to SNC's frame data document."""
        link = ('https://docs.google.com/spreadsheets/d/'
                '19UtK7xG2c-ehxdlhCFKMpM4_IHSG-EXFgXLJaunE79I')
        embed = discord.Embed(
            url=link,
            title='Rivals of Aether Academy Frame Data - Updated for 1.4.8',
            description='Data extracted manually in-game and from dev-mode files by SNC. '
                        'Extra information provided by Menace13 and Youngblood. '
                        'General Stats created by Kisuno. '
                        'Frame Data App lead by Smiles1990.')
        embed.set_thumbnail(url='https://i.imgur.com/2Cyfccy.png')
        await ctx.send(content=link, embed=embed)

    @commands.command(name='golden-guides', aliases=['goldenguides'])
    async def goldenguides_complete_collection(self, ctx):
        """Link to "Complete Collection" of Golden Guides Reddit post."""
        await ctx.send('https://www.reddit.com/r/RivalsOfAether/comments/9v6pw4/')

    @commands.command(name='the-basics', aliases=['thebasics', 'basics'])
    async def goldenguide_basics(self, ctx):
        """Link to Golden Elite's beginner's guide."""
        link = ('https://docs.google.com/document/d/'
                '1232jAesA_q1tRch-jer7rYYxWWn3K8BXVmhX75Tmnyw')
        embed = discord.Embed(
            url=link,
            title='Golden Guides: The Basics',
            description='Beginner\'s guide featuring a complete tech list '
                        'and a large amount of technical definitions.')
        embed.set_thumbnail(url='https://i.imgur.com/tXcwyJR.png')
        await ctx.send(content=link, embed=embed)

    @commands.command(name='every-tech', aliases=['everytech'])
    async def goldenguide_everytech(self, ctx):
        """Link to Golden Elite's write-up of every tech in Rivals."""
        link = ('https://docs.google.com/document/d/'
                '1R10JBGY3633U3Ja1voqvNwV8YS5-XI1HbjyXmV592uA')
        embed = discord.Embed(
            url=link,
            title='Golden Guides: Every Tech',
            description='Comprehensive list of every advanced technique in the game.')
        embed.set_thumbnail(url='https://i.imgur.com/BKyW9u5.png?1')
        await ctx.send(content=link, embed=embed)

    @commands.command(name='survival-di', aliases=['survivaldi', 'di'])
    async def goldenguide_survivaldi(self, ctx):
        """Link to Golden Elite's Survival DI guide."""
        link = ('https://docs.google.com/document/d/'
                '1Q7b0bLYcATnwlakuB_HtS2Mx2Jl3rf2YQlVX5RQJIeU')
        embed = discord.Embed(
            url=link,
            title='Golden Guides: Survival DI',
            description='How to DI the killing blows of each character.')
        embed.set_thumbnail(url='https://i.imgur.com/Po4u4Wp.png')
        await ctx.send(content=link, embed=embed)

    @commands.command(name='tech-chasing', aliases=['techchasing'])
    async def goldenguide_techchasing(self, ctx):
        """Link to Golden Elite's tech chasing guide."""
        link = ('https://docs.google.com/document/d/'
                '1e0japzRqVI5VvnwzZ5uijL4nkOrRrOSaQ_qlyU6Bww0')
        embed = discord.Embed(
            url=link,
            title='Golden Guides: Tech Chasing',
            description='The overall thought process, priority list, '
                        'and tech chasing options for each character.')
        embed.set_thumbnail(url='https://i.imgur.com/WRxAYTN.png')
        await ctx.send(content=link, embed=embed)

    @commands.command(name='mindset', aliases=['jackie'])
    async def mindset_screenshot(self, ctx):
        """Send screenshot of Jackie Chan mindset post."""
        jackie = '<:jackie:547193437229940746>'
        await ctx.send(f'{jackie} https://i.imgur.com/jDnEAOz.jpg {jackie}')

    @commands.command(name='patch-notes', aliases=['patchnotes'])
    async def patch_notes(self, ctx):
        """Link to SNC's collated list of patch notes and undocumented changes."""
        link = ('https://docs.google.com/spreadsheets/d/'
                '1MNe3jg64nzKxAg0Ts8vM0PyMZFoD6Nhc2YPbhOIHzyY')
        embed = discord.Embed(
            url=link,
            title='Rivals of Aether Patch Notes',
            description='Collated by SNC, a list of all of the existing patch notes and '
                        'undocumented changes since day 1 of early access, split into '
                        'separate changes for each character.')
        embed.set_thumbnail(url='https://imgur.com/WtU3xBU.png')
        await ctx.send(content=link, embed=embed)

    @commands.command(name='smashvods', aliases=['vods'])
    async def smashvods_link(self, ctx):
        """Link to Rivals of Aether section of SmashVods website."""
        link = 'http://smashvods.com/roa'
        embed = discord.Embed(url=link, title='SmashVods',
                              description='Search for RoA VODs by player or matchup.')
        await ctx.send(content=link, embed=embed)


def setup(bot):
    bot.add_cog(Links(bot))
