import discord, Discord as _D, common as _c
from discord.ext import commands
import TeacherFunc as Do
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
            if token_s[0][0] == 'ping':
                Do.ping(self, message, token_s)
            elif token_s[0][0] == 'print':
                Do._print(self, message, token_s)
            elif token_s[0][0] == 'echo':
                Do.echo(self, message, token_s)
            elif token_s[0][0] == 'new-dev':
                Do.new_dev(self, message, token_s)
            elif token_s[0][0] == 'change-dev':
                Do.change_dev(self, message, token_s)
            elif token_s[0][0] == 'del-dev':
                Do.del_dev(self, message, token_s)
            elif token_s[0][0] == 'get-dev':
                Do.get_dev(self, message, token_s)
            elif token_s[0][0] == 'new-cours':
                Do.new_cours(self, message, token_s)
            elif token_s[0][0] == 'change-cours':
                Do.change_cours(self, message, token_s)
            elif token_s[0][0] == 'del-cours':
                Do.del_cours(self, message, token_s)
            elif token_s[0][0] == 'get-cours':
                Do.get_cours(self, message, token_s)
            else:
                Do.__(self, message, token_s)


del discord, commands, _D, Do, _c
