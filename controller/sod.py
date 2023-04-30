from openpyxl import Workbook, load_workbook
from collections import OrderedDict
import os

diretorio_atual = os.getcwd()
diretorio_pai = os.path.dirname(diretorio_atual)
diretorio_pai = diretorio_pai + '\\planilhas'

# construir um caminho relativo para um arquivo no diretório atual
caminho_rel = os.path.join(diretorio_pai, "MatrizSod.xlsx")
filename = caminho_rel


wb = load_workbook(filename=filename)
ws = wb.active


from model.sod import Sod


class sodController:

    def __init__(self, codigo=None, codigo_perfil1=None, nome_perfil1=None, sistema_perfil1=None,
                 codigo_perfil2=None, nome_perfil2=None, sistema_perfil2=None):
        self.codigo = codigo
        self.codigo_perfil1 = codigo_perfil1
        self.nome_perfil1 = nome_perfil1
        self.sistema_perfil1 = sistema_perfil1
        self.codigo_perfil2 = codigo_perfil2
        self.nome_perfil2 = nome_perfil2
        self.sistema_perfil2 = sistema_perfil2
        print('obj criado')

    def set_sod(self):
        codigo_perfil1 = self.codigo_perfil1
        nome_perfil1 = self.nome_perfil1
        sistema_perfil1 = self.sistema_perfil1
        codigo_perfil2 = self.codigo_perfil2
        nome_perfil2 = self.nome_perfil2
        sistema_perfil2 = self.sistema_perfil2

        proxima_linha = ws.max_row + 1
        ws.cell(row=proxima_linha, column=1).value = proxima_linha
        ws.cell(row=proxima_linha, column=2).value = codigo_perfil1
        ws.cell(row=proxima_linha, column=3).value = nome_perfil1
        ws.cell(row=proxima_linha, column=4).value = sistema_perfil1
        ws.cell(row=proxima_linha, column=5).value = codigo_perfil2
        ws.cell(row=proxima_linha, column=6).value = nome_perfil2
        ws.cell(row=proxima_linha, column=7).value = sistema_perfil2
        wb.save(filename=filename)

    def __str__(self):
        return f'Nome1: {self.nome_perfil1}'