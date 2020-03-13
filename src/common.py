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

del _url
