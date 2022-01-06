try:
    from .helpers import config, management, xp
except ImportError:
    import helpers.config, helpers.management, helpers.xp

import time
import discord
import datetime

from discord.ext import commands

class InviteEvent(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def get_invite_dict(self, guild):
        invites_list = await guild.invites()
        invites_dict = {}

        for i in invites_list:
            actual_inviter = config.load('inviteowners').get(i.id)

            if actual_inviter and invites_dict.get(actual_inviter):
                invites_dict[actual_inviter] += i.uses
            else:
                invites_dict[actual_inviter] = i.uses
        
        if invites_dict[None]:
            invites_dict.pop(None)

        return invites_dict

    @commands.Cog.listener()
    async def on_member_join(self, member):
        old_dict = config.load('invites')
        new_dict = await self.get_invite_dict(guild=member.guild)
        if old_dict != new_dict:
            for inviter_id in list(new_dict.keys()):
                if old_dict.get(inviter_id) != new_dict.get(inviter_id):
                    config.save(filename='invites', source=new_dict)
                    config.set('invitedby', member.id, inviter_id)
                    inviter = member.guild.get_member(inviter_id)
                    xp.add(inviter, config.load()['invite-reward-xp'])

                    for channel in config.load()['welcome-channels']:
                        if channel in [c.id for c in member.guild.text_channels]:
                            embed = discord.Embed(title=config.lang('invited-title', {'user': str(member)}), description=config.lang('invited-description', {'inviter': inviter.mention, 'inviter_id': inviter.id, 'created': round(time.mktime(member.created_at.timetuple())), 'id': member.id}), color=management.color())
                            embed.set_thumbnail(url=member.avatar if member.avatar else member.default_avatar)
                        
                            await member.guild.get_channel(channel).send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if config.load('invitedby').get(member.id):
            xp.add(config.load('invitedby')[member.id], -1*config.load()['invite-reward-xp'])

def setup(client):
    client.add_cog(InviteEvent(client))