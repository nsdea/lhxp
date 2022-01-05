try:
    from .helpers import config, management, xp
except ImportError:
    import helpers.config, helpers.management, xp

import discord

from discord.ext import commands
from discord.commands import slash_command

class AdminTools(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(administrator=True)
    @slash_command(description=config.lang('set-xp-description'))
    async def setxp(self, ctx,
        user: discord.commands.Option(discord.Member, config.lang('user')),
        level: discord.commands.Option(int, config.lang('level-amount')),
        in_levels: discord.commands.Option(bool, config.lang('if-in-levels'), required=False, default=True),
    ):
        if in_levels:
            level = level**2

        config.set('xp', user.id, level)
        await ctx.respond(embed=discord.Embed(title=config.lang('success-mod'), color=management.color()))

    @commands.has_permissions(administrator=True)
    @slash_command(description=config.lang('change-xp-description'))
    async def changexp(self, ctx,
        user: discord.commands.Option(discord.Member, config.lang('user')),
        level: discord.commands.Option(int, config.lang('level-amount')),
        in_levels: discord.commands.Option(bool, config.lang('if-in-levels'), required=False, default=True),
    ):
        if in_levels:
            level = level**2

        config.change('xp', user.id, level)
        await ctx.respond(embed=discord.Embed(title=config.lang('success-mod'), color=management.color()))

    @commands.has_permissions(administrator=True)
    @slash_command(description=config.lang('clear-xp-description'))
    async def clearxp(self, ctx,
        user: discord.commands.Option(discord.Member, config.lang('user')),
    ):
        config.set('xp', user.id, 0)
        await ctx.respond(embed=discord.Embed(title=config.lang('success-mod'), color=management.color()))


def setup(client):
    client.add_cog(AdminTools(client))