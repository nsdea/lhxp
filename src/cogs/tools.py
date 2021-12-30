try:
    from .helpers import config, management
except ImportError:
    import helpers.config, helpers.management

import discord
import traceback

from discord.ext import commands
from discord.commands import slash_command

class Tools(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(administrator=True)
    @slash_command(name='xp', description=config.load('lang')['xp-description'])
    async def xp_(self, ctx,
        user: discord.commands.Option(discord.Member, config.load('lang')['user']),
        level: discord.commands.Option(int, config.load('lang')['level-amount']),
        in_levels: discord.commands.Option(bool, config.load('lang')['if-in-levels'], required=False, default=True),
    ):
        await ctx.send(embed=discord.Embed(title=config.load('lang')['success-mod'], description=config.var(config.load('lang')['success-mod'], {'user': user}), color=management.color()))

def setup(client):
    client.add_cog(Tools(client))