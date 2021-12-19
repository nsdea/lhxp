try:
    from .helpers import config, management
except ImportError:
    import helpers.config, helpers.management

import discord
import traceback

from discord.ext import commands
from discord.commands import slash_command

class AdminTools(commands.Cog):
    def __init__(self, client):
        self.client = client

    @slash_command(name='xp', description='🎚️ Admin only » Sets the experience points or level of an user')
    async def xp_(self, ctx,
        user: discord.commands.Option(discord.Member, 'User'),
        level: discord.commands.Option(int, 'Level Amount'),
        in_levels: discord.commands.Option(bool, 'Percent', required=False, default=True),
    ):
        await ctx.send(embed=discord.Embed(title='', description='', color=management.color()))

def setup(client):
    client.add_cog(AdminTools(client))