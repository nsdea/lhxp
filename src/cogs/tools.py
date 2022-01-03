try:
    from .helpers import config, management, xp
except ImportError:
    import helpers.config, helpers.management, helpers.xp

import discord
import traceback

from discord.ext import commands
from discord.commands import slash_command

class Tools(commands.Cog):
    def __init__(self, client):
        self.client = client

    @slash_command(name='xp', description=config.lang('xp-command-description'))
    async def xp_(self, ctx,
        user: discord.commands.Option(discord.Member, config.lang('user'), required=False, default=None)
    ):
        if user.bot:
            return await ctx.respond(embed=discord.Embed(title=config.lang('xp-bot-error'), color=management.color('error')))

        user = user or ctx.author
        rank_color = discord.Color(0x000000)
        user_rank = config.lang('standard-rank')

        for role in user.roles:
            for rank in list(config.load('ranks').values()):
                if role.id in rank and role.name != '@everyone':
                    user_rank = role.name
                    rank_color = role.color
                    break

        level_for_next_rank = ''

        rank_num = 1
        for rank in list(config.load('ranks').keys()):
            if xp.level_of(user) > rank:
                level_for_next_rank = list(config.load('ranks').keys())[rank_num]
                break


        bar_fill = config.load()['bar-fill']
        bar_empty = config.load()['bar-empty']
        
        bar_progress = xp.of(user) - xp.needed_for_level(user)
        bar_full = xp.needed_for_next_level(user) - xp.needed_for_level(user)

        bars = round(bar_progress/bar_full*10)
        bar = (bar_fill*bars) + bar_empty*(10-bars)

        await ctx.respond(embed=discord.Embed(
            title=config.lang('xp-title', {'user': str(user)}),
            description=config.lang('xp-description', {'level_amount': xp.level_of(user), 'level_for_next_rank': level_for_next_rank, 'rank': user_rank, 'xp_amount': xp.of(user), 'xp_for_next_level': xp.needed_for_next_level(user), 'bar': bar}),
            color=rank_color).set_thumbnail(url=user.avatar.url)
        )

    @slash_command(description=config.lang('leaderboard-command-description'))
    async def leaderboard(self, ctx):
        users = sorted(config.load('xp').items(), key=lambda x:x[1], reverse=True)
        users = dict(users[:10])

        emojis = [':first_place:', ':second_place:', ':third_place:', ':four:', ':five:', ':six:', ':seven:', ':eight:', ':nine:']

        text = '\n'
        place = 0

        for user in list(users.keys()):
            text += f'{emojis[place]} {ctx.guild.get_member(user).mention} **{xp.level_of(user)}** \n'
            place += 1

        await ctx.respond(embed=discord.Embed(title=config.lang('leaderboard-title'), description=text, color=management.color()))

def setup(client):
    client.add_cog(Tools(client))