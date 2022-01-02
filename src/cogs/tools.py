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

    @commands.has_permissions(administrator=True)
    @slash_command(name='xp', description=config.lang('xp-command-description'))
    async def xp_(self, ctx,
        user: discord.commands.Option(discord.Member, config.lang('user'), required=False, default=None)
    ):
        user = user or ctx.author
        rank_color = discord.Color(0x000000)
        user_rank = config.lang('standard-rank')

        for role in user.roles:
            for rank in list(config.load('ranks').values()):
                if role.id in rank and role.name != '@everyone':
                    user_rank = role.name
                    rank_color = role.color
                    break

        level_for_next_rank = 1

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

def setup(client):
    client.add_cog(Tools(client))