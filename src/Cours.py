import os as _os
import re as _re

class Cours():

    def __init__(self):
        self.donnees = {}

    async def save(self, matiere, nom, list_fic):
        path_matiere = "_".join(matiere.upper().split("-"))
        if len(list_fic)>1:
            for i in range(len(list_fic)):
                path_dirs = f"{_os.pardir}{_os.sep}data{_os.sep}{path_matiere}{_os.sep}{nom}"
                if not _os.path.exists(path_dirs):
                    _os.makedirs(path_dirs)
                await list_fic[i].save(f"{_os.pardir}{_os.sep}data{_os.sep}{path_matiere}{_os.sep}{nom}{_os.sep}{list_fic[i].filename}")
        else:
            path_dirs = f"{_os.pardir}{_os.sep}data{_os.sep}{path_matiere}"
            if not _os.path.exists(path_dirs):
                _os.makedirs(path_dirs)
            for i in range(len(list_fic)):
                await list_fic[i].save(f"{_os.pardir}{_os.sep}data{_os.sep}{path_matiere}{_os.sep}{list_fic[i].filename}")

    def load(self, matiere, nom):
        path_matiere = f"{_os.pardir}{_os.sep}data{_os.sep}{matiere}"
        path_folder = f"{_os.pardir}{_os.sep}data{_os.sep}{matiere}{_os.sep}{nom}"
        path_file = r(f"{_os.pardir}{_os.sep}data{_os.sep}{matiere}{_os.sep}{nom}.\w")
        potential_file_name = r(f"{nom}.\w")

        if not matiere in self.donnees:
            self.donnees[matiere] = {}
        try:
            for pathdirs,dirs, files in _os.walk(path_folder):
                if pathdirs == nom:
                    self.donnees[matiere][nom] = files

        except Exception as e:
            for pathdirs,dirs, files in _os.walk(path_matiere):
                for i in range(len(files)):
                    if _re.match(potential_file_name, files[i]):
                        self.donnees[matiere][nom] = files[i]
                        break
        return self.donnees[matiere][nom]


    def load_all(self):
        pass
    def save_all(self):
        pass
