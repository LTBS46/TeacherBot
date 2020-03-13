import urllib as _url

def get_string_from_url(url):
    str = ''
    try:
        f = _url.urlopen(url)
        str = f.read()
    except:
        print("cannot access : {0}".format(url))
    finally:
        f.close()
    return str

def get_new_compteur_id(string):
    rv = 0
    try:
        f = open("../data/int/{0}".format(string), "r")
        rv = int(f.read(),10)
        f.close()
        f = open("../data/int/{0}".format(string), "w")
        f.write(str(rv + 1))
    except IOError:
        f = open("../data/int/{0}".format(string), "w")
        f.write('0')
    finally:
        f.close()
    return rv

def get_compteur_id(string):
    rv = -1
    try:
        f = open("../data/int/{0}".format(string), "r")
        rv = int(f.read(),10)
    finally:
        f.close()
    return rv

del _url
