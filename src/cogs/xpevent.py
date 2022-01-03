try:
    from .helpers import config, management, xp
except ImportError:
    import helpers.config, helpers.management, helpers.xp

import discord

from discord.ext import commands
from discord.commands import slash_command

class XPEvent(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        text = message.content.replace('  ', '') # avoid spam
        xp_gain = text.count(' ')*config.load()['word-reward-xp'] # word count

        if xp_gain < 2: # don't go into negative XP numbers!
            xp_gain = config.load()['word-reward-xp']

        xp.add(message.author, xp_gain)

        await self.client.process_commands(message)

def setup(client):
    client.add_cog(XPEvent(client))