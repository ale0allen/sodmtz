from PyQt5 import QtCore, QtGui, QtWidgets
from controller.sistema import SistemaController

import botao_cadastrar
import botao_cancelar

class novo_sistema_form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 70, 61, 21))
        self.label.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.form_nome = QtWidgets.QLineEdit(Form)
        self.form_nome.setGeometry(QtCore.QRect(80, 70, 251, 21))
        self.form_nome.setObjectName("form_nome")
        self.botao_cancelar = QtWidgets.QPushButton(Form)
        self.botao_cancelar.setGeometry(QtCore.QRect(60, 170, 75, 71))
        self.botao_cancelar.setStyleSheet("image: url(:/botao_cancelar/cancelar.png)")
        self.botao_cancelar.setText("")
        self.botao_cancelar.setObjectName("botao_cancelar")
        self.botao_cadastrar = QtWidgets.QPushButton(Form)
        self.botao_cadastrar.setGeometry(QtCore.QRect(230, 170, 75, 71))
        self.botao_cadastrar.setStyleSheet("image: url(:/botao_cadastrar/cadastrar.png)")
        self.botao_cadastrar.setText("")
        self.botao_cadastrar.setObjectName("botao_cadastrar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.botao_cadastrar.clicked.connect(self.cadastrar)

    def cadastrar(self):
        nome = self.form_nome.text()
        sist = SistemaController(nome=nome)
        sist.set_sistema()
        print(sist)
        print('Salvou')


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Nome"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
