def __(b, message, token_s):await message.channel.send('unknown command : {0}'.format(message.content))

def ___h(b, message, token_s):pass

def _print(b, message, token_s):await message.channel.send(''.join([c[0]for c in token_s[1:]]))

def _print_h(b, message, token_s):pass

def change_cours(b, message, token_s):pass

def change_cours_h(b, message, token_s):pass

def change_dev_h(b, message, token_s):pass

def change_dev_h(b, message, token_s):pass

def del_cours(b, message, token_s):pass

def del_cours_h(b, message, token_s):pass

def del_dev(b, message, token_s):pass

def del_dev_h(b, message, token_s):pass

def get_cours_h(b, message, token_s):pass

def get_cours(b, message, token_s):pass

def get_dev_h(b, message, token_s):pass

def get_dev_h(b, message, token_s):pass

def echo(b, message, token_s):await message.channel.send(message.content[5:])

def echo_h(b, message, token_s):await message.channel.send(message.content[5:])

def help(b, message, token_s):pass

def help_h(b, message, token_s):pass

def new_dev(b, message, token_s):pass

def new_dev_h(b, message, token_s):pass

def new_cours(b, message, token_s):pass

def new_cours_h(b, message, token_s):pass

def ping(b, message, token_s):await message.channel.send('pong')

def ping_h(b, message, token_s):await message.channel.send('pong')


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

helphandler = {
    'change-dev':change_dev_h,
    'change-cours':change_cours_h,
    'del-cours':del_cours_h,
    'del-dev':del_dev_h,
    'echo':echo_h,
    'help':help_h,
    'get-cours':get_cours_h,
    'get-dev':get_dev_h,
    'new-cours':new_cours_h,
    'new-dev':new_dev_h,
    'ping':ping_h,
    'print':_print_h,
}
