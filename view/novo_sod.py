import botao_cadastrar
import botao_cancelar


from PyQt5 import QtCore, QtGui, QtWidgets
from controller.perfil import PerfilController
from controller.sod import SodController

class tela_novo_sod(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.botao_cancelar = QtWidgets.QPushButton(Form)
        self.botao_cancelar.setGeometry(QtCore.QRect(60, 190, 75, 71))
        self.botao_cancelar.setStyleSheet("image: url(:/botao_cancelar/cancelar.png)")
        self.botao_cancelar.setText("")
        self.botao_cancelar.setObjectName("botao_cancelar")
        self.botao_cadastrar = QtWidgets.QPushButton(Form)
        self.botao_cadastrar.setGeometry(QtCore.QRect(230, 190, 75, 71))
        self.botao_cadastrar.setStyleSheet("image: url(:/botao_cadastrar/cadastrar.png)")
        self.botao_cadastrar.setText("")
        self.botao_cadastrar.setObjectName("botao_cadastrar")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 61, 21))
        self.label_2.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.box_perfil2 = QtWidgets.QComboBox(Form)
        self.box_perfil2.setGeometry(QtCore.QRect(90, 140, 241, 22))
        self.box_perfil2.setObjectName("box_perfil2")
        lista = self.carrega_opcoes()
        for sis in lista:
            self.box_perfil2.addItem("")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 61, 21))
        self.label_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.box_perfil1 = QtWidgets.QComboBox(Form)
        self.box_perfil1.setGeometry(QtCore.QRect(90, 70, 241, 22))
        self.box_perfil1.setObjectName("box_perfil1")
        for sis in lista:
            self.box_perfil1.addItem("")
        self.todos_perfis()
        self.retranslateUi(Form)
        self.botao_cadastrar.clicked.connect(self.novo_sod)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.botao_cancelar.clicked.connect(lambda: self.sairTela(Form))

    def sairTela(self, formSOD):
        formSOD.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Perfil"))
        self.label_3.setText(_translate("Form", "Perfil"))
        lista = self.todos_perfis()
        indice = 0
        for sis in lista:
            self.box_perfil1.setItemText(indice, _translate("Form", f'{sis.codigo_perfil} | {sis.nome_perfil} | {sis.nome_sistema}'))
            indice += 1
        indice = 0
        for sis in lista:
            self.box_perfil2.setItemText(indice, _translate("Form", f'{sis.codigo_perfil} | {sis.nome_perfil} | {sis.nome_sistema}'))
            indice += 1

    def carrega_opcoes(self):
        lista = self.todos_perfis()
        return lista

    def todos_perfis(self):
        perf = PerfilController()
        todos = perf.todos_perfis()
        return todos

    def novo_sod(self):
        perfil1 = self.box_perfil1.currentText()
        perfil1 = perfil1.split("|")
        perfil2 = self.box_perfil2.currentText()
        perfil2 = perfil2.split("|")
        codigo_perfil1 = perfil1[0]
        nome_perfil1 = perfil1[1]
        sistema_perfil1 = perfil1[2]
        codigo_perfil2 = perfil2[0]
        nome_perfil2 = perfil2[1]
        sistema_perfil2 = perfil2[2]
        sod = SodController(codigo_perfil1=codigo_perfil1,nome_perfil1=nome_perfil1,sistema_perfil1=sistema_perfil1,
                            codigo_perfil2=codigo_perfil2, nome_perfil2=nome_perfil2, sistema_perfil2=sistema_perfil2)
        sod.set_sod()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = tela_novo_sod()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
