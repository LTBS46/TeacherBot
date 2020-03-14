import discord
import Discord as _D
from discord.ext import commands

class Teacher(discord.Client)
    def __init__(self):
        super().__init__(self)
        await self.change_presence(status = discord.Status.idle, activity = discord.Game("Trying to be a working bot"))

    async def on_ready(self):
        print('logged as {0}'.format(self.user))

    async def on_message(self, message):
        if (message.author == self.user):
            return
        elif _D.is_command(message.content):
            token_s = _D.token_split(message.content[1:])
            if token_s[0] == 'ping':
                await message.channel.send('pong')
            else:
                await message.channel.send('unknown command : {0}'.format(message.content))

#    async def on_raw_reaction_add

#Teacher = commands.Bot(command_prefix = '$')
del discord, commands, _D
