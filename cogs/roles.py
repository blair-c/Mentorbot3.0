from datetime import datetime

import discord
from discord.ext import commands

from data import rivals
from helpers import helpers


class Roles(commands.Cog):
    """Add and remove roles from users."""

    def __init__(self, bot):
        self.bot = bot

    # Role toggle commands for mentors
    @commands.command(name='dnd', hidden=True)
    @commands.has_any_role('Mentors', 'DO NOT DISTURB')
    @helpers.in_channel('teacher-lounge')
    @helpers.in_academy()
    async def do_not_disturb_toggle(self, ctx):
        """Toggle member between mentors and do not disturb roles."""
        mentors_role = discord.utils.get(ctx.guild.roles, name='Mentors')
        dnd_role = discord.utils.get(ctx.guild.roles, name='DO NOT DISTURB')
        member = ctx.guild.get_member(ctx.author.id)
        # Mentors -> DND
        if mentors_role in ctx.author.roles:
            # Change nickname
            try:
                if ctx.author.display_name[:6] != '[DND] ':
                    await ctx.author.edit(nick=f'[DND] {ctx.author.display_name}')
            except discord.errors.Forbidden:
                pass
            # Update roles and get embed
            embed = await helpers.update_roles(member, remove=mentors_role, add=dnd_role)
        # DND -> Mentors
        elif dnd_role in ctx.author.roles:
            # Change nickname
            try:
                if ctx.author.display_name[6:] == ctx.author.name:
                    await ctx.author.edit(nick=None)
                elif ctx.author.display_name[:6] == '[DND] ':
                    await ctx.author.edit(nick=ctx.author.display_name[6:])
            except discord.errors.Forbidden:
                pass
            # Update roles and get embed
            embed = await helpers.update_roles(member, remove=dnd_role, add=mentors_role)
        await ctx.send(embed=embed)

    @commands.command(name='advisor', hidden=True)
    @commands.has_role('Mentor')
    @helpers.in_channel('teacher-lounge')
    @helpers.in_academy()
    async def advisor_role_add(self, ctx):
        """Toggle mentor's roles from mentor to advisor."""
        embed = await helpers.update_roles(
            ctx.guild.get_member(ctx.author.id),
            remove=discord.utils.get(ctx.guild.roles, name='Mentor'),
            add=discord.utils.get(ctx.guild.roles, name='Advisor'))
        await ctx.send(embed=embed)

    @commands.command(name='mentor', hidden=True)
    @commands.has_role('Advisor')
    @helpers.in_channel('teacher-lounge')
    @helpers.in_academy()
    async def mentor_role_add(self, ctx):
        """Toggle mentor's roles from advisor to mentor."""
        embed = await helpers.update_roles(
            ctx.guild.get_member(ctx.author.id),
            remove=discord.utils.get(ctx.guild.roles, name='Advisor'),
            add=discord.utils.get(ctx.guild.roles, name='Mentor'))
        await ctx.send(embed=embed)

    @commands.command(name='keyboardmentor', aliases=['keyboard-mentor'], hidden=True)
    @commands.has_any_role('Mentors', 'DO NOT DISTURB')
    @helpers.in_channel('teacher-lounge')
    @helpers.in_academy()
    async def keyboard_role_toggle(self, ctx):
        """Toggle mentor's keyboard status in roles and commands."""
        member = ctx.guild.get_member(ctx.author.id)
        role = discord.utils.get(ctx.guild.roles, name='Keyboard')
        if role in member.roles:
            embed = await helpers.update_roles(member, remove=role)
        else:
            embed = await helpers.update_roles(member, add=role)
        await ctx.send(embed=embed)

    @commands.command(name='switchmentor', aliases=['switch-mentor'], hidden=True)
    @commands.has_any_role('Mentors', 'DO NOT DISTURB')
    @helpers.in_channel('teacher-lounge')
    @helpers.in_academy()
    async def switch_role_toggle(self, ctx):
        """Toggle mentor's Nintendo Switch availability status in roles and commands."""
        member = ctx.guild.get_member(ctx.author.id)
        role = discord.utils.get(ctx.guild.roles, name='Switch Mentor')
        if role in member.roles:
            embed = await helpers.update_roles(member, remove=role)
        else:
            embed = await helpers.update_roles(member, add=role)
        await ctx.send(embed=embed)

    @commands.command(name='xboxmentor', aliases=['xbox-mentor'], hidden=True)
    @commands.has_any_role('Mentors', 'DO NOT DISTURB')
    @helpers.in_channel('teacher-lounge')
    @helpers.in_academy()
    async def xbox_role_toggle(self, ctx):
        """Toggle mentor's Xbox availability status in roles and commands."""
        member = ctx.guild.get_member(ctx.author.id)
        role = discord.utils.get(ctx.guild.roles, name='Xbox Mentor')
        if role in member.roles:
            embed = await helpers.update_roles(member, remove=role)
        else:
            embed = await helpers.update_roles(member, add=role)
        await ctx.send(embed=embed)

    # Reaction system for main, secondaries, region, undergrad, and enrollment
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        """Give member character, region, pronouns, undergrad, or student role on reaction."""
        # Ignore reactions from Mentorbot
        if (user_id := payload.user_id) == self.bot.user.id: return
        # Ensure set-your-roles channel name
        guild = self.bot.get_guild(payload.guild_id)
        channel = guild.get_channel(payload.channel_id)
        if 'roles' not in channel.name: return
        # Setup
        user = self.bot.get_user(user_id)
        member = guild.get_member(user_id)
        message = await channel.fetch_message(payload.message_id)
        guild_roles = guild.roles
        emote = f'<:{payload.emoji.name}:{payload.emoji.id}>'
        ACADEMY_ID = 252352512332529664
        NACORD_ID = 63722835520004096
        TEST_SERVER_ID = 475599187812155392
        # Characters
        if message.attachments:
            img = message.attachments[0].filename
            characters = dict(rivals.characters)
            if payload.guild_id in [NACORD_ID, TEST_SERVER_ID]:
                characters['Sandbert'] = {'emote': '<:Sandbert:938163492849065994>'}
                characters['Random'] = {'emote': '<:Random:938274541413756928>'}
            # Main
            if img == 'main.png':
                for character, info in characters.items():
                    if info['emote'] == emote:
                        main_role = discord.utils.get(guild_roles, name=f'{character} (Main)')
                        await member.add_roles(main_role)
                        secondary_role = discord.utils.get(guild_roles, name=character)
                        await member.remove_roles(secondary_role)
            # Secondaries
            elif img == 'secondaries.png':
                for character, info in characters.items():
                    if info['emote'] == emote:
                        secondary_role = discord.utils.get(guild_roles, name=character)
                        await member.add_roles(secondary_role)
                        main_role = discord.utils.get(guild_roles, name=f'{character} (Main)')
                        await member.remove_roles(main_role)
            # Characters
            elif img == 'characters.png':
                for character, info in characters.items():
                    if info['emote'] == emote:
                        character_role = discord.utils.get(guild_roles, name=character)
                        await member.add_roles(character_role)
        # Region
        elif 'West Coast' in message.content:
            for region, info in rivals.regions.items():
                if info['emote'] == emote:
                    await member.add_roles(discord.utils.get(guild_roles, name=region))
        # Pronouns
        elif 'he/him' in message.content:
            if emote == '<:he_him:817651606384017419>':
                pronoun = 'he/him'
            elif emote == '<:they_them:817651606396469269>':
                pronoun = 'they/them'
            elif emote == '<:she_her:817651606685483008>':
                pronoun = 'she/her'
            elif emote == '<:any_pronouns:817651606270902293>':
                pronoun = 'any pronouns'
            elif emote == '<:ask_for_pronouns:938288388841308230>':
                pronoun = 'ask for pronouns'
            await member.add_roles(discord.utils.get(guild_roles, name=pronoun))
        # Academy only
        elif payload.guild_id in [ACADEMY_ID]:
            # Matchmaking
            if 'Matchmaking' in message.content:
                # PC
                if emote == '<:PCMatchmaking:817627642143703041>':
                    role = 'Matchmaking (PC)'
                elif emote == '<:PCNewbieMatchmaking:817627666131845131>':
                    role = 'Newbie Matchmaking (PC)'
                # Switch
                elif emote == '<:SwitchMatchmaking:758087700363477074>':
                    role = 'Matchmaking (Switch)'
                elif emote == '<:SwitchNewbieMatchmaking:758087700468465725>':
                    role = 'Newbie Matchmaking (Switch)'
                # Xbox
                elif emote == '<:XboxMatchmaking:758087700405551175>':
                    role = 'Matchmaking (Xbox)'
                elif emote == '<:XboxNewbieMatchmaking:758087700309082182>':
                    role = 'Newbie Matchmaking (Xbox)'
                await member.add_roles(discord.utils.get(guild_roles, name=role))
            # RAS
            elif 'amateur' in message.content:
                if emote == '<:NorthAmerica:547189311527845907>':
                    await member.add_roles(discord.utils.get(guild_roles, name='Undergrad'))
                elif emote == '<:Europe:547189473432305665>':
                    await member.add_roles(discord.utils.get(guild_roles, name='amatEUr'))
            # Enrollment
            elif emote == '<:roaa:547193418560962570>':
                student = discord.utils.get(guild_roles, name='Student')
                dress_code = discord.utils.get(guild_roles, name='Dress Code Violation')
                if student not in member.roles and dress_code not in member.roles:
                    await member.add_roles(student)
                    # Display enrollment in action-log
                    embed = discord.Embed(
                        color=0xfefefe,
                        description=f'{member.mention}\n**{str(member)}**',
                        timestamp=datetime.utcnow())
                    embed.set_author(name='Member Enrolled', icon_url=member.avatar_url)
                    embed.set_thumbnail(url=user.avatar_url)
                    embed.set_footer(text=f'ID: {payload.user_id}')
                    action_log = discord.utils.get(guild.text_channels, name='action-log')
                    await action_log.send(embed=embed)
        # NAcord only
        elif payload.guild_id in [NACORD_ID, TEST_SERVER_ID]:
            # Misc. roles
            if 'Speedrunning' in message.content:
                if emote == rivals.consoles['Nintendo Switch']['emote']:
                    await member.add_roles(discord.utils.get(guild_roles, name='Joycon'))
                elif emote == rivals.consoles['Xbox One']['emote']:
                    await member.add_roles(discord.utils.get(guild_roles, name='XB1'))
                elif emote == '<:Tournaments:938301433806225470>':
                    await member.add_roles(discord.utils.get(guild_roles, name='Tournament'))
                elif emote == '<:Artist:938293074730303508>':
                    await member.add_roles(discord.utils.get(guild_roles, name='Artist'))
                elif emote == '<:Speedrunning:938293098348425226>':
                    await member.add_roles(discord.utils.get(guild_roles, name='Speedrunner'))

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        """Remove member's character, region, or undergrad role on reaction remove."""
        # Ignore reactions from Mentorbot
        if (user_id := payload.user_id) == self.bot.user.id: return
        # Ensure set-your-roles channel name
        guild = self.bot.get_guild(payload.guild_id)
        channel = guild.get_channel(payload.channel_id)
        if 'roles' not in channel.name: return
        # Setup
        user = self.bot.get_user(user_id)
        member = guild.get_member(user_id)
        message = await channel.fetch_message(payload.message_id)
        guild_roles = guild.roles
        emote = f'<:{payload.emoji.name}:{payload.emoji.id}>'
        ACADEMY_ID = 252352512332529664
        NACORD_ID = 63722835520004096
        TEST_SERVER_ID = 475599187812155392
        # Characters
        if message.attachments:
            img = message.attachments[0].filename
            characters = dict(rivals.characters)
            if payload.guild_id in [NACORD_ID, TEST_SERVER_ID]:
                characters['Sandbert'] = {'emote': '<:Sandbert:938163492849065994>'}
                characters['Random'] = {'emote': '<:Random:938274541413756928>'}
            # Main
            if img == 'main.png':
                for character, info in characters.items():
                    if info['emote'] == emote:
                        main_role = discord.utils.get(guild_roles, name=f'{character} (Main)')
                        await member.remove_roles(main_role)
            # Secondaries
            elif img == 'secondaries.png':
                for character, info in characters.items():
                    if info['emote'] == emote:
                        secondary_role = discord.utils.get(guild_roles, name=character)
                        await member.remove_roles(secondary_role)
            # Characters
            elif img == 'characters.png':
                for character, info in characters.items():
                    if info['emote'] == emote:
                        character_role = discord.utils.get(guild_roles, name=character)
                        await member.remove_roles(character_role)
        # Region
        elif 'West Coast' in message.content:
            for region, info in rivals.regions.items():
                if info['emote'] == emote:
                    await member.remove_roles(discord.utils.get(guild_roles, name=region))
        # Pronouns
        elif 'he/him' in message.content:
            if emote == '<:he_him:817651606384017419>':
                pronoun = 'he/him'
            elif emote == '<:they_them:817651606396469269>':
                pronoun = 'they/them'
            elif emote == '<:she_her:817651606685483008>':
                pronoun = 'she/her'
            elif emote == '<:any_pronouns:817651606270902293>':
                pronoun = 'any pronouns'
            elif emote == '<:ask_for_pronouns:938288388841308230>':
                pronoun = 'ask for pronouns'
            await member.remove_roles(discord.utils.get(guild_roles, name=pronoun))
        # Academy Only
        elif payload.guild_id in [ACADEMY_ID]:
            # Matchmaking
            if 'Matchmaking' in message.content:
                # PC
                if emote == '<:PCMatchmaking:817627642143703041>':
                    role = 'Matchmaking (PC)'
                elif emote == '<:PCNewbieMatchmaking:817627666131845131>':
                    role = 'Newbie Matchmaking (PC)'
                # Switch
                elif emote == '<:SwitchMatchmaking:758087700363477074>':
                    role = 'Matchmaking (Switch)'
                elif emote == '<:SwitchNewbieMatchmaking:758087700468465725>':
                    role = 'Newbie Matchmaking (Switch)'
                # Xbox
                elif emote == '<:XboxMatchmaking:758087700405551175>':
                    role = 'Matchmaking (Xbox)'
                elif emote == '<:XboxNewbieMatchmaking:758087700309082182>':
                    role = 'Newbie Matchmaking (Xbox)'
                await member.remove_roles(discord.utils.get(guild_roles, name=role))
            # RAS
            elif 'amateur' in message.content:
                if emote == '<:NorthAmerica:547189311527845907>':
                    await member.remove_roles(discord.utils.get(guild_roles, name='Undergrad'))
                elif emote == '<:Europe:547189473432305665>':
                    await member.remove_roles(discord.utils.get(guild_roles, name='amatEUr'))
        # NAcord only
        elif payload.guild_id in [NACORD_ID, TEST_SERVER_ID]:
            # Misc. roles
            if 'Speedrunning' in message.content:
                if emote == rivals.consoles['Nintendo Switch']['emote']:
                    await member.remove_roles(discord.utils.get(guild_roles, name='Joycon'))
                elif emote == rivals.consoles['Xbox One']['emote']:
                    await member.remove_roles(discord.utils.get(guild_roles, name='XB1'))
                elif emote == '<:Tournaments:938301433806225470>':
                    await member.remove_roles(discord.utils.get(guild_roles, name='Tournament'))
                elif emote == '<:Artist:938293074730303508>':
                    await member.remove_roles(discord.utils.get(guild_roles, name='Artist'))
                elif emote == '<:Speedrunning:938293098348425226>':
                    await member.remove_roles(discord.utils.get(guild_roles, name='Speedrunner'))

    @commands.command(name='setyourroles', aliases=['set-your-roles'])
    @commands.has_permissions(ban_members=True)
    async def set_your_roles_channel_setup(self, ctx):
        """Send and react to messages to set up role reaction system channel."""
        if 'roles' not in ctx.message.channel.name: return
        ACADEMY_ID = 252352512332529664
        NACORD_ID = 63722835520004096
        TEST_SERVER_ID = 475599187812155392
        emojis = self.bot.get_guild(TEST_SERVER_ID).emojis
        # Introduction
        intro = ('• **Add reactions below to set your main, secondaries, and region.**\n'
                '• Reacting too quickly may cause the bot to fail in adding/removing roles.\n'
                '• You might need to react and unreact for the role to be added properly.')
        if ctx.message.guild.id in [ACADEMY_ID]:
            intro = 'Hello! Welcome to the **Rivals of Aether Academy!**\n\n' + intro
        await ctx.send(intro)
        # Characters
        emotes = [c.replace(' ', '') for c in rivals.characters]
        if ctx.message.guild.id in [NACORD_ID, TEST_SERVER_ID]:
            emotes.append('Sandbert')
            emotes.append('Random')
        if ctx.message.guild.id in [ACADEMY_ID, NACORD_ID, TEST_SERVER_ID]:
            # Main
            msg = await ctx.send(file=discord.File('images/setyourroles/main.png'))
            for emote in emotes:
                await msg.add_reaction(discord.utils.get(emojis, name=emote))
            # Secondaries
            msg = await ctx.send(file=discord.File('images/setyourroles/secondaries.png'))
            for emote in emotes:
                await msg.add_reaction(discord.utils.get(emojis, name=emote))
        else:
            # Characters
            msg = await ctx.send(file=discord.File('images/setyourroles/characters.png'))
            for emote in emotes:
                await msg.add_reaction(discord.utils.get(emojis, name=emote))
        # Region
        await ctx.send(file=discord.File('images/setyourroles/region.png'))
        msg = await ctx.send(
            '\n'.join([f'{info["emote"]} → {region}' for region, info in rivals.regions.items()]))
        for region in rivals.regions:
            await msg.add_reaction(discord.utils.get(emojis, name=region.replace(' ', '')))
        # Pronouns
        await ctx.send(file=discord.File('images/setyourroles/pronouns.png'))
        msg = await ctx.send(
            '<:he_him:817651606384017419> → `he/him`\n'
            '<:they_them:817651606396469269> → `they/them`\n'
            '<:she_her:817651606685483008> → `she/her`\n'
            '<:any_pronouns:817651606270902293> → `any pronouns`\n'
            '<:ask_for_pronouns:938288388841308230> → `ask for pronouns`')
        for emote in (['he_him', 'they_them', 'she_her', 'any_pronouns', 'ask_for_pronouns']):
            await msg.add_reaction(discord.utils.get(emojis, name=emote))
        # Academy only
        if ctx.message.guild.id in [ACADEMY_ID]:
            # Matchmaking
            await ctx.send(file=discord.File('images/setyourroles/matchmaking.png'))
            msg = await ctx.send(
                # Steam
                '<:PCMatchmaking:817627642143703041> → Matchmaking (PC)\n'
                '<:PCNewbieMatchmaking:817627666131845131> → Newbie Matchmaking (PC)\n'
                # Switch
                '<:SwitchMatchmaking:758087700363477074> → Matchmaking (Switch)\n'
                '<:SwitchNewbieMatchmaking:758087700468465725> → Newbie Matchmaking (Switch)\n'
                # Xbox
                '<:XboxMatchmaking:758087700405551175> → Matchmaking (Xbox)\n'
                '<:XboxNewbieMatchmaking:758087700309082182> → Newbie Matchmaking (Xbox)')
            for emote in (['PCMatchmaking', 'PCNewbieMatchmaking', 'SwitchMatchmaking', 
                        'SwitchNewbieMatchmaking', 'XboxMatchmaking', 'XboxNewbieMatchmaking']):
                await msg.add_reaction(discord.utils.get(emojis, name=emote))
            # RAS
            await ctx.send(file=discord.File('images/setyourroles/ras.png'))
            msg = await ctx.send(
                '• **If you would like to be notified for our weekly amateur tournaments '
                ' (Rivals Amateur Series), please click on a region reaction below.**\n'
                '• Click on the reaction again to opt out of notifications.\n'
                '<:NorthAmerica:547189311527845907> → North America\n'
                '<:Europe:547189473432305665> → Europe')
            for region in ['NorthAmerica', 'Europe']:
                await msg.add_reaction(discord.utils.get(emojis, name=region))
            # Enroll
            await ctx.send(file=discord.File('images/setyourroles/enroll.png'))
            msg = await ctx.send(
                '• **Is this the only channel you can see?**\n'
                '• Click the <:roaa:547193418560962570> reaction below to enroll in the '
                'server and view the rest of the channels!')
            await msg.add_reaction(discord.utils.get(emojis, name='roaa'))
        # NAcord only
        if ctx.message.guild.id in [NACORD_ID, TEST_SERVER_ID]:
            # More
            await ctx.send(file=discord.File('images/setyourroles/more.png'))
            msg = await ctx.send(
                # Consoles
                f'{rivals.consoles["Nintendo Switch"]["emote"]} → Nintendo Switch\n'
                f'{rivals.consoles["Xbox One"]["emote"]} → Xbox One\n'
                # Misc. Roles
                '<:Tournaments:938301433806225470> → Tournaments\n'
                '<:Artist:938293074730303508> → Artist\n'
                '<:Speedrunning:938293098348425226> → Speedrunning')
            for emote in ['NintendoSwitch', 'XboxOne', 'Tournaments', 'Artist', 'Speedrunning']:
                await msg.add_reaction(discord.utils.get(emojis, name=emote))

def setup(bot):
    bot.add_cog(Roles(bot))
