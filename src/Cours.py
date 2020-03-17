import os as _os
import re as _re
import discord

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

    def load(self, matiere, nom):
        path_matiere = "_".join(matiere.upper().split("-"))

        if not path_matiere in self.donnees:
            self.donnees[path_matiere] = {}

        for pathdirs,dirs, files in _os.walk(path_folder):
            if pathdirs == nom:
                self.donnees[path_matiere][nom] = files
                break
        files_l = []
        for i in self.donnees[path_matiere][nom]:
            path = f'{_os.pardir}{_os.sep}data{_os.sep}{path_matiere}{_os.sep}{i}'
            files_l.append(discord.File(path, i))
        return files_l

    def load_all(self):
        pass
    def save_all(self):
        pass
