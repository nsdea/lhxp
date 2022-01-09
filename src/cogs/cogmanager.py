try:
    from .helpers import config, management, xp
except ImportError:
    import helpers.config, helpers.management, helpers.xp

import discord

from discord.ext import commands
from discord.commands import slash_command

class CogManager(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(administrator=True)
    @slash_command(description=config.lang('reload-description'))
    async def refresh(self, ctx, cog: discord.commands.Option(str, config.lang('cog'), required=False, default='')):
        if cog == 'error.test':
            raise Exception('Intentional Testing Error')

        if not cog:
            cog_list_joiner = '\n**»** '
            return await ctx.respond(embed=discord.Embed(title=config.lang('reload-list-title'), description=f'**»** {cog_list_joiner.join([str(c) for c in self.client.cogs])}', color=management.color()))

        if not cog in [c.lower() for c in self.client.cogs]:
            return await ctx.respond(embed=discord.Embed(title=config.lang('error-reload'), color=management.color('error')))

        self.client.reload_extension('cogs.' + cog) 
        return await ctx.respond(embed=discord.Embed(title=config.lang('success-reload'), color=management.color()))

def setup(client):
    client.add_cog(CogManager(client))