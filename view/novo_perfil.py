import botao_cadastrar
import botao_cancelar
from controller.sistema import SistemaController
from controller.perfil import PerfilController
from PyQt5 import QtCore, QtGui, QtWidgets


class tela_novo_perfil(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 50, 61, 21))
        self.label.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.form_nome = QtWidgets.QLineEdit(Form)
        self.form_nome.setGeometry(QtCore.QRect(80, 50, 251, 21))
        self.form_nome.setObjectName("form_nome")
        self.botao_cancelar = QtWidgets.QPushButton(Form)
        self.botao_cancelar.setGeometry(QtCore.QRect(60, 210, 75, 71))
        self.botao_cancelar.setStyleSheet("image: url(:/botao_cancelar/cancelar.png)")
        self.botao_cancelar.setText("")
        self.botao_cancelar.setObjectName("botao_cancelar")
        self.botao_cadastrar = QtWidgets.QPushButton(Form)
        self.botao_cadastrar.setGeometry(QtCore.QRect(230, 210, 75, 71))
        self.botao_cadastrar.setStyleSheet("image: url(:/botao_cadastrar/cadastrar.png)")
        self.botao_cadastrar.setText("")
        self.botao_cadastrar.setObjectName("botao_cadastrar")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 61, 21))
        self.label_2.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 61, 21))
        self.label_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.box_sistema = QtWidgets.QComboBox(Form)
        self.box_sistema.setGeometry(QtCore.QRect(90, 90, 241, 22))
        self.box_sistema.setObjectName("box_sistema")
        lista = self.carrega_opcoes()
        for sis in lista:
            self.box_sistema.addItem("")
        self.form_descricao = QtWidgets.QTextEdit(Form)
        self.form_descricao.setGeometry(QtCore.QRect(93, 130, 231, 71))
        self.form_descricao.setObjectName("form_descricao")

        self.botao_cadastrar.clicked.connect(self.cadastrar)
        self.botao_cancelar.clicked.connect(lambda: self.sairTela(Form))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Nome"))
        self.label_2.setText(_translate("Form", "Sistema"))
        self.label_3.setText(_translate("Form", "Descrição"))
        lista = self.todos_sistemas()
        indice = 0
        for sis in lista:
            self.box_sistema.setItemText(indice, _translate("Form", sis.nome))
            indice += 1

    def cadastrar(self):
        nome_perfil = self.form_nome.text()
        nome_sistema = self.box_sistema.currentText()
        descricao = self.form_descricao.toPlainText()
        perfil = PerfilController(nome_perfil=nome_perfil, nome_sistema=nome_sistema, descricao_perfil=descricao)
        perfil.set_perfil()
        print(perfil)
        print('Cadastrou!!')

    def sairTela(self, formDadosPerfil):
        formDadosPerfil.close()

    def carrega_opcoes(self):
        lista = self.todos_sistemas()
        return lista


    def todos_sistemas(self):
        sist = SistemaController()
        todos = sist.todos_sistemas()
        return todos


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = tela_novo_perfil()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
