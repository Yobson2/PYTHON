from os import *

def siezeFile(filename):
    file_info=path.getsize(filename)
    if not path.exists(filename):
        return print('fichier introuvable')
    else:
     return file_info*1024

# print(siezeFile('C:\\Users\\Yoboue_Louis\\Desktop\\Realisation_mois'))

