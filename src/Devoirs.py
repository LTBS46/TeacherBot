#{ "maths":{"nom devoir 1":"à faire", "nom devoir 2":"à faire"},
# "francais":....,
#}
import os

class Devoirs():
    def __init__(self):
        self.donnees = {}

    def save(self,matiere, nom, content):
            path_dir = "Data/"+matiere
            path = "Data/"+matiere+"/"+nom+".txt"

            if not matiere in self.donnees:
                self.donnees[matiere] = {}
            if not os.path.exists(path_dir):
                os.makedirs(path_dir)

            with open(path, "w") as f:
                f.write(content)
                self.donnees[matiere][nom] = content

    def save_all(self):
        for mat in self.donnees.keys():
            for dev in self.donnees[mat].keys():
                self.save(mat, dev, self.donnees[mat][dev])

    def load(self,nom,matiere= None):
        path_dir = "Data/"+matiere
        path = "Data/"+matiere+"/"+nom+".txt"
        if not matiere in self.donnees:
            self.donnees[matiere] = {}
        if not os.path.exists(path_dir):
            return "path doesn't exist"

        with open(path, "r") as f:
            self.donnees[matiere][nom] = f.read()
        return self.donnees[matiere][nom]

    def load_all(self):
        path = "Data"
        for pathdirs, dirs, files in os.walk(path):
            if pathdirs != "Data":
                for i in files:
                    matiere = pathdirs.split("\\")[1]
                    path_f = pathdirs+"/"+i
                    nom = i.split(".")[0]
                    with open(path_f, "r") as f:
                        self.donnees[matiere][nom] = f.read()

            else:
                for i in dirs:
                    if not i in self.donnees:
                        self.donnees[i] = {}
        return self.donnees

C = Devoirs()


