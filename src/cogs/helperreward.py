try:
    from .helpers import config, management
except ImportError:
    import helpers.config, helpers.management

import time
import discord

from discord.ext import commands
from discord.commands import slash_command

class HelperReward(commands.Cog):
    def __init__(self, client):
        self.client = client

    @slash_command(description=config.load('lang')['helper-description'])
    async def helfer(self, ctx,
        user: discord.commands.Option(discord.Member, config.load('lang')['user']),
    ):
        ctx.author.id

        xp_dict = config.load('xp')
        xp_dict[message.author.id] += xp_gain
        config.save(xp_dict, 'xp')



def setup(client):
    client.add_cog(HelperReward(client))