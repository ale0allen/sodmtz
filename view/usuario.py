from PyQt5 import QtCore, QtGui, QtWidgets
from controller.usuario import UsuarioController
from PyQt5.QtWidgets import  QTableWidgetItem
import pandas as pd
import view.variaveis
from view.geral_usuarios import geral_usuarios
from view.novo_usuario import novo_usuario_form
from view.vincula_perfil import vincula_perfil


import view.botao_adicionar
import view.botao_alterar
import view.botao_consultar
import view.botao_excluir
import view.botao_recarregar
import view.botao_retornar
import view.botao_vincular


from PyQt5 import QtCore, QtGui, QtWidgets


class tela_usuario(object):
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
        self.tabela.setColumnCount(2)
        self.tabela.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(1, item)
        self.botao_vincular = QtWidgets.QPushButton(Form)
        self.botao_vincular.setGeometry(QtCore.QRect(450, 0, 91, 101))
        self.botao_vincular.setStyleSheet("image: url(:/botaovincular/icones/vincular.png)")
        self.botao_vincular.setText("")
        self.botao_vincular.setObjectName("botao_vincular")
        self.carrega_tabela()

        self.botao_consultar.clicked.connect(self.tela_consulta_usuario)
        self.botao_alterar.clicked.connect(self.tela_altera_usuario)
        self.botao_adicionar.clicked.connect(self.tela_novo_usuario)
        self.botao_excluir.clicked.connect(self.exclui_usuario)
        self.botao_vincular.clicked.connect(self.tela_vincula_perfil)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tabela.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Código"))
        item = self.tabela.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nome"))

        self.botao_recarregar.clicked.connect(self.carrega_tabela)
        self.botao_retornar.clicked.connect(lambda: self.sairTela(Form))

    def sairTela(self, formSistema):
        formSistema.close()

    def carrega_tabela(self):
        lista = self.todos_usuarios()
        todas_linhas = []
        for sis in lista:
            cpf = sis.cpf_usuario
            nome = sis.nome_usuario
            filhadaputagem = (cpf, nome)
            todas_linhas.append(filhadaputagem)
        df = pd.DataFrame(todas_linhas[:todas_linhas.__sizeof__()], columns=['CPF', 'Nome'])

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

    def todos_usuarios(self):
        users = UsuarioController()
        todos = users.todos_usuarios()
        return todos

    def tela_consulta_usuario(self):
        ativa = self.tabela.currentRow()
        cpf = self.tabela.item(ativa, 0)
        variaveis.cpf_usuario = cpf.text()
        variaveis.tipo_tela = 'consulta'
        self.Form = QtWidgets.QWidget()
        self.ui = geral_usuarios()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def tela_altera_usuario(self):
        ativa = self.tabela.currentRow()
        cpf = self.tabela.item(ativa, 0)
        variaveis.cpf_usuario = cpf.text()
        variaveis.tipo_tela = 'altera'
        self.Form = QtWidgets.QWidget()
        self.ui = geral_usuarios()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def tela_novo_usuario(self):
        self.Form = QtWidgets.QWidget()
        self.ui = novo_usuario_form()
        self.ui.setupUi(self.Form)
        self.Form.show()

        print('abriu tela novo sistema')

    def exclui_usuario(self):
        ativa = self.tabela.currentRow()
        id = self.tabela.item(ativa, 0)
        user = UsuarioController(cpf_usuario=int(id.text()))
        user.delete_usuario()
        self.carrega_tabela()

    def tela_vincula_perfil(self):
        ativa = self.tabela.currentRow()
        cpf = self.tabela.item(ativa, 0)

        variaveis.cpf_usuario = cpf.text()
        self.Form = QtWidgets.QWidget()
        self.ui = vincula_perfil()
        self.ui.setupUi(self.Form)
        self.Form.show()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
