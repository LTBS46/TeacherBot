import sys
import common as _c


class StatusArg:
    def __init__(self):
        self.test = False


def parsearg(globvar):
    globvar['status'] = StatusArg();
    for arg in sys.argv[1:]:
        if arg == '-t':
            globvar['status'].test = True
        else:
            print(f"unknown argument : {arg}")
    return None
