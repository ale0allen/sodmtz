from PyQt5 import QtCore, QtGui, QtWidgets
import view.botao_cadastrar
import view.botao_cancelar
import view.variaveis
from controller.usuario import UsuarioController


class geral_usuarios(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 301)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 110, 61, 21))
        self.label.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")


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
        self.cod = QtWidgets.QLabel(Form)
        self.cod.setGeometry(QtCore.QRect(20, 60, 61, 21))
        self.cod.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.cod.setObjectName("cod")

        if variaveis.tipo_tela == 'consulta':
            user = UsuarioController(cpf_usuario=variaveis.cpf_usuario)
            pqp = user.get_usuario()

            self.form_nome = QtWidgets.QLineEdit(Form)
            self.form_nome.setGeometry(QtCore.QRect(80, 110, 251, 21))
            self.form_nome.setObjectName("form_nome")
            self.form_nome.setText(str(pqp.nome_usuario))
            self.form_nome.setEnabled(False)

            self.form_cpf = QtWidgets.QLineEdit(Form)
            self.form_cpf.setGeometry(QtCore.QRect(80, 60, 241, 21))
            self.form_cpf.setObjectName("form_cpf")
            self.form_cpf.setText(str(pqp.cpf_usuario))
            self.form_cpf.setEnabled(False)

        if variaveis.tipo_tela ==  'altera':
            user = UsuarioController(cpf_usuario=variaveis.cpf_usuario)
            pqp = user.get_usuario()

            self.form_nome = QtWidgets.QLineEdit(Form)
            self.form_nome.setGeometry(QtCore.QRect(80, 110, 251, 21))
            self.form_nome.setObjectName("form_nome")
            self.form_nome.setText(str(pqp.nome_usuario))


            self.form_cpf = QtWidgets.QLineEdit(Form)
            self.form_cpf.setGeometry(QtCore.QRect(80, 60, 241, 21))
            self.form_cpf.setObjectName("form_cpf")
            self.form_cpf.setText(str(pqp.cpf_usuario))
            self.form_cpf.setEnabled(False)

            self.botao_cadastrar.clicked.connect(self.salva_alteracao)





        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Nome"))
        self.cod.setText(_translate("Form", "CPF"))

    def salva_alteracao(self):
        obj = UsuarioController(cpf_usuario=variaveis.cpf_usuario)
        obj.update_usuario(novo_nome=self.form_nome.text())
        print('Alterouuuu')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = geral_usuarios()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
