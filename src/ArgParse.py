import sys as _sys, common as _c

class StatusArg:
    def __init__(self):
        self.test = False

def parsearg(globvar):
    globvar['status'] = StatusArg();
    for arg in _sys.argv:
        if arg == '-t':
            globvar()['status'].test = True
        else:
            print("unknown argument : " + arg)
    return None

del _sys, _c
