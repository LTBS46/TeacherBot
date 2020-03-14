from ArgParse import parsearg, StatusArg
import COVID19, common as c, Discord, Teacher as T

def main():
    parsearg(globals())
    client = T.Teacher()
    client.run(c.get_token())
    return None

if __name__ == '__main__':
    main()
    exit(0)
