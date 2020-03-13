import discord
from discord.ext import commands


Teacher = commands.Bot(command_prefix = '/')

@Teacher.event
async def on_ready();
    #load data
    pass

async def on_message();
    #on analyse les messages qu'ils nou envoie et on adapte en fonction
    pass
