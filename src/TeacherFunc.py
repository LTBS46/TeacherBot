from Cours import *

async def __(b, message, token_s):await message.channel.send('unknown command : {0}'.format(message.content))

async def ___h(b, message, token_s):pass

async def _print(b, message, token_s):await message.channel.send(''.join([c[0]for c in token_s[1:]]))

async def _print_h(b, message, token_s):pass

async def change_cours(b, message, token_s):pass

async def change_cours_h(b, message, token_s):pass

async def change_dev(b, message, token_s):pass

async def change_dev_h(b, message, token_s):pass

async def del_cours(b, message, token_s):pass

async def del_cours_h(b, message, token_s):pass

async def del_dev(b, message, token_s):pass

async def del_dev_h(b, message, token_s):pass

async def get_cours_h(b, message, token_s):pass

async def get_cours(b, message, token_s):pass

async def get_dev(b, message, token_s):pass

async def get_dev_h(b, message, token_s):pass

async def echo(b, message, token_s):await message.channel.send(message.content[5:])

async def echo_h(b, message, token_s):await message.channel.send(message.content[5:])

async def help(b, message, token_s):
    if len(token_s) == 2:
        try:
            helphandler[token_s[1][0]](b, message, token_s)
        except KeyError:
            pass
    elif len(token_s) == 1:
        #help normale
        pass
    else:
        #illegal argument number
        pass

async def help_h(b, message, token_s):pass

async def new_dev(b, message, token_s):pass

async def new_dev_h(b, message, token_s):pass

def new_cours(b, message, token_s):
    #récup les fichiers du message et les enregistrer au bon endroit
    matiere = token_s[0][0]
    nom = token_s[1][0]
    content = message.attachments

    Cours_obj.save(matiere, nom, content)

async def new_cours_h(b, message, token_s):pass

async def ping(b, message, token_s):await message.channel.send('pong')

async def ping_h(b, message, token_s):await message.channel.send('pong')


Cours_obj = Cours()

commdict = {
    'change-dev':change_dev,
    'change-cours':change_cours,
    'suppr-cours':del_cours,
    'suppr-dev':del_dev,
    'echo':echo,
    'aide':help,
    'avoir-cours':get_cours,
    'avoir-dev':get_dev,
    'nouveau-cours':new_cours,
    'nouveau-dev':new_dev,
    'ping':ping,
    'print':_print,
}

helphandler = {
    'change-dev':change_dev_h,
    'change-cours':change_cours_h,
    'suppr-cours':del_cours_h,
    'suppr-dev':del_dev_h,
    'echo':echo_h,
    'aide':help_h,
    'avoir-cours':get_cours_h,
    'avoir-dev':get_dev_h,
    'nouveau-cours':new_cours_h,
    'nouveau-dev':new_dev_h,
    'ping':ping_h,
    'print':_print_h,
}
