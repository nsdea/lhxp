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

    @slash_command(name='help', description=config.load()['info-description'])
    async def helpcmd(self, ctx):
        embed = discord.Embed(title='Stop it, get some help!', color=management.color(), description='')
        embed.set_image(url='https://sayingimages.com/wp-content/uploads/stop-it-help-meme.jpg')
        
        await ctx.respond(embed=embed)

    @slash_command(description=config.load()['stats-description'])
    async def stats(self, ctx):
        embed = discord.Embed(
            title='Bot Stats',
            description='** **',
            color=management.color(),
        )
        embed.add_field(name='Servers', value=f'{len(self.client.guilds)}')
        embed.add_field(name='Members', value=f'{len(self.client.users)}')
        embed.set_footer(text='💙')
        
        await ctx.respond(embed=embed)

    @slash_command(description=config.load()['ping-description'])
    async def ping(self, ctx):
        embed = discord.Embed(title=config.load()['stats'], color=management.color(), timestamp=management.get_start_time())
        embed.add_field(name=':desktop: Ping', value=str(round(self.client.latency * 1000, 2)) + 'ms')
        await ctx.respond(embed=embed)


def setup(client):
    client.add_cog(Info(client))