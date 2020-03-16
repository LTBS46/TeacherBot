from Cours import *


commdict = {}
helphandler = {}

def namef(name):
    to_split = False
    if name[-2:] == '_h':
        name = name[:-2]
    while name[0] == '_':
        if len(name) == 1:
            return ''
        name = name[1:]
    for i in range(len(name)):
        if name[i] == '_':
            to_split = True
    if to_split:
        array = name.split("_")
        name = "-".join(array)
    return name

def helpwrap(func):
    helphandler[namef(func.__name__)] = func
    if __name__ == "__main__":
        print("reach helper : %s" % namef(func.__name__))
    return func

def commwrap(func):
    commdict[namef(func.__name__)] = func
    if __name__ == "__main__":
        print("reach : %s" % namef(func.__name__))
    return func

@commwrap
async def __(b, message):await message.channel.send('unknown command : {0}'.format(message.content))

@helpwrap
async def ___h(b, message, token_s):pass

@commwrap
async def _print(b, message, token_s):await message.channel.send(''.join([c[0]for c in token_s[1:]]))

@helpwrap
async def _print_h(b, message, token_s):pass

@commwrap
async def change_cours(b, message, token_s):pass

@helpwrap
async def change_cours_h(b, message, token_s):pass

@commwrap
async def change_dev(b, message, token_s):pass


@helpwrap
async def change_dev_h(b, message, token_s):pass

@commwrap
async def del_cours(b, message, token_s):pass

@helpwrap
async def del_cours_h(b, message, token_s):pass

@commwrap
async def del_dev(b, message, token_s):pass

@helpwrap
async def del_dev_h(b, message, token_s):pass

@commwrap
async def get_cours(b, message, token_s):pass

@helpwrap
async def get_cours_h(b, message, token_s):pass

@commwrap
async def get_dev(b, message, token_s):pass

@helpwrap
async def get_dev_h(b, message, token_s):pass

@commwrap
async def echo(b, message, token_s):await message.channel.send(token_s[1][0])

@helpwrap
async def echo_h(b, message, token_s):await message.channel.send(message.content[5:])

@commwrap
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

@helpwrap
async def help_h(b, message, token_s):pass

@commwrap
async def new_dev(b, message, token_s):
    matiere = token_s[1][0]
    nom = token_s[2][0]
    contenu = token_s[3][0]
    b.Devoirs_obj.save(matiere, nom, contenu)

@helpwrap
async def new_dev_h(b, message, token_s):pass

@commwrap
async def new_cours(b, message, token_s):
    #récup les fichiers du message et les enregistrer au bon endroit
    matiere = token_s[0][0]
    nom = token_s[1][0]
    content = message.attachments

    b.Cours_obj.save(matiere, nom, content)

@helpwrap
async def new_cours_h(b, message, token_s):pass

@commwrap
async def ping(b, message, token_s):await message.channel.send('pong')

@helpwrap
async def ping_h(b, message, token_s):await message.channel.send('pong')

if __name__ == '__main__':
    print(commdict)
    print(helphandler)
