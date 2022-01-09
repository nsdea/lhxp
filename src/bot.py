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
import asyncio
import discord
import discord.commands

from datetime import datetime
from discord.ext import commands
from discord.commands import slash_command

from cogs.helpers import config, management, xp

# FUNCTIONS
async def give_rank(user: discord.Member, rank_level: int):
    rank_index = config.load('ranks')[0].index(user.guild.id)
    role = user.guild.get_role(config.load('ranks')[rank_level][rank_index])

    if role in user.roles:
        return

    await user.add_roles(role, reason=config.lang('rank-reason'))

    for channel in config.load()['rank-message-channels']:
        if channel in [c.id for c in user.guild.text_channels]:
            await user.guild.get_channel(channel).send(embed=discord.Embed(title=config.lang('rank-dm-title', {'user': str(user)}), description=config.lang('rank-dm-description', {'role': role.mention}), color=management.color()))

def main():
    print(f'{colorama.Fore.BLUE}INFO » Main starting...')

    # SETUP
    dotenv.load_dotenv()  # initialize virtual environment
    token = os.getenv('DISCORD_TOKEN')
    client = commands.Bot(command_prefix=commands.when_mentioned, intents=discord.Intents.all())
    xp.set_client(client)

    async def status_task():
        await client.change_presence(
            activity=discord.Game(name=config.load()['playing']),
            status=discord.Status.idle if management.testing_mode() else discord.Status.dnd
        )
        print(f'{colorama.Fore.BLUE}INFO » Playing', discord.Status.idle if management.testing_mode() else discord.Status.streaming + config.load()['playing'])

    async def monthly_reset(): 
        while True:
            if not config.load('times').get('xp-reset'):
                config.set('times', 'xp-reset', (time.time()//2629800)*2629800) # beginning of the current month

            if time.time() - config.load('times')['xp-reset'] > 2629800: # 1 month since last reset
                for f in config.load()['monthly-reset']:
                    config.save(f, {}) # reset

                config.set('times', 'xp-reset', (time.time()//2629800)*2629800) # beginning of the current month

            await asyncio.sleep(60)

    @client.event
    async def on_ready():
        management.set_start_time()

        print(f'{colorama.Fore.GREEN}SUCCESS »', f'Online: {client.user}')

        client.loop.create_task(status_task())
        client.loop.create_task(monthly_reset())

    # Extensions
    extensions_loaded = []

    for filename in os.listdir(os.getcwd() + '/src/cogs/'):
        if filename.endswith('.py'):
            cog_name = filename.split(".")[0]
            extensions_loaded.append(cog_name)
            client.load_extension(f'cogs.{cog_name}') # cogs.filename

            print(f'{colorama.Fore.GREEN}SUCCESS »', f'Loaded extension {cog_name}')

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
        print(f'{colorama.Fore.RED}FATAL »', f'Unable to run the client. Please check your bot token and your internet connection.\nError: {e}')

if __name__ == '__main__':
    main()