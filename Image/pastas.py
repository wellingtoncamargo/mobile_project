import os
import shutil
from time import sleep


def Copy_files(De: str, existe= False):

    destino = './Image/Baseline/'
    pastas = De.split('/', 2)
    pasta = pastas[-1].split('/')
    if not os.path.exists(destino + '/'.join(pasta[:-1])):
        os.makedirs(destino + '/'.join(pasta[:-1]), exist_ok=existe)
        shutil.copy2(De, destino + pastas[-1])
    # else:
    #     if not os.path.exists(destino + '/'.join(pasta[-1])):
    #         shutil.copy2(De, destino + pastas[-1])


def create_folder(arq):
    pasta = arq.split('/')
    if not os.path.exists('/'.join(pasta[:-1])):
        os.makedirs('/'.join(pasta[:-1]))


