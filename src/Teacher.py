import discord, Discord as _D, common as _c
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
        await c.send('connecté comme {0}'.format(self.user))
        print('connecté comme {0}'.format(self.user))

    @self.event()
    async def on_message(self, message):
        if (message.author == self.user):
            return
        elif _D.is_command(message.content):
            token_s = _D.token_split(message.content[1:])
            if token_s[0][0] == 'ping':
                await message.channel.trigger_typing()
                await message.channel.send('pong')
            elif token_s[0][0] == 'print':
                await message.channel.trigger_typing()
                str = ''
                for c in token_s[1:]:
                    str += c[0]
                await message.channel.send(str)
            elif token_s[0][0] == 'nouveau-dev':
                pass
            elif token_s[0][0] == 'change-dev':
                pass
            elif token_s[0][0] == 'del-dev':
                pass
            elif token_s[0][0] == 'avoir-dev':
                pass
            elif token_s[0][0] == 'nouveau-cours':
                pass
            elif token_s[0][0] == 'change-cours':
                pass
            elif token_s[0][0] == 'suppr-cours':
                pass
            elif token_s[0][0] == 'avoir-cours':
                pass
            else:
                await message.channel.trigger_typing()
                await message.channel.send('je ne comprend pas la commande : {0}'.format(message.content))


del discord, commands, _D
