import urllib as _url, json as _js, os as _os, enum as _en

class BaseEnum(_en.Enum):
    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)
#    def __new__(cls):
#        value = len(cls.__members__) + 1
#        obj = object.__new__(cls)
#        obj._value_ = value
#        return obj
    def _generate_next_value_(name, start, count, last_values):
        return name


@_en.unique
class Matiere(BaseEnum):
    MATHS = _en.auto()
    PHILO = _en.auto()
    HIST = _en.auto()
    GEO = _en.auto()
    SPE_MATHS = _en.auto()
    PHYSIQUE = _en.auto()
    SPE_PHYSIQUE = _en.auto()
    ISN = _en.auto()
    ANGLAIS_G1 = _en.auto()
    ANGLAIS_G2 = _en.auto()
    ESPAGNOL = _en.auto()
    ITALIEN = _en.auto()
    ALLEMAND = _en.auto()
    SI = _en.auto()
    PROJET = _en.auto()


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
        f = open("{2}{1}data{1}int{1}{0}".format(string,_os.sep,os.pardir), "r")
        rv = int(f.read(),10)
        f.close()
        f = open("{2}{1}data{1}int{1}{0}".format(string,_os.sep,os.pardir), "w")
        f.write(str(rv + 1))
    except IOError:
        f = open("{2}{1}data{1}int{1}{0}".format(string,_os.sep,os.pardir), "w")
        f.write('0')
    finally:
        f.close()
    return rv

def get_compteur_id(string):
    rv = -1
    try:
        f = open("{2}{1}data{1}int{1}{0}".format(string,_os.sep,os.pardir), "r")
        rv = int(f.read(),10)
    finally:
        f.close()
    return rv

def get_token():
    rv = None
    try:
        f = open("{0}{1}data{1}settings.json".format(_os.pardir,_os.sep),"r")
        str = f.read()
        obj = _js.loads(str)
        rv = obj["token"]["discord"]
    except IOError:
        print("file not found or can't be read")
    finally:
        f.close()
    return rv

def get_master_guild():
    rv = None
    try:
        f = open("{0}{1}data{1}settings.json".format(_os.pardir,_os.sep),"r")
        str = f.read()
        obj = _js.loads(str)
        rv = obj["main_guild"]
    except IOError:
        print("file not found or can't be read")
    finally:
        f.close()
    return rv

def get_master_channel():
    rv = None
    try:
        f = open("{0}{1}data{1}settings.json".format(_os.pardir,_os.sep),"r")
        str = f.read()
        obj = _js.loads(str)
        rv = obj["main_channel"]
    except IOError:
        print("file not found or can't be read")
    finally:
        f.close()
    return rv

del _url, _js, _os, _en
