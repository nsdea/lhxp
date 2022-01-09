try:
    from . import config, management
except ImportError:
    import config, management

import sys
import math
import discord
import asyncio

sys.path.append('..') # https://stackoverflow.com/a/11096846

try:
    from bot import give_rank
except:
    print('Warning » helpers/xp Couldn\'t import bot')

client = None

def xp_to_level(x: int) -> int:
    return eval(config.load()['level-formula'])

def level_to_xp(x: int) -> int:
    return eval(config.load()['xp-formula'])

def set_client(c):
    global client
    client = c 

def of(user):
    user = management.user_to_id(user)
    xp_value = 0

    if config.load('xp').get(user):
        xp_value = config.load('xp').get(user)
    
    return round(xp_value, 1)

def level_of(user):
    user = management.user_to_id(user)
    xp_value = 0

    if config.load('xp').get(user):
        xp_value = config.load('xp').get(user)
    
    return xp_to_level(xp_value)

def needed_for_level(user):
    return level_to_xp(level_of(user))

def needed_for_next_level(user):
    return level_to_xp(level_of(user)+1)

def on_add(user: discord.Member, xp_change):
    global client

    rank_list = list(config.load('ranks').keys())[1:]
    rank_list.reverse()

    for rank in rank_list:
        if level_of(user) > rank:
            client.loop.create_task(give_rank(user, rank))
            break

def add(user, value: int):
    config.change('xp', management.user_to_id(user), value)
    on_add(user, value)

    if of(user) < 0:
        config.set('xp', management.user_to_id(user), 0)

if __name__ == '__main__':
    print(xp_to_level(123))
    print(level_to_xp(123))