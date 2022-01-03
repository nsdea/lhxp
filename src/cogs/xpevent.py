try:
    from .helpers import config, management, xp, spam
except ImportError:
    import helpers.config, helpers.management, helpers.xp, helpers.spam

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

        message_is_spam = False
        message_content = message.content

        if spam.is_spam(message_content):
            message_is_spam = True
            await message.delete()

        last_message = await message.channel.history().get(author__name=message.author.name)

        if spam.is_spam(message_content + last_message.content):
            message_is_spam = True

        messages = []
        async for msg in message.channel.history(limit=2):
            messages.append(msg)

        if message_is_spam or messages[0].content == messages[1].content:
            try:
                await message.delete()
                await last_message.delete()
            except:
                pass
            return

        text = message.content.replace('  ', '') # avoid spam
        xp_gain = text.count(' ')*config.load()['word-reward-xp'] # word count

        if xp_gain < 2: # don't go into negative XP numbers!
            xp_gain = config.load()['word-reward-xp']

        xp.add(message.author, xp_gain)

        await self.client.process_commands(message)

def setup(client):
    client.add_cog(XPEvent(client))