class StatusArg:
    def __init__(self):
        self.test = False

import sys, common as _c
def parsearg(globvar):
    globvar['status'] = StatusArg();
    for arg in sys.argv:
        if arg == '-t':
            globvar()['status'].test = True
        else:
            print("unknown argument : " + arg)
    return None

del _c
