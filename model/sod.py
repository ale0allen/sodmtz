from openpyxl import Workbook, load_workbook
from collections import OrderedDict
import os

diretorio_atual = os.getcwd()
diretorio_pai = os.path.dirname(diretorio_atual)
diretorio_pai = diretorio_pai + '\\planilhas'

# construir um caminho relativo para um arquivo no diretório atual
caminho_rel = os.path.join(diretorio_pai, "MatrizSod.xlsx")
filename = caminho_rel

class Sod:
    def __init__(self, codigo=None, codigo_perfil1=None, nome_perfil1=None, sistema_perfil1=None,
                 codigo_perfil2=None, nome_perfil2=None, sistema_perfil2=None):

        if codigo is None:
            self.codigo = ""
        else:
            self.codigo = codigo

        if codigo_perfil1 is None:
            self.codigo_perfil1 = ""
        else:
            self.codigo_perfil1 = codigo_perfil1

        if nome_perfil1 is None:
            self.nome_perfil1 = ""
        else:
            self.nome_perfil1 = nome_perfil1

        if sistema_perfil1 is None:
            self.sistema_perfil1 = ""
        else:
            self.sistema_perfil1 = sistema_perfil1

        if codigo_perfil2 is None:
            self.codigo_perfil2 = ""
        else:
            self.codigo_perfil2 = codigo_perfil2
        if nome_perfil2 is None:
            self.nome_perfil2 = ""
        else:
            self.nome_perfil2 = nome_perfil2

        if sistema_perfil2 is None:
            self.sistema_perfil2 = ""
        else:
            self.sistema_perfil2 = sistema_perfil2



