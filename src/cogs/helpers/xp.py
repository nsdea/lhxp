try:
    from . import config
except ImportError:
    import config

import sys
import math
import discord
import asyncio

sys.path.append('..') # https://stackoverflow.com/a/11096846

from bot import give_rank

client = None

def set_client(c):
    global client
    client = c 

def of(user):
    user = user_to_id(user)
    xp_value = 0

    if config.load('xp').get(user):
        xp_value = config.load('xp').get(user)
    
    return round(xp_value, 1)

def level_of(user):
    user = user_to_id(user)
    xp_value = 0

    if config.load('xp').get(user):
        xp_value = config.load('xp').get(user)
    
    return math.trunc(xp_value ** 0.5)

def needed_for_level(user):
    return (level_of(user))**2 

def needed_for_next_level(user):
    return (level_of(user)+1)**2

def on_add(user: discord.Member, xp_change):
    global client

    rank_list = list(config.load('ranks').keys())[1:]
    rank_list.reverse()

    for rank in rank_list:
        if level_of(user) > rank:
            client.loop.create_task(give_rank(user, rank))
            break

def user_to_id(user):
    if isinstance(user, discord.Member) or isinstance(user, discord.User):
        return user.id

    if isinstance(user, str):
        return int(user)

    return user

def add(user, value: int):
    config.change('xp', user_to_id(user), value)
    on_add(user, value)

    if of(user) < 0:
        config.set('xp', user_to_id(user), 0)