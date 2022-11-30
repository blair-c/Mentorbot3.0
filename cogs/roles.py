from datetime import datetime

import discord
from discord.ext import commands

from data import rivals


class Roles(commands.Cog):
    """Add and remove roles from users."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    # Reaction system for main, secondaries, region, undergrad, and enrollment
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        """Give member character, region, pronouns, undergrad, or student role on reaction."""
        # Ignore reactions from Mentorbot
        if (user_id := payload.user_id) == self.bot.user.id: return
        # Ensure set-your-roles channel name
        guild = self.bot.get_guild(payload.guild_id)
        channel = guild.get_channel(payload.channel_id)
        if not channel or 'roles' not in channel.name: return
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
        elif payload.guild_id in [ACADEMY_ID, TEST_SERVER_ID]:
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
            # Open
            elif 'open' in message.content:
                if emote == '<:NorthAmerica:547189311527845907>':
                    await member.add_roles(discord.utils.get(guild_roles, name='Intramural'))
            # Enrollment
            elif emote == '<:roaa:547193418560962570>':
                student = discord.utils.get(guild_roles, name='Student')
                dress_code = discord.utils.get(guild_roles, name='Dress Code Violation')
                if student not in member.roles and dress_code not in member.roles:
                    await member.add_roles(student)
        # NAcord only
        elif payload.guild_id in [NACORD_ID]:
            # Misc. roles
            if 'Speedrunning' in message.content:
                if emote == '<:NintendoSwitch:938304361635913798>':
                    await member.add_roles(discord.utils.get(guild_roles, name='Joycon'))
                elif emote == '<:XboxOne:938304372356571176>':
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
        if not channel or 'roles' not in channel.name: return
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
        elif payload.guild_id in [ACADEMY_ID, TEST_SERVER_ID]:
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
            # Open
            elif 'open' in message.content:
                if emote == '<:NorthAmerica:547189311527845907>':
                    await member.remove_roles(discord.utils.get(guild_roles, name='Intramural'))
        # NAcord only
        elif payload.guild_id in [NACORD_ID]:
            # Misc. roles
            if 'Speedrunning' in message.content:
                if emote == '<:NintendoSwitch:938304361635913798>':
                    await member.remove_roles(discord.utils.get(guild_roles, name='Joycon'))
                elif emote == '<:XboxOne:938304372356571176>':
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
        intro = ('• **Add reactions below to set your roles.**\n'
                '• Reacting too quickly may cause the bot to fail in adding/removing roles.\n'
                '• You might need to react and unreact for the role to be added properly.')
        if ctx.message.guild.id in [ACADEMY_ID]:
            intro = 'Hello! Welcome to the **Rivals of Aether Academy!**\n\n' + intro
        await ctx.send(intro)
        # Characters
        emotes = [c.replace(' ', '') for c in rivals.characters]
        if ctx.message.guild.id in [NACORD_ID]:
            emotes.append('Sandbert')
            emotes.append('Random')
        # Main
        msg = await ctx.send(file=discord.File('images/setyourroles/main.png'))
        for emote in emotes:
            await msg.add_reaction(discord.utils.get(emojis, name=emote))
        # Secondaries
        msg = await ctx.send(file=discord.File('images/setyourroles/secondaries.png'))
        for emote in emotes:
            await msg.add_reaction(discord.utils.get(emojis, name=emote))
        # Characters
        msg = await ctx.send(file=discord.File('images/setyourroles/characters.png'))
        for emote in emotes:
            await msg.add_reaction(discord.utils.get(emojis, name=emote))
        # Region
        if ctx.message.guild.id in [ACADEMY_ID, NACORD_ID, TEST_SERVER_ID]:
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
        if ctx.message.guild.id in [ACADEMY_ID, TEST_SERVER_ID]:
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
            # Tournaments
            await ctx.send(file=discord.File('images/setyourroles/tournaments.png'))
            msg = await ctx.send(
                '• **If you would like to be notified for our weekly amateur tournaments** '
                '(Rivals Amateur Series)**, click on a region reaction below.**\n'
                '<:NorthAmerica:547189311527845907> → Thursdays at 8 PM ET / 5 PM PT\n'
                '<:Europe:547189473432305665> → Saturdays at 20:30 CEST')
            for region in ['NorthAmerica', 'Europe']:
                await msg.add_reaction(discord.utils.get(emojis, name=region))
            msg = await ctx.send(
                '• **If you would like to be notified for our weekly North American open '
                'brackets** (Go to School: Wednesdays at 8 PM ET / 5 PM PT)**, plus additional '
                'Academy open brackets, click on the reaction below.**')
            await msg.add_reaction(discord.utils.get(emojis, name='NorthAmerica'))
            # Enroll
            await ctx.send(file=discord.File('images/setyourroles/enroll.png'))
            msg = await ctx.send(
                '• **Is this the only channel you can see?**\n'
                '• Click the <:roaa:547193418560962570> reaction below to enroll in the '
                'server and view the rest of the channels!')
            await msg.add_reaction(discord.utils.get(emojis, name='roaa'))
        # NAcord only
        if ctx.message.guild.id in [NACORD_ID]:
            # More
            await ctx.send(file=discord.File('images/setyourroles/more.png'))
            msg = await ctx.send(
                # Consoles
                '<:NintendoSwitch:938304361635913798> → Nintendo Switch\n'
                '<:XboxOne:938304372356571176> → Xbox One\n'
                # Misc. Roles
                '<:Tournaments:938301433806225470> → Tournaments\n'
                '<:Artist:938293074730303508> → Artist\n'
                '<:Speedrunning:938293098348425226> → Speedrunning')
            for emote in ['NintendoSwitch', 'XboxOne', 'Tournaments', 'Artist', 'Speedrunning']:
                await msg.add_reaction(discord.utils.get(emojis, name=emote))

async def setup(bot: commands.Bot):
    await bot.add_cog(Roles(bot))
