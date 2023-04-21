from openpyxl import Workbook, load_workbook
from collections import OrderedDict
import os
filename = 'C:\\Users\\user\\estacio\\sodmtz\\controller\\Sistemas.xlsx'
wb = load_workbook(filename=filename)
ws = wb.active

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

