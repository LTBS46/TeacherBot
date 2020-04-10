from ArgParse import parsearg, StatusArg
import common as c
import Dscrd
import Teacher as T
import Devoirs as D
import Cours as C
import os
import atexit
os.path.dirname(os.path.realpath(__file__))

def main():
    parsearg(globals())
    if globals()['status'].test:
        if os.system('Teacher') != 10:
            return 10
    globals()["client"] = T.Teacher(D.Devoirs(), C.Cours())

    @atexit.register
    def delclient():
        del client
    client.run(c.get_token())
    return 0

if __name__ == '__main__':

    exit(main())
