def ping(b, message, token_s):
    await message.channel.trigger_typing()
    await message.channel.send('pong')

def _print(b, message, token_s):
    await message.channel.trigger_typing()
    str = ''
    for c in token_s[1:]:
        str += c[0]
    await message.channel.send(str)

def echo(b, message, token_s):
    await message.channel.trigger_typing()
    await message.channel.send(message.content[5:])

def new_dev(b, message, token_s):
    pass

def get_dev(b, message, token_s):
    pass

def del_dev(b, message, token_s):
    pass

def change_dev(b, message, token_s):
    pass

def new_cours(b, message, token_s):
    pass

def get_cours(b, message, token_s):
    pass

def del_cours(b, message, token_s):
    pass

def change_cours(b, message, token_s):
    pass

def __(b, message, token_s):
    await message.channel.trigger_typing()
    await message.channel.send('unknown command : {0}'.format(message.content))

commdict = {
    'ping':ping,
    'print':_print,
    'echo':echo,
    'new-dev':new_dev,
    'change-dev':change_dev,
    'del-dev':del_dev,
    'get-dev':get_dev,
    'new-cours':new_cours,
    'change-cours':change_cours,
    'del-cours':del_cours,
    'get-cours':get_cours,
}
