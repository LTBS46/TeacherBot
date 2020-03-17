import discord
import Dscrd as _D
import common as _c
import TeacherFunc as Do
import os
from discord.ext import commands
from Cours import *
from Devoirs import *
import payloadhandler

class Teacher(discord.Client):

    def __init__(self, devoirhandler, courshandler):
        super(Teacher,self).__init__()
        self.devoirhandler = devoirhandler
        self.courshandler = courshandler
        #self.change_presence(status = discord.Status.idle, activity = discord.Game("Trying to be a working bot"))

    async def on_raw_reaction_add(payload):
        try:
            payloadhandler.payloadhandleadd[payload.message_id](self, payload)
        except KeyError:
            pass

    async def on_raw_reaction_remove(payload):
        try:
            payloadhandler.payloadhandlerem[payload.message_id](self, payload)
        except KeyError:
            pass

    async def on_ready(self):
#        tmp = {}
#        try:
#            tmp["f"] = open("{0}{1}data{1}settings.json".format(_os.pardir, _os.sep), "w")
#            tmp["f"].write(_c.get_widget_data())
#        finally:
#            tmp["f"].close()
        self.main_channel = self.get_channel(687940090454081601)
        await self.main_channel.trigger_typing()
        await self.main_channel.send(f'connecté comme {self.user}')
        print(f'connecté comme {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        elif _D.is_command(message.content):
            await message.channel.trigger_typing()
            try:
                token_s = _D.token_split(message.content[1:])
                token_v = [t[0] == '' and t[1] != 'l' for t in token_s]
                for i in range(len(token_v)):
                    if token_v[-i]:
                        del token_s[-i]
                await Do.commdict[token_s[0][0]](self, message, token_s)
            except KeyError:
                await Do.__(self, message)

    def get_role_member(self, payload):
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, self.guilds)
        emoji_name = payload.emoji.name
        try:
            role = discord.utils.get(guild.roles, name = emoji_name)
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            return role, member, emoji_name
        except:
            pass
