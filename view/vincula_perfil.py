from PyQt5 import QtCore, QtGui, QtWidgets
import view.botao_cadastrar
import view.botao_cancelar

from controller.perfil import PerfilController
from controller.usuario import UsuarioController
from controller.vinculo import VinculoController

import view.variaveis
from view import variaveis


class vincula_perfil(object):
    def setupUi(self, Form):
        obj = UsuarioController(cpf_usuario=variaveis.cpf_usuario)
        pqp = obj.get_usuario()
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 80, 61, 21))
        self.label.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.form_nome = QtWidgets.QLineEdit(Form)
        self.form_nome.setGeometry(QtCore.QRect(90, 80, 241, 21))
        self.form_nome.setObjectName("form_nome")
        self.form_nome.setText(str(pqp.nome_usuario))
        self.form_nome.setEnabled(False)
        self.botao_cancelar = QtWidgets.QPushButton(Form)
        self.botao_cancelar.setGeometry(QtCore.QRect(60, 220, 75, 71))
        self.botao_cancelar.setStyleSheet("image: url(:/botao_cancelar/cancelar.png)")
        self.botao_cancelar.setText("")
        self.botao_cancelar.setObjectName("botao_cancelar")
        self.botao_cadastrar = QtWidgets.QPushButton(Form)
        self.botao_cadastrar.setGeometry(QtCore.QRect(230, 220, 75, 71))
        self.botao_cadastrar.setStyleSheet("image: url(:/botao_cadastrar/cadastrar.png)")
        self.botao_cadastrar.setText("")
        self.botao_cadastrar.setObjectName("botao_cadastrar")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 61, 21))
        self.label_2.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.box_sistema = QtWidgets.QComboBox(Form)
        self.box_sistema.setGeometry(QtCore.QRect(90, 120, 241, 22))
        self.box_sistema.setObjectName("box_sistema")
        lista = self.carrega_opcoes()
        for sis in lista:
            self.box_sistema.addItem("")
        self.todos_perfis()

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 41, 21))
        self.label_4.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.form_codigo = QtWidgets.QLineEdit(Form)
        self.form_codigo.setGeometry(QtCore.QRect(90, 40, 241, 21))
        self.form_codigo.setObjectName("form_codigo")
        self.form_codigo.setText(str(pqp.cpf_usuario))
        self.form_codigo.setEnabled(False)
        self.botao_cadastrar.clicked.connect(self.cria_vinculo)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Nome"))
        self.label_2.setText(_translate("Form", "Perfil"))
        self.box_sistema.setItemText(0, _translate("Form", "Opção1"))
        self.box_sistema.setItemText(1, _translate("Form", "Opção2"))
        self.label_4.setText(_translate("Form", "CPF"))
        lista = self.todos_perfis()
        indice = 0
        for sis in lista:
            self.box_sistema.setItemText(indice, _translate("Form",
                                                            f'{sis.codigo_perfil} | {sis.nome_perfil} | {sis.nome_sistema}'))
            indice += 1


    def todos_perfis(self):
        perf = PerfilController()
        todos = perf.todos_perfis()
        return todos


    def carrega_opcoes(self):
        lista = self.todos_perfis()
        return lista

    def cria_vinculo(self):
        cpf_usuario = self.form_codigo.text()
        perfil = self.box_sistema.currentText()
        perfil = perfil.split('|')
        cod_perfil= perfil[0]
        vinculo = VinculoController(cpf_usuario=cpf_usuario, id_perfil=cod_perfil)
        vinculo.set_vinculo()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = vincula_perfil()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
