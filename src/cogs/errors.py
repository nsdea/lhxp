try:
    from .helpers import config, management
except ImportError:
    import helpers.config, helpers.management

import discord
import traceback

from discord.ext import commands
from discord.commands import slash_command

class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        error_message = '\n'.join(traceback.format_exception(type(error), error, error.__traceback__))
        error_message = error_message.split('\n\nThe above exception was the direct cause of the following exception:')[0]
        error_message = error_message.split('Traceback (most recent call last):\n\n')[1]

        if 'self.callback(self.cog, ctx, **kwargs)' in error_message:
            error_message = error_message.split('self.cog, ctx, **kwargs)\n\n')[1]

        embed = discord.Embed(
            title=config.lang('error-title'),
            description=f'{config.lang("error-tip")}\n```py\n{error_message[:1900]}```',
            color=management.color('error')
        )

        try:
            await ctx.respond(embed=embed)
        except:
            await ctx.send(embed=embed)

        if management.testing_mode():
            raise error # if this is a testing system, show the full error in the console

def setup(client):
    client.add_cog(Errors(client))