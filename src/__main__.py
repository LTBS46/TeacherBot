import sys

def parsearg():
    globals()['status'] = {"test":False};
    for arg in sys.argv:
        if arg == '-t':
            globals()['status']["test"] = True
        else:
            print("unknown argument : " + arg)

def main():
    parsearg()

if __name__ == '__main__':
    main()
