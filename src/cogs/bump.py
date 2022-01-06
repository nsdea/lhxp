try:
    from .helpers import config, management, xp
except ImportError:
    import helpers.config, helpers.management, helpers.xp

import discord

from discord.ext import commands
from discord.commands import slash_command

class Bump(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 302050872383242240: # bump
            if ':thumbsup:' in message.embeds[0].description: # succesful bump
                bumper = message.guild.get_member(int(message.embeds[0].description.split('@')[1].split('>')[0]), config.load()['bumper-reward-xp'])
                xp.add(bumper)
        
def setup(client):
    client.add_cog(Bump(client))