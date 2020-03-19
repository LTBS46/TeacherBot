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
            print("unknown argument : {0}".format(arg))
    return None
