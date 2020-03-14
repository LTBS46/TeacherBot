import discord, Discord as _D, common as _c, TeacherFunc as Do
from discord.ext import commands
class Teacher(discord.Client)
    def __init__(self, devoirhandler):
        super().__init__(self)
        self.devoirhandler = devoirhandler
        await self.change_presence(status = discord.Status.idle, activity = discord.Game("Trying to be a working bot"))


    @self.event()
    async def on_ready(self):
        g = await get_guild(_c.get_master_guild())
        c = await g.get_channel(_c.get_master_channel())
        await c.trigger_typing()
        await c.send('logged as {0}'.format(self.user))
        print('logged as {0}'.format(self.user))

    @self.event()
    async def on_message(self, message):
        if (message.author == self.user):
            return
        elif _D.is_command(message.content):
            token_s = _D.token_split(message.content[1:])
            try:
                Do.commdict[token_s[0][0]](self, message, token_s)
            except KeyError:
                Do.__(self, message, token_s)


del discord, commands, _D, Do, _c
