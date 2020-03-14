def __(b, message, token_s):
    await message.channel.trigger_typing()
    await message.channel.send('unknown command : {0}'.format(message.content))

def _print(b, message, token_s):
    await message.channel.trigger_typing()
    str = ''
    for c in token_s[1:]:
        str += c[0]
    await message.channel.send(str)

def change_cours(b, message, token_s):pass

def change_dev(b, message, token_s):pass

def del_cours(b, message, token_s):pass

def del_dev(b, message, token_s):pass

def get_cours(b, message, token_s):pass

def get_dev(b, message, token_s):pass

def echo(b, message, token_s):
    await message.channel.trigger_typing()
    await message.channel.send(message.content[5:])

def help(b, message, token_s):pass

def new_dev(b, message, token_s):pass

def new_cours(b, message, token_s):pass

def ping(b, message, token_s):
    await message.channel.trigger_typing()
    await message.channel.send('pong')


commdict = {
    'change-dev':change_dev,
    'change-cours':change_cours,
    'del-cours':del_cours,
    'del-dev':del_dev,
    'echo':echo,
    'help':help,
    'get-cours':get_cours,
    'get-dev':get_dev,
    'new-cours':new_cours,
    'new-dev':new_dev,
    'ping':ping,
    'print':_print,
}
