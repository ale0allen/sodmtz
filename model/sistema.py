from openpyxl import Workbook, load_workbook
from collections import OrderedDict
import os

diretorio_atual = os.getcwd()
diretorio_pai = os.path.dirname(diretorio_atual)
diretorio_pai = diretorio_pai + '\\planilhas'

# construir um caminho relativo para um arquivo no diretório atual
caminho_rel = os.path.join(diretorio_pai, "Sistemas.xlsx")
filename = caminho_rel

class Sistema:
    def __init__(self, codigo=None, nome=None):
        if codigo is None:
            self.codigo = ""
        else:
            self.codigo = codigo
        if nome is None:
            self.nome = ""
        else:
            self.nome = nome

