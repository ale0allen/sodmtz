import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QTableWidgetItem
from novo_perfil import tela_novo_perfil
from geral_perfil import geral_perfil
import variaveis

import botao_adicionar
import botao_alterar
import botao_consultar
import botao_recarregar
import botao_excluir
import botao_retornar
from controller.perfil import PerfilController



class tela_perfis(object):
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
        self.botao_recarregar = QtWidgets.QPushButton(Form)
        self.botao_recarregar.setGeometry(QtCore.QRect(270, 0, 91, 101))
        self.botao_recarregar.setStyleSheet("image: url(:/botao_recarregar/icones/recarregar.png)")
        self.botao_recarregar.setText("")
        self.botao_recarregar.setObjectName("botao_recarregar")
        self.botao_excluir = QtWidgets.QPushButton(Form)
        self.botao_excluir.setGeometry(QtCore.QRect(360, 0, 91, 101))
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
        self.tabela.setColumnCount(4)
        self.tabela.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(1, item)
        self.carrega_tabela()
        self.retranslateUi(Form)
        self.botao_adicionar.clicked.connect(self.abre_tela_adicionar)
        self.botao_consultar.clicked.connect(self.tela_consulta_perfil)
        self.botao_alterar.clicked.connect(self.tela_altera_perfil)
        self.botao_excluir.clicked.connect(self.exclui_perfil)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Perfis"))
        self.botao_recarregar.setToolTip(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.botao_retornar.setToolTip(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))

        self.botao_recarregar.clicked.connect(self.carrega_tabela)
        self.botao_retornar.clicked.connect(lambda: self.sairTela(Form))

    def abre_tela_adicionar(self):
        self.Form = QtWidgets.QWidget()
        self.ui = tela_novo_perfil()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def sairTela(self, formPerfil):
        formPerfil.close()

    def carrega_tabela(self):
        lista = self.todos_perfis()
        todas_linhas = []
        for sis in lista:
            codigo = sis.codigo_perfil
            nome_perfil = sis.nome_perfil
            nome_sistema = sis.nome_sistema
            descricao_perfil = sis.descricao_perfil
            filhadaputagem = (codigo, nome_perfil, nome_sistema, descricao_perfil)
            todas_linhas.append(filhadaputagem)
        df = pd.DataFrame(todas_linhas[:todas_linhas.__sizeof__()], columns=['Código', 'Nome', 'Sistema', 'Descricao'])

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

    def todos_perfis(self):
        perf = PerfilController()
        todos = perf.todos_perfis()
        return todos

    def tela_consulta_perfil(self):
        ativa = self.tabela.currentRow()
        id = self.tabela.item(ativa, 0)
        if id is None:
            self.todos_perfis()
        else:
            variaveis.id_consulta = id.text()
            variaveis.tipo_tela = 'consulta'
            self.Form = QtWidgets.QWidget()
            self.ui = geral_perfil()
            self.ui.setupUi(self.Form)
            self.Form.show()


    def exclui_perfil(self):
        ativa = self.tabela.currentRow()
        id = self.tabela.item(ativa,0)
        obj = PerfilController(codigo_perfil=int(id.text()))
        obj.delete_perfil()
        self.carrega_tabela()


    def tela_altera_perfil(self):
        ativa = self.tabela.currentRow()
        id = self.tabela.item(ativa, 0)
        if id is None:
            self.todos_perfis()
        else:
            variaveis.id_consulta = id.text()
            variaveis.tipo_tela = 'altera'
            self.Form = QtWidgets.QWidget()
            self.ui = geral_perfil()
            self.ui.setupUi(self.Form)
            self.Form.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = tela_perfis()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
