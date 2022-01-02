try:
    from .helpers import config, management
except ImportError:
    import helpers.config, helpers.management

import socket
import discord.commands

from discord.ext import commands
from discord.commands import slash_command

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @slash_command(name='info', description=config.lang('help-command-description'))
    async def info(self, ctx):
        await ctx.respond(embed=discord.Embed(title=config.lang('help-title'), description=config.lang('help-description', {'user': ctx.author.name}), color=management.color()))

    @slash_command(description=config.lang('ping-description'))
    async def ping(self, ctx):
        embed = discord.Embed(title=config.lang('stats'), color=management.color(), timestamp=management.get_start_time())
        embed.add_field(name=':desktop: Ping', value=str(round(self.client.latency * 1000, 2)) + 'ms')
        await ctx.respond(embed=embed)


def setup(client):
    client.add_cog(Info(client))