import urllib.request as _urlr
import json as _js
import enum as _en
import errno as _err
import os as _os

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
    RUSSE = _en.auto()
    LATIN = _en.auto()
    LSF = _en.auto()
    MUSIQUE = _en.auto()
    CINEMA = _en.auto()

def get_string_from_url(url):
    str = ''
    tmp = {}
    try:
        tmp["f"] = _urlr.urlopen(url)
        str = tmp["f"].read()
    except Exception as e:
        print(e)
        print(f"cannot access : {url}")
    finally:
        tmp["f"].close()
    return str

def get_compteur_id(string):
    tmp = {}
    rv = 0
    try:
        tmp["f"] = open(f"{os.pardir}{_os.sep}data{_os.sep}int{_os.sep}{string}", "r")
        rv = int(tmp["f"].read(),10)
        tmp["f"].close()
        tmp["f"] = open(f"{os.pardir}{_os.sep}data{_os.sep}int{_os.sep}{string}", "w")
        tmp["f"].write(str(rv + 1))
    except OSError as e:
        tmp["f"] = open(f"{os.pardir}{_os.sep}data{_os.sep}int{_os.sep}{string}", "w")
        tmp["f"].write('0')
    finally:
        tmp["f"].close()
    return rv

def get_token():
    return "Njg4MTI2NzgyMjgwNjk1ODc0.Xmvy_A.uSb4OFRxpeaEEd80JdAu_Uq7tgs"

def get_master_guild():
    tmp = {}
    rv = None
    try:
        tmp["f"] = open((f"{_os.pardir}{_os.sep}data{_os.sep}setting.json"), "r")
        rv = _js.loads(tmp["f"].read())["id"]
    except OSError as e:
        print("file not found or can't be read")
    finally:
        tmp["f"].close()
    return rv

def get_master_channel():
    tmp = {}
    rv = None
    try:
        tmp["f"] = open(f"{_os.pardir}{_os.sep}data{_os.sep}setting.json", "r")
        rv = _js.loads(tmp["f"].read())["main_channel"]
    except OSError as e:
        print("file not found or can't be read")
    finally:
        tmp["f"].close()
    return rv

def get_widget_data():
    return _js.loads(get_string_from_url("http://discordapp.com/api/guilds/687779265093435420/widget.json"))
