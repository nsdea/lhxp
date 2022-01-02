try:
    from .helpers import config, management
except ImportError:
    import helpers.config, helpers.management

import discord

from discord.ext import commands
from discord.commands import slash_command

class AdminTools(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(administrator=True)
    @slash_command(name='setxp', description=config.lang('set-xp-description'))
    async def setxp(self, ctx,
        user: discord.commands.Option(discord.Member, config.lang('user')),
        level: discord.commands.Option(int, config.lang('level-amount')),
        in_levels: discord.commands.Option(bool, config.lang('if-in-levels'), required=False, default=True),
    ):
        await ctx.respond(embed=discord.Embed(title=config.lang('success-mod'), description=config.var(config.lang('success-mod'), {'user': user}), color=management.color()))

def setup(client):
    client.add_cog(AdminTools(client))