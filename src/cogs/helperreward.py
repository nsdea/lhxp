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

    @slash_command(description=config.lang('helper-description'))
    async def thank(self, ctx,
        user: discord.commands.Option(discord.Member, config.lang('user')),
    ):
        if not config.load('helperreward').get(ctx.author.id): # user has never thanked someone before
            config.set('helperreward', ctx.author.id, -1) # reset it to -1

        if ctx.author == user:
            return await ctx.respond(embed=discord.Embed(title=config.lang('helper-cant-thank-themselves'), color=management.color('error')))

        if user.bot:
            return await ctx.respond(embed=discord.Embed(title=config.lang('helper-cant-thank-bot'), color=management.color('error')))

        if time.time() - config.load('helperreward')[ctx.author.id] < 60*60*12: # cooldown of 12 hours - has to be calculated in seconds
            return await ctx.respond(embed=discord.Embed(title=config.lang('cooldown-title'), description=config.lang('cooldown-description'), color=management.color('error')))
 
        config.set('helperreward', ctx.author.id, time.time()) # save time of the person who thanked
        config.change('xp', user.id, config.load()['helper-reward-xp'])

        await ctx.respond(embed=discord.Embed(title=config.lang('helper-thanks-title'), description=config.lang('helper-thanks-description'), color=management.color()))

def setup(client):
    client.add_cog(HelperReward(client))