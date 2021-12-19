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

print(f'{colorama.Fore.BLUE}INFO »', f'Imported colorama and gevent')

import os
import dotenv
import discord
import discord.commands

# IMPORTS
from discord.ext import commands
from cogs.helpers import config, management

# SETTINGS
COLOR = config.load()['color-primary']
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

for filename in os.listdir(os.getcwd() + '/src/cogs/'): # load cogs/extensions
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename.split(".")[0]}')
        print(f'{colorama.Fore.GREEN}SUCCESS »', f'Loaded extension {filename.split(".")[0]}')

try:
    client.run(token)
except:
    print(f'{colorama.Fore.RED}FATAL »', 'Unable to run the client. Please check your bot token.')
