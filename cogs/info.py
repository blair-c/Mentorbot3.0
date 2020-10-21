import discord
from discord.ext import commands


class Info(commands.Cog):
    """Send informational Rivals links and formatted displays."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='commands')
    async def commands_list(self, ctx):
        """List all info commands."""
        embed = discord.Embed()
        embed.set_author(name='Commands List', icon_url=self.bot.user.avatar_url)
        commands = {
            'Rivals Data':
                ['angleflippers', 'dodgedata', 'forceflinch', 'hitpauseformula', 
                 'hitstunformula', 'knockbackformula'],
            'Videos & Clips':
                ['AAAA', 'babydashing', 'bairhitfall', 'pwjpecotr'],
            'Mentorbot/Misc.':
                ['about', 'help', 'replays'],
            'Beefy Aether Doods':
                ['cactuardashing', 'DI', 'horizontalwaveland', 'ledgecancel','RAR',
                 'teching', 'wavedashing'],
            'Golden Guides':
                ['goldenguides', 'thebasics', 'everytech', 'survivaldi', 'techchasing'],
            'Sector 7-G Resources':
                ['framedata', 'hurtboxdata', 'generalstats', 'patchnotes']
        }
        for category in commands:
            commands_list = [f'!{command}' for command in commands[category]]
            commands_list = '\n'.join(commands_list)
            embed.add_field(name=f'{category}', value=f'```{commands_list}```')
        await ctx.send(embed=embed)

    # Rivals Data
    @commands.command(name='angleflippers', aliases=['angleflipper', 'flippers', 'flipper'])
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
            '9 - Hits toward the center of the hitbox\n'
            '10 - Sends in the direction the player is moving```')
        embed = discord.Embed(title='Angle Flipper Definitions', description=definitions)
        await ctx.send(embed=embed)

    @commands.command(name='dodgedata', aliases=['parry', 'roll', 'airdodge', 'dodge'])
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
             '\n**Roll** ```ml\n'
             'Startup      | 4    \n'
             'Invulnerable | 5-19 \n'
             'Endlag       | 12   \n'
             'FAF          | 31```'
             # Airdodge
             '\n**Airdodge** ```ml\n'
             'Startup      | 2    \n'
             'Invulnerable | 3-15 \n'
             'Endlag       | 12   \n'
             'FAF          | 27```'))
        embed.set_author(name='Universal Dodge Frame Data')
        await ctx.send(embed=embed)

    @commands.command(name='forceflinch', aliases=['flinch'])
    async def force_flinch_definitions(self, ctx, *formula):
        """Send display of force flinch definitions."""
        definitions = ('```glsl\n'
            '1 - Forces a flinch, unless the attack is crouch cancelled\n'
            '2 - Cannot cause flinch, even if crouch cancelled\n'
            '3 - Can always be crouch cancelled, regardless of percent```')
        embed = discord.Embed(title='Force Flinch Definitions', description=definitions)
        await ctx.send(embed=embed)

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

    @commands.command(name='knockbackformula', aliases=['knockback', 'kbformula', 'kb'])
    async def knockback_formula(self, ctx, *formula):
        """Send display of Rivals' knockback formula."""
        formula = ('```ml\n'
                   'BKB + Damage * Knockback_Scaling * 0.12 * Knockback_Adj```')
        embed = discord.Embed(title='Knockback Formula', description=formula)
        await ctx.send(embed=embed)

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
        """Link to Rivals Dojo video covering babydashing."""
        await ctx.send('https://www.youtube.com/watch?v=BW1M8zx_KGM')

    @commands.command(name='bairhitfall')
    async def bair_hitfall_tutorial(self, ctx):
        """Link to clip of and instructions for the hitfalling tutorial."""
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

    @commands.command(name='pwjpecotr')
    async def pwjpecotr(self, ctx):
        """Link to MSB's pwjpecotr tweet."""
        await ctx.send('https://twitter.com/notMSB/status/1025537436565364738')

    # Mentorbot
    @commands.command(name='about', aliases=['info', 'information', 'invite'], hidden=True)
    async def info_command(self, ctx):
        """Display information about Mentorbot."""
        embed = discord.Embed(
            description='A custom Discord bot by the Rivals of Aether Academy.')
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
        embed.add_field(
            name='<:Mentorbot:640465696869974017> Add Mentorbot to your own server:',
            value=('https://discordapp.com/api/oauth2/authorize?'
                   'client_id=475596740368793600&permissions=264192&scope=bot'))
        await ctx.send(embed=embed)

    @commands.command(name='help', aliases=['syntax'], hidden=True)
    async def help_command(self, ctx, *arg):
        """Display information and command syntax for hitbox commands."""
        embed = discord.Embed()
        embed.set_author(name='Hitbox Command Syntax', icon_url=self.bot.user.avatar_url)
        embed.add_field(
            name='`![character] [move]`',
            value='Multiple character and move names are supported, try it out!')
        embed.set_image(url='https://i.imgur.com/nHBfPyL.png')
        embed.set_footer(text='For non-hitbox commands, try !commands.')
        await ctx.send(embed=embed)

    @commands.command(name='replays')
    async def how_to_access_your_replays(self, ctx, *arg):
        """Display instructions to access your RoA replays."""
        embed = discord.Embed()
        embed.set_author(name='How to Access Your Replays', icon_url=self.bot.user.avatar_url)
        embed.add_field(
            name='Method 1:',
            value='1. Press `Win + R`\n' 
                  '2. Put in the following: ```%LocalAppData%\\RivalsOfAether\\replays```',
            inline=False)
        embed.add_field(
            name='Method 2:',
            value='1. Make sure "Hidden items" are shown in File Explorer\n'
                  '2. Go to ```C:\\Users\\yourname\\AppData\\Local\\RivalsofAether\\replays```',
            inline=False)
        await ctx.send(embed=embed)

    # Beefy Aether Doods
    @commands.command(name='cactuardashing', aliases=['cactuar','cactuardash'])
    async def beefy_cactuardashing(self, ctx):
        """Link to Beefy Aether Doods video covering cactuar dashing."""
        await ctx.send('https://www.youtube.com/watch?v=SBQOpChfbx4')

    @commands.command(name='DI', aliases=['directionalinfluence'])
    async def beefy_di(self, ctx):
        """Link to Beefy Aether Doods video covering DI."""
        await ctx.send('https://www.youtube.com/watch?v=-22VyPy6QZU')

    @commands.command(name='horizontalwaveland', aliases=['horizontalwavelanding'])
    async def beefy_horizontalwaveland(self, ctx):
        """Link to Beefy Aether Doods video covering horizontal wavelanding."""
        await ctx.send('https://www.youtube.com/watch?v=ejN--TPcePE')

    @commands.command(name='ledgecancel', aliases=['legdeslip'])
    async def beefy_ledgecancel(self, ctx):
        """Link to Beefy Aether Doods video covering ledge cancelling."""
        await ctx.send('https://www.youtube.com/watch?v=6N6joIHrqDg')

    @commands.command(name='RAR', aliases=['reverse_aerial_rush'])
    async def beefy_rar(self, ctx):
        """Link to Beefy Aether Doods video covering reverse aerial rush."""
        await ctx.send('https://www.youtube.com/watch?v=M8XgHJkAltw')

    @commands.command(name='teching', aliases=['tech', 'techroll'])
    async def beefy_teching(self, ctx):
        """Link to Beefy Aether Doods video covering teching."""
        await ctx.send('https://www.youtube.com/watch?v=tc781GiW20Q')
        await ctx.send('https://cdn.discordapp.com/attachments/254803568308125706/730293957699043428/roaknockdownframedata-1.png')

    @commands.command(name='wavedash', aliases=['waveland', 'wavedashing', 'wavelanding'])
    async def beefy_wavedash_waveland(self, ctx):
        """Link to Beefy Aether Doods video covering wavedashing and wavelanding."""
        await ctx.send('https://www.youtube.com/watch?v=RkLciJMr42g')

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

    @commands.command(name='survivaldi')
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

    # Sector 7-G Resources
    @commands.command(name='framedata')
    async def frame_data_doc(self, ctx):
        """Link to SNC's frame data document."""
        link = ('https://docs.google.com/spreadsheets/d/'
                '19UtK7xG2c-ehxdlhCFKMpM4_IHSG-EXFgXLJaunE79I')
        embed = discord.Embed(
            url=link,
            title='Rivals of Aether Academy Frame Data - Updated for 1.4.25',
            description='Data extracted manually in-game and from dev-mode files by SNC. '
                        'Extra information provided by Menace13 and Youngblood. '
                        'General Stats created by Kisuno. '
                        'Collated Patch Notes created by SNC.')
        embed.set_thumbnail(url='https://i.imgur.com/NCdvqoG.png')
        await ctx.send(content=link, embed=embed)

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

    @commands.command(name='generalstats', aliases=['stats'])
    async def hurtbox_data(self, ctx):
        """Link to Kisuno's general stats doc."""
        link = ('https://docs.google.com/spreadsheets/d/'
                '14JIjL_5t81JHqnJmU6BSsRosTe2JO8sFGUysM_9tDoU')
        embed = discord.Embed(
            url=link,
            title='Rivals General Stats - Updated for 1.4.0',
            description='Data extracted from devmode files and formatted by Kisuno. '
                        'Info provided by Menace13, Youngblood and SNC.')
        embed.set_thumbnail(url='https://i.imgur.com/5Iy3ZrX.png')
        await ctx.send(content=link, embed=embed)

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

    # Hidden
    @commands.command(name='jackie', aliases=['mindset'])
    async def jackie_screenshot(self, ctx):
        """Send screenshot of Jackie Chan mindset post."""
        jackie = '<:jackie:547193437229940746>'
        await ctx.send(f'{jackie} https://i.imgur.com/jDnEAOz.jpg {jackie}')


def setup(bot):
    bot.add_cog(Info(bot))
