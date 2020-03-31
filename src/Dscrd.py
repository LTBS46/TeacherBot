def is_command(string):
    return len(string) > 0 and string[0] == '$'

def token_split(string):
    rv = []
    list_brackets_args = ['"']
    spaces = ["\n","\t", " "]
    opened_bracket = True
    open_bracket = "$"
    arg = ""
    for c in string:
        if c in list_brackets_args:
            if opened_bracket:
                opened_bracket = False
                rv.append([arg, 'l'])
                arg = ""
            else:
                opened_bracket = True
                open_bracket = "\""
        if c in spaces:
            if open_bracket == "$":
                rv.append([arg, "t"])
                open_bracket = ""
                opened_bracket = False
                arg = ""
                open_bracket =""

        if opened_bracket and not c in list_brackets_args:
            arg+=c
    if opened_bracket and arg!= "":
        rv.append([arg,"t"])
        arg = ""
    print(rv)
    return rv
