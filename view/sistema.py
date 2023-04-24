from controller.sistema import SistemaController
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QTableWidgetItem
import pandas as pd
import botao_adicionar
import botao_alterar
import botao_consultar
import botao_excluir
import botao_retornar
from novo_sistema import novo_sistema_form

class tela_sistema(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(751, 387)
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
        self.tabela.setColumnCount(2)
        self.tabela.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(1, item)
        self.botao_adicionar.clicked.connect(self.tela_novo_sistema)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #carrega arquivo tabela
        lista = self.todos_sistemas()
        todas_linhas = []
        for sis in lista:
            codigo = sis.codigo
            nome_sistema = sis.nome
            filhadaputagem = (codigo,nome_sistema)
            todas_linhas.append(filhadaputagem)
        df = pd.DataFrame(todas_linhas[:todas_linhas.__sizeof__()], columns = ['Código', 'Nome'])

        self.all_data = df
        numero_linhas = len(self.all_data.index)
        self.tabela.setRowCount(numero_linhas)
        self.tabela.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(numero_linhas):
            for j in range(len(self.all_data.columns)):
                print(self.all_data.iat[i,j])
                self.tabela.setItem(i,j, QTableWidgetItem(str(self.all_data.iat[i,j])))

        self.tabela.resizeColumnsToContents()
        self.tabela.resizeRowsToContents()
    def todos_sistemas(self):
        sist = SistemaController()
        todos = sist.todos_sistemas()
        return todos

    def tela_novo_sistema(self):
        self.Form = QtWidgets.QWidget()
        self.ui = novo_sistema_form()
        self.ui.setupUi(self.Form)
        self.Form.show()
        print('abriu tela novo sistema')
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tabela.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Código"))
        item = self.tabela.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nome"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = tela_sistema()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
