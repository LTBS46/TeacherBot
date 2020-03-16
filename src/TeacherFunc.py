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
async def arbitrary_exec(b, message, token_s):
    rv = None
    try:
        rv = eval(''.join([c[0]for c in token_s[1:]]))
    except Exception as e:
        message.channel.send(str(e))
    message.channel.send(str(rv))

@commwrap
async def __(b, message, token_s):await message.channel.send('unknown command : {0}'.format(message.content))

@helpwrap
async def ___h(b, message, token_s):await message.channel.send('help about error')

@commwrap
async def _print(b, message, token_s):print(''.join([c[0]for c in token_s[1:]]));await message.channel.send(''.join([c[0]for c in token_s[1:]]))

@helpwrap
async def _print_h(b, message, token_s):await message.channel.send('help about print')

@commwrap
async def change_cours(b, message, token_s):pass

@helpwrap
async def change_cours_h(b, message, token_s):await message.channel.send('help about change_cours')

@commwrap
async def change_dev(b, message, token_s):pass

@helpwrap
async def change_dev_h(b, message, token_s):await message.channel.send('help about change_dev')

@commwrap
async def del_cours(b, message, token_s):pass

@helpwrap
async def del_cours_h(b, message, token_s):await message.channel.send('help about del_cours')

@commwrap
async def del_dev(b, message, token_s):pass

@helpwrap
async def del_dev_h(b, message, token_s):await message.channel.send('help about del_dev')

@commwrap
async def get_cours(b, message, token_s):pass

@helpwrap
async def get_cours_h(b, message, token_s):await message.channel.send('help about get_cours')

@commwrap
async def get_dev(b, message, token_s):pass

@helpwrap
async def get_dev_h(b, message, token_s):await message.channel.send('help about get_dev')

@commwrap
async def echo(b, message, token_s):await message.channel.send(token_s[1][0])

@helpwrap
async def echo_h(b, message, token_s):await message.channel.send('help about echo')

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
async def help_h(b, message, token_s):await message.channel.send('help about help')

@commwrap
async def new_dev(b, message, token_s):pass

@helpwrap
async def new_dev_h(b, message, token_s):await message.channel.send('help about new_dev')

@commwrap
async def new_cours(b, message, token_s):b.courshandler.save(token_s[1][0].upper().split('-').join('_'), token_s[2][0], message.attachments)
    #récup les fichiers du message et les enregistrer au bon endroit
    #matiere = token_s[1][0].upper().split('-').join('_') le premier argument correspond à l'enum matière de common.py
    #nom = token_s[2][0]
    #content = message.attachments

@helpwrap
async def new_cours_h(b, message, token_s):pass

@commwrap
async def ping(b, message, token_s):await message.channel.send('pong')

@helpwrap
async def ping_h(b, message, token_s):await message.channel.send('help about ping')

if __name__ == '__main__':
    import Debug
    print(commdict)
    print(helphandler)
