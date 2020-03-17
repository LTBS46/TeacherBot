from ArgParse import parsearg, StatusArg
import COVID19
import common as c
import Dscrd
import Teacher as T
import Devoirs as D
import Cours as C
import atexit

def main():
    parsearg(globals())
    if globals()['status'].test:
        pass
    globals()["client"] = T.Teacher(D.Devoirs(), C.Cours())
    @atexit.register
    def delclient():
        del client
    client.run(c.get_token())
    return 0

if __name__ == '__main__':
    exit(main())
