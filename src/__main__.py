import sys

def parsearg():
    globals()['status'] = {"test":False};
    for arg in sys.argv:
        if arg == '-t':
            globals()['status']["test"] = True
        else:
            print("unknown argument : " + arg)
    return None

def main():
    parsearg()
    return None

if __name__ == '__main__':
    main()
    exit(0)
