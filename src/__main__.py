from ArgParse import parsearg, StatusArg
import COVID19, common as c, Dscrd, Teacher as T, Devoirs as D

def main():
    parsearg(globals())
    if globals()['status'].test:
        pass
    client = T.Teacher(D.Devoirs())
    client.run(c.get_token())
    return None

if __name__ == '__main__':
    main()
    exit(0)
