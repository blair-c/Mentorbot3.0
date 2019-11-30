import discord
from discord.ext import commands


class Info(commands.Cog):
    """Send informational Rivals links and formatted displays."""

    def __init__(self, bot):
        self.bot = bot

    @comminds.command(name='commandslist', aliases=['infocommands', 'commands'])
    async def commands_list(self, ctx):
        """List all info commands.""""
        embed = discord.Embed()
        embed.set_author(name='Commands List', icon_url=self.bot.user.avatar_url)
        commands = {
            'Mentorbot':
                ['help', 'info'],
            'Rivals Data':
                ['angleflippers', 'dodgedata', 'forceflinch', 'framedata', 
                 'hitpauseformula', 'hitstunformula', 'hurtboxdata',
                 'knockbackformula', 'patchnotes'],
            'Videos & Clips':
                ['AAAA', 'babydashing', 'bairhitfall'],
            'Golden Guides':
                ['goldenguides', 'thebasics', 'everytech', 'survivaldi', 'techchasing']
        }
        for category in commands:
            commands_list = [f'`!{command}`' for command in commands[category]]
            embed.add_field(name=category, value='\n'.join(commands_list))
        await ctx.send(embed=embed)

    # Mentorbot
    @commands.command(name='help', aliases=['syntax'], hidden=True)
    async def help_command(self, ctx, *arg):
        """Display information and command syntax for hitbox commands."""
        embed = discord.Embed()
        embed.set_author(name='Hitbox Command Syntax', icon_url=self.bot.user.avatar_url)
        embed.add_field(
            name='`![character] [move]`',
            value='Multiple character and move names are supported, try it out!')
        embed.set_image(url='https://i.imgur.com/iiLINcV.png')
        embed.set_footer(text='For non-hitbox commands, try !commands.')
        await ctx.send(embed=embed)

    @commands.command(name='info', aliases=['information', 'about'], hidden=True)
    async def info_command(self, ctx):
        """Display information about Mentorbot."""
        embed = discord.Embed(
            description='A custom Discord bot by the Rivals of Aether Academy.')
        embed.set_author(name='Mentorbot 3.0', icon_url=self.bot.user.avatar_url)
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
        embed.add_field(
            name='<:Mentorbot:640465696869974017> Add Mentorbot to your own server:',
            value=('https://discordapp.com/api/oauth2/authorize?'
                   'client_id=475596740368793600&permissions=264192&scope=bot'))
        await ctx.send(embed=embed)

    # Rivals Data
    @commands.command(name='angleflippers')
    async def angle_flippers(self, ctx, *formula):
        """Send display of angle flipper definitions."""
        definitions = ('```glsl\n'
            '0 - Sends at the exact knockback_angle every time\n'
            '1 - Sends away from center of the enemy player\n'
            '2 - Sends toward center of the enemy player\n'
            '3 - Horizontal knockback sends away from the center of the hitbox\n'
            '4 - Horizontal knockback sends toward the center of the hitbox\n'
            '5 - Horizontal knockback is reversed\n'
            '6 - Horizontal knockback sends away from the enemy player\n'
            '7 - Horizontal knockback sends toward the enemy player\n'
            '8 - Sends away from the center of the hitbox\n'
            '9 - Hits toward the center of the hitbox```')
        embed = discord.Embed(title='Angle Flipper Definitions', description=definitions)
        await ctx.send(embed=embed)

    @commands.command(name='dodgedata', aliases=['dodge', 'parry', 'roll', 'airdodge'])
    async def dodge_data(self, ctx):
        """Send display of universal parry, roll, and airdodge frame data."""
        embed = discord.Embed(description=
            # Parry
            ('**Parry** ```ml\n'
             'Startup      | 2    \n'
             'Invulnerable | 3-10 \n'
             'Endlag       | 20   \n'
             'FAF          | 31   \n'
             'Cooldown     | 20   \n'
             'successfully parrying removes your ability to parry/roll for 30 frames.```'
             # Roll
             '**Roll** ```ml\n'
             'Startup      | 4    \n'
             'Invulnerable | 5-19 \n'
             'Endlag       | 12   \n'
             'FAF          | 31```'
             # Airdodge
             '**Airdodge** ```ml\n'
             'Startup      | 2    \n'
             'Invulnerable | 3-15 \n'
             'Endlag       | 12   \n'
             'FAF          | 27```'))
        embed.set_author(name='Universal Dodge Frame Data')
        await ctx.send(embed=embed)

    @commands.command(name='forceflinch')
    async def force_flinch_definitions(self, ctx, *formula):
        """Send display of force flinch definitions."""
        definitions = ('```glsl\n'
            '1 - Forces a flinch, unless the attack is crouch cancelled\n'
            '2 - Cannot cause flinch, even if crouch cancelled\n'
            '3 - Can always be crouch cancelled, regardless of percent```')
        embed = discord.Embed(title='Force Flinch Definitions', description=definitions)
        await ctx.send(embed=embed)

    @commands.command(name='framedata')
    async def frame_data_doc(self, ctx):
        """Link to SNC's frame data document."""
        link = ('https://docs.google.com/spreadsheets/d/'
                '19UtK7xG2c-ehxdlhCFKMpM4_IHSG-EXFgXLJaunE79I')
        embed = discord.Embed(
            url=link,
            title='Rivals of Aether Academy Frame Data - Updated for 1.4.15',
            description='Data extracted manually in-game and from dev-mode files by SNC. '
                        'Extra information provided by Menace13 and Youngblood. '
                        'General Stats created by Kisuno. '
                        'Collated Patch Notes created by SNC.')
        embed.set_thumbnail(url='https://i.imgur.com/ovYeevo.png')
        await ctx.send(content=link, embed=embed)

    @commands.command(name='hitpauseformula', aliases=['hitpause'])
    async def hitpause_formula(self, ctx, *formula):
        """Send display of Rivals' hitpause formula."""
        formula = ('```ml\n'
                   'Base_Hitpause + Damage * Hitpause_scaling * .05```')
        embed = discord.Embed(title='Hitpause Formula', description=formula)
        await ctx.send(embed=embed)

    @commands.command(name='hitstunformula', aliases=['hitstun'])
    async def hitstun_formula(self, ctx, *formula):
        """Send display of Rivals' hitstun formula."""
        formula = ('```ml\n'
                   'BKB * 4 * ((Knockback_Adj - 1) * 0.6 + 1) + Damage * '
                   '0.12 * Knockback_scaling * 4 * 0.65 * Knockback_Adj```')
        embed = discord.Embed(title='Hitstun Formula', description=formula)
        await ctx.send(embed=embed)

    @commands.command(name='hurtboxdata', aliases=['hurtboxes'])
    async def hurtbox_data(self, ctx):
        """Link to IGL's hurtbox measurements doc."""
        link = ('https://docs.google.com/spreadsheets/d/'
                '1jtfuDGjHXfC0UXbEyw7JOZYjB4ufZg6HbF39iNMHxbw')
        embed = discord.Embed(
            url=link,
            title='Rivals Hurtbox Sizes',
            description='Idle, crouch, and hitstun hurtbox size measurements by IGL.')
        embed.set_thumbnail(url='https://i.imgur.com/nN6DAmT.png')
        await ctx.send(content=link, embed=embed)

    @commands.command(name='knockbackformula', aliases=['knockback', 'kbformula', 'kb'])
    async def knockback_formula(self, ctx, *formula):
        """Send display of Rivals' knockback formula."""
        formula = ('```ml\n'
                   'BKB + Damage * Knockback_Scaling * 0.12 * Knockback_Adj```')
        embed = discord.Embed(title='Knockback Formula', description=formula)
        await ctx.send(embed=embed)

    @commands.command(name='patchnotes')
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

    # Videos & Clips
    @commands.command(name='AAAA', aliases=['dropdashing', 'dropdash'])
    async def aaaa_dashing(self, ctx):
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
    async def babydashing(self, ctx):
        """Link to video covering the 'babydashing' advanced technique."""
        await ctx.send('https://www.youtube.com/watch?v=BW1M8zx_KGM')

    @commands.command(name='bairhitfall')
    async def bair_hitfall_tutorial(self, ctx):
        """Link to clip of and instructions for the 'hitfalling' tutorial."""
        instructions = ('```\n'
            'Instructions:\n'
            '1. Turn away from Orby\n'
            '2. Input jump\n'
            '3. Buffer the input for back air\n'
            '4. Input fast fall (down on joystick) as soon as the back air hits\n'
            '5. Buffer input for turn around to face towards Orby\n'
            '6. Buffer inputs for up and strong attack immediately after, and '
            'continue holding up and towards Orby until the up strong begins```')
        embed = discord.Embed(description=instructions, color=0x76428a)
        embed.set_author(
            name='Bair Hitfall Ustrongs Tutorial', 
            icon_url='https://i.imgur.com/WlD8Bac.png')
        await ctx.send(embed=embed)
        # Send example Clip
        await ctx.send('https://gfycat.com/FlakyEasyAmethystgemclam')

    # Golden Guides
    @commands.command(name='goldenguides')
    async def goldenguides_complete_collection(self, ctx):
        """Link to "Complete Collection" of Golden Guides Reddit post."""
        await ctx.send('https://www.reddit.com/r/RivalsOfAether/comments/9v6pw4/')

    @commands.command(name='thebasics', aliases=['basics'])
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

    @commands.command(name='everytech')
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

    @commands.command(name='survivaldi', aliases=['di'])
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

    @commands.command(name='techchasing')
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

    # Hidden
    @commands.command(name='mindset', aliases=['jackie'])
    async def mindset_screenshot(self, ctx):
        """Send screenshot of Jackie Chan mindset post."""
        jackie = '<:jackie:547193437229940746>'
        await ctx.send(f'{jackie} https://i.imgur.com/jDnEAOz.jpg {jackie}')


def setup(bot):
    bot.add_cog(Info(bot))
