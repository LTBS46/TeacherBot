from ArgParse import parsearg, StatusArg
import COVID19, common as c, Dscrd, Teacher as T, Devoirs as D, Cours as C

def main():
    parsearg(globals())
    if globals()['status'].test:
        pass
    client = T.Teacher(D.Devoirs(), C.Cours())
    client.run(c.get_token())
    return 0

if __name__ == '__main__':
    exit(main())
