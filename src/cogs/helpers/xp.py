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

def of(user):
    user = user_to_id(user)
    xp_value = 0

    if config.load('xp').get(user):
        xp_value = config.load('xp').get(user)
    
    return xp_value

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
    print(config.load('ranks').keys())
    rank_list = list(config.load('ranks').keys()).reverse()

    for rank in rank_list:
        if level_of(user) > rank:
            asyncio.run_until_complete(give_rank(user, rank))
            break

def user_to_id(user):
    if isinstance(user, discord.Member) or isinstance(user, discord.User):
        return user.id

    if isinstance(user, str):
        return int(user)

    return user

def add(user: discord.Member, value: int):
    config.change('xp', user_to_id(user), value)
    on_add(user, value)
