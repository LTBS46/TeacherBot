#{ "maths":{"nom devoir 1":"à faire", "nom devoir 2":"à faire"},
# "francais":....,
#}
import os as _os

class Devoirs():
    def __init__(self):
        self.donnees = {}

    def save(self, matiere, nom, content):
            path_dir = "{0}{1}data{1}{2}".format(_os.pardir, _os.sep, matiere)
            path = "{0}{1}data{1}{2}{1}{3}.dev".format(_os.pardir, _os.sep, matiere, nom)
            if not matiere in self.donnees:
                self.donnees[matiere] = {}
            if not _os.path.exists(path_dir):
                _os.makedirs(path_dir)
            try:
                f = open(path, "w")
                f.write(content)
            finally:
                f.close()
            self.donnees[matiere][nom] = content

    def save_all(self):
        for mat in self.donnees.keys():
            for dev in self.donnees[mat].keys():
                self.save(mat, dev, self.donnees[mat][dev])

    def load(self, nom, matiere = None):
        path = "{0}{1}data{1}{2}{1}{3}.dev".format(_os.pardir, _os.sep, matiere, nom)
        if not matiere in self.donnees:
            self.donnees[matiere] = {}
        try:
            f = open(path, "r")
            self.donnees[matiere][nom] = f.read()
        finally:
            f.close()
        return self.donnees[matiere][nom]

    def load_all(self):
        path = "{0}{1}data".format(_os.pardir,_os.sep)
        for pathdirs, dirs, files in _os.walk(path):
            if pathdirs != path:
                for i in files:
                    matiere = pathdirs.split(_os.sep)[1]
                    path_f = pathdirs + _os.sep + i
                    nom = i.split(".")[0]
                    try:
                        f = open(path_f, "r")
                        self.donnees[matiere][nom] = f.read()
                    finally:
                        f.close()

            else:
                for i in dirs:
                    if not i in self.donnees:
                        self.donnees[i] = {}
        return self.donnees


del _os
