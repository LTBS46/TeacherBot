def is_command(string):
    return string[0]=='$'

def token_split(string):
    rv = []
    char_s = ''
    breaktime = 0
    literal = False
    for c in string:
        if breaktime :
            breaktime -= 1
            continue
        elif literal:
            char_s += c
        elif c == '\n':
            rv.append(char_s)
        elif c == '\t':
            rv.append(char_s)
        elif c == ' ':
            rv.append(char_s)
        else:
            char_s += c
    rv.append(char_s)
    return rv
