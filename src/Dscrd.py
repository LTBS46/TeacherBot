def is_command(string):
    if len(string)>0:
        return string[0] == '$'
    else:
        return False

def token_split(string):
    rv = []
    char_s = ''
    breaktime = 0
    literal = 0
    for c in string:
        if breaktime :
            breaktime -= 1
        elif literal:
            if literal == 2 and c == "'":
                literal = 0
                rv.append([char_s, 'l'])
                char_s = ''
            elif literal == 1 and c == '"':
                literal = 1
                rv.append([char_s, 'l'])
                char_s = ''
            else:
                char_s += c

        elif c == '\n':
            rv.append([char_s, 't'])
            char_s = ''
        elif c == '\t':
            rv.append([char_s, 't'])
            char_s = ''
        elif c == ' ':
            rv.append([char_s, 't'])
            char_s = ''
        elif c == '"':
            literal = 1
            rv.append([char_s, 't'])
            char_s = ''
        elif c == "'":
            literal = 2
            rv.append([char_s, 't'])
            char_s = ''
        else:
            char_s += c

    rv.append([char_s, "l" if literal else "])
    return rv
