try:
    from .helpers import config, management, translate
except ImportError:
    import helpers.config, helpers.management, helpers.translate

import html
import discord
import requests
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

        error_view_url = requests.post('https://onlix.me/view-create', json={'title': html.escape(str(error)), 'text': html.escape(error_message)}).text
        
        if 'self.callback(self.cog, ctx, **kwargs)' in error_message:
            error_message = error_message.split('self.cog, ctx, **kwargs)\n\n')[1]

        embed_general = discord.Embed(
            title=config.lang('error-title'),
            description=f'{config.lang("error-tip")}\n**`{type(error)}`**\n`{error}`\n\n```py\n{error_message[:1900]}```',
            color=management.color('error')
        )

        embed_additional = discord.Embed(
            title=config.lang('error-additional-title'),
            description=f'`{translate.auto(error, fix=True)}`',
            color=management.color('error')
        )
        embed_additional.set_footer(text=config.lang('error-additional-footer'))

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label=config.lang('error-view-url'), url=error_view_url, style=discord.ButtonStyle.url))
        print(error_view_url)

        try:
            await ctx.respond(content=error_view_url, embeds=[embed_general, embed_additional], view=view)
        except:
            await ctx.send(content=error_view_url, embeds=[embed_general, embed_additional], view=view)

        if management.testing_mode():
            raise error # if this is a testing system, show the full error in the console

def setup(client):
    client.add_cog(Errors(client))