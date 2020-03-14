import discord, Discord as _D, common as _c, TeacherFunc as Do
from discord.ext import commands

def get_role_member(payload):
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id , client.guilds)
    emoji_name = payload.emoji.name
    try:
        role = discord.utils.get(guild.roles , name=emoji_name)
        member = discord.utils.find(lambda m : m.id == payload.user_id , guild.members)
        return role,member,emoji_name
    except:
        pass


class Teacher(discord.Client)

    def __init__(self, devoirhandler):
        super().__init__(self)
        self.devoirhandler = devoirhandler
        await self.change_presence(status = discord.Status.idle, activity = discord.Game("Trying to be a working bot"))

    @self.event()
    async def on_raw_reaction_add(payload):
        if(payload.message_id == 688342534988365825):
            try:
                role,member,emoji_name = get_role_member(payload)
                await member.add_roles(role)
                cdc = ":white_check_mark: Tu as maintenant accès aux salons " + emoji_name + " , Bon travail !"
                await member.send(cdc)
            except:
                await member.send("Erreur lors de l'attribution du rôle , contacte un administrateur ( Raphaël PEYRE en priorité )")

    @self.event()
    async def on_raw_reaction_remove(payload):
        if(payload.message_id == 688342534988365825):
            try:
                role,member,emoji_name = get_role_member(payload)
                await member.remove_roles(role)
                cdc = ":x: Tu ne peux maintenant plus accèder aux salons " + emoji_name + " !"
                await member.send(cdc)
            except:
                pass

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
            await message.channel.trigger_typing()
            token_s = _D.token_split(message.content[1:])
            try:
                Do.commdict[token_s[0][0]](self, message, token_s)
            except KeyError:
                Do.__(self, message, token_s)


del discord, commands, _D, Do, _c
