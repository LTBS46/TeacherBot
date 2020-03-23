import os as _os
import re as _re
import discord
import shutil

class Cours():

    def __init__(self):
        self.donnees = {}

    async def save(self, matiere, nom, list_fic):
        path_matiere = "_".join(matiere.upper().split("-"))
        for i in range(len(list_fic)):
            path_dirs = f"{_os.pardir}{_os.sep}data{_os.sep}{path_matiere}{_os.sep}{nom}"
            if not _os.path.exists(path_dirs):
                _os.makedirs(path_dirs)
            await list_fic[i].save(f"{_os.pardir}{_os.sep}data{_os.sep}{path_matiere}{_os.sep}{nom}{_os.sep}{list_fic[i].filename}")

    def load(self, matiere, nom=None):
        path_matiere = "_".join(matiere.upper().split("-"))
        path_folder = f'{_os.pardir}{_os.sep}data{_os.sep}{path_matiere}{_os.sep}{nom}'
        if nom != None:
            try:



                if not path_matiere in self.donnees:
                    self.donnees[path_matiere] = {}

                for pathdirs,dirs, files in _os.walk(path_folder):
                    if pathdirs == path_folder:
                        self.donnees[path_matiere][nom] = files

                files_l = []
                for i in self.donnees[path_matiere][nom]:
                    path = f'{_os.pardir}{_os.sep}data{_os.sep}{path_matiere}{_os.sep}{nom}{_os.sep}{i}'
                    files_l.append(discord.File(path, i))

                return files_l
            except Exception as e:
                return False
        else:
            to_return = []
            try:
                for pathdirs,dirs, files in _os.walk(f'{_os.pardir}{_os.sep}data{_os.sep}{path_matiere}'):
                    if pathdirs == f'{_os.pardir}{_os.sep}data{_os.sep}{path_matiere}':
                        to_return = dirs
                return to_return
            except Exception as e:
                return False

    def delete(self, matiere, nom, fichier = None):
        try:
            if fichier == None:
                path = "{0}{1}data{1}{2}".format(_os.pardir, _os.sep, matiere)
                for pathdirs, dirs, files in _os.walk(path):
                    if nom in dirs:
                        pass
                        shutil.rmtree(path+_os.sep+nom)
            else:
                path = "{0}{1}data{1}{2}{1}{3}{1}{4}".format(_os.pardir, _os.sep, matiere, nom, fichier)
                _os.remove(path)
            return True
        except Exception as e:
            return False


    def load_all(self):
        pass
    def save_all(self):
        pass
