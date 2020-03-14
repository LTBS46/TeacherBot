#{ "maths":{"nom devoir 1":"à faire", "nom devoir 2":"à faire"},
# "francais":....,
#}
import _os

class Devoirs():
    def __init__(self):
        self.donnees = {}

    def save(self,matiere, nom, content):
            path_dir = "Data/" + matiere
            path = "{0}{1}data{1}{2}{1}{3}.txt".format(_os.pardir, _os.sep, matiere, nom)
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

    def load(self,nom,matiere = None):
        path = "{0}{1}data{1}{2}{1}{3}.txt".format(_os.pardir, _os.sep, matiere, nom)
#        path = _os.pardir + _os.sep + "data" + _os.sep + matiere + _os.sep + nom + ".txt"
        if not matiere in self.donnees:
            self.donnees[matiere] = {}
        try:
            f = open(path, "r")
            self.donnees[matiere][nom] = f.read()
        finally:
            f.close()
        return self.donnees[matiere][nom]

    def load_all(self):
        path = "../data"
        for pathdirs, dirs, files in os.walk(path):
            if pathdirs != "../data":
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

C = Devoirs()

del _os
