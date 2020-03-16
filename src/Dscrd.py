def is_command(string):
    return len(string) > 0 and string[0] == '$'

def token_split(string):
    rv = []
    char_s = ''
    literal = 0
    for c in string:
        if literal:
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
            if char_s != '':
                rv.append([char_s, 't'])
                char_s = ''
        elif c == '\t':
            if char_s != '':
                rv.append([char_s, 't'])
                char_s = ''
        elif c == ' ':
            if char_s != '':
                rv.append([char_s, 't'])
                char_s = ''
        elif c == '"':
            literal = 1
            if char_s != '':
                rv.append([char_s, 't'])
                char_s = ''
        elif c == "'":
            literal = 2
            if char_s != '':
                rv.append([char_s, 't'])
                char_s = ''
        else:
            char_s += c
    rv.append([char_s, "l" if literal else "t"])
    return rv
