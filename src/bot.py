# IMPORT MANAGEMENT
try:
    import gevent.monkey
except ModuleNotFoundError: # detects that something's wrong with packages
    import os
    os.system('pip3 install -r requirements.txt') # automatically fix package installation
    import gevent.monkey

gevent.monkey.patch_all()  # patch everything

import colorama

colorama.init(autoreset=True)

# IMPORTS
import os
import time
import dotenv
import discord
import discord.commands

from datetime import datetime
from discord.ext import commands
from discord.commands import slash_command

from cogs.helpers import config, management, xp

# FUNCTIONS
async def give_rank(user: discord.Member, rank_level: int):
    rank_index = config.load('ranks')[0].index(user.guild.id)
    role = config.load('ranks')[rank_level][rank_index]

    if role in user.roles:
        return

    await user.add_roles(role, reason=config.lang('rank-reason'))

def main():
    print(f'{colorama.Fore.BLUE}INFO » main() starting...')

    # SETTINGS
    COLOR = management.color()
    TESTING_MODE = management.testing_mode()
    PREFIX = '//'

    # SETUP
    dotenv.load_dotenv()  # initialize virtual environment
    token = os.getenv('DISCORD_TOKEN')
    client = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

    async def status_task():
        await client.change_presence(
            activity=discord.Game(name=config.load()['playing']),
            status=discord.Status.idle if management.testing_mode() else discord.Status.dnd
        )
        print(f'{colorama.Fore.BLUE}INFO » Playing', discord.Status.idle if management.testing_mode() else discord.Status.streaming + config.load()['playing'])

    @client.event
    async def on_ready():
        management.set_start_time()

        print(f'{colorama.Fore.GREEN}SUCCESS »', f'Online: {client.user}')

        client.loop.create_task(status_task())

    # Extensions
    extensions_loaded = []

    for filename in os.listdir(os.getcwd() + '/src/cogs/'):
        if filename.endswith('.py'):
            cog_name = filename.split(".")[0]
            extensions_loaded.append(cog_name)
            client.load_extension(f'cogs.{cog_name}') # cogs.filename

            print(f'{colorama.Fore.GREEN}SUCCESS »', f'Loaded extension {cog_name}')

    @slash_command(description=config.lang('reload-description'), guild_ids=[921468392026824745])
    async def reload(ctx, cog: discord.commands.Option(str, config.lang('user'), required=False, default='')):
        if not cog:
            cog_list_joiner = '» '
            return await ctx.respond(embed=discord.Embed(title=config.lang('reload-list-title'), description=f'{cog_list_joiner}{cog_list_joiner.join(extensions_loaded)}', color=management.color()))

        if not cog in extensions_loaded:
            return await ctx.respond(embed=discord.Embed(title=config.lang('error-reload'), color=management.color('warn')))

        client.reload_extension('cogs.' + cog) 

    # Backups

    config_dir = f'{os.getcwd()}/src/'
    config_files = os.listdir(config_dir)
    backed_up = []

    for filename in config_files:
        if filename.endswith('.yml'):
            open(f'{os.getcwd()}/backups/{filename}', 'w').write(open(config_dir + filename).read())
            backed_up.append(filename)
            print(f'{colorama.Fore.GREEN}SUCCESS »', f'Backed up {filename}')

    backup_list_joiner = "\n\t- "
    backup_info = \
    f"""This file was auto-generated!

Last automatic backup: {datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}
Backed up:{backup_list_joiner}{backup_list_joiner.join(backed_up)}

Backups are automatically created every time the bot base (bot.py) is started."""

    open(f'{os.getcwd()}/backups/_info.txt', 'w').write(backup_info)

    # Run

    try:
        print(f'{colorama.Fore.BLUE}INFO » Bot starting...')
        client.run(token)
    except Exception as e:
        print(f'{colorama.Fore.RED}FATAL »', 'Unable to run the client. Please check your bot token and your internet connection.\nError: {e}')

if __name__ == '__main__':
    main()