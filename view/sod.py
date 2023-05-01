import botao_adicionar
import botao_alterar
import botao_consultar
import botao_excluir
import botao_retornar

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QTableWidgetItem
import pandas as pd
from novo_sod import tela_novo_sod
from controller.sod import SodController
from geral_sod import geral_sod
import variaveis

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(791, 523)
        self.botao_adicionar = QtWidgets.QPushButton(Form)
        self.botao_adicionar.setGeometry(QtCore.QRect(0, 0, 91, 101))
        self.botao_adicionar.setStyleSheet("image: url(:/botao_adicionar/icones/adicionar.png)")
        self.botao_adicionar.setText("")
        self.botao_adicionar.setObjectName("botao_adicionar")
        self.botao_alterar = QtWidgets.QPushButton(Form)
        self.botao_alterar.setGeometry(QtCore.QRect(90, 0, 91, 101))
        self.botao_alterar.setStyleSheet("image: url(:/botao_alterar/icones/alterar.png)")
        self.botao_alterar.setText("")
        self.botao_alterar.setObjectName("botao_alterar")
        self.botao_consultar = QtWidgets.QPushButton(Form)
        self.botao_consultar.setGeometry(QtCore.QRect(180, 0, 91, 101))
        self.botao_consultar.setStyleSheet("image: url(:/botao_consultar/icones/consultar.png)")
        self.botao_consultar.setText("")
        self.botao_consultar.setObjectName("botao_consultar")
        self.botao_excluir = QtWidgets.QPushButton(Form)
        self.botao_excluir.setGeometry(QtCore.QRect(270, 0, 91, 101))
        self.botao_excluir.setStyleSheet("image: url(:/botao_excluir/icones/excluir.png)")
        self.botao_excluir.setText("")
        self.botao_excluir.setObjectName("botao_excluir")
        self.botao_retornar = QtWidgets.QPushButton(Form)
        self.botao_retornar.setGeometry(QtCore.QRect(620, 0, 91, 101))
        self.botao_retornar.setStyleSheet("image: url(:/botao_retornar/icones/retornar.png)")
        self.botao_retornar.setText("")
        self.botao_retornar.setObjectName("botao_retornar")
        self.tabela = QtWidgets.QTableWidget(Form)
        self.tabela.setGeometry(QtCore.QRect(20, 180, 711, 221))
        self.tabela.setObjectName("tabela")
        self.tabela.setColumnCount(7)
        self.tabela.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(1, item)
        self.botao_adicionar.clicked.connect(self.tela_adicionar)
        self.botao_alterar.clicked.connect(self.tela_altera_sod)
        self.botao_consultar.clicked.connect(self.tela_consulta_sod)
        self.botao_excluir.clicked.connect(self.exclui_sod)
        self.carrega_tabela()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tabela.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Código"))
        item = self.tabela.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Código Perfil 1"))

    def tela_consulta_sod(self):
        ativa = self.tabela.currentRow()
        id = self.tabela.item(ativa, 0)
        variaveis.id_consulta = id.text()
        variaveis.tipo_tela = 'consulta'
        self.Form = QtWidgets.QWidget()
        self.ui = geral_sod()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def tela_altera_sod(self):
        ativa = self.tabela.currentRow()
        id = self.tabela.item(ativa, 0)
        variaveis.id_consulta = id.text()
        variaveis.tipo_tela = 'altera'
        self.Form = QtWidgets.QWidget()
        self.ui = geral_sod()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def exclui_sod(self):
        ativa = self.tabela.currentRow()
        id = self.tabela.item(ativa, 0)
        obj = SodController(codigo=int(id.text()))
        obj.delete_sod()
        self.carrega_tabela()


    def tela_adicionar(self):
        self.Form = QtWidgets.QWidget()
        self.ui = tela_novo_sod()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def carrega_tabela(self):
        lista = self.todos_sod()
        todas_linhas = []
        for sis in lista:
            codigo = sis.codigo
            codigo_perfil1 = sis.codigo_perfil1
            nome_perfil1 = sis.nome_perfil1
            sistema_perfil1 = sis.sistema_perfil1
            codigo_perfil2 = sis.codigo_perfil2
            nome_perfil2 = sis.nome_perfil2
            sistema_perfil2 = sis.sistema_perfil2
            filhadaputagem = (codigo, codigo_perfil1, nome_perfil1, sistema_perfil1,
                              codigo_perfil2, nome_perfil2, sistema_perfil2)
            todas_linhas.append(filhadaputagem)
        df = pd.DataFrame(todas_linhas[:todas_linhas.__sizeof__()], columns=['Código',
                                                                             'Código Perfil 1','Nome Perfil 1', 'Sistema Perfil 1',
                                                                             'Código Perfil 2', 'Nome Perfil 2','Sistema Perfil 2',
                                                                             ])

        self.all_data = df
        numero_linhas = len(self.all_data.index)
        self.tabela.setRowCount(numero_linhas)
        self.tabela.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(numero_linhas):
            for j in range(len(self.all_data.columns)):
                print(self.all_data.iat[i, j])
                self.tabela.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.tabela.resizeColumnsToContents()
        self.tabela.resizeRowsToContents()

    def todos_sod(self):
        sod = SodController()
        todos = sod.todos_sod()
        return todos

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
