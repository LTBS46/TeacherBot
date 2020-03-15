from ArgParse import parsearg, StatusArg
import COVID19, common as c, Discord, Teacher as T, Devoirs as D

def main():
    parsearg(globals())
    if globals()['status'].test:
        pass
    client = T.Teacher(D.Devoir())
    client.run(c.get_token())
    return None

if __name__ == '__main__':
    main()
    exit(0)
