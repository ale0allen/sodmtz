import view.botao_cadastrar
import view.botao_cancelar
import view.variaveis
from view import variaveis
from controller.sistema import SistemaController
from PyQt5 import QtCore, QtGui, QtWidgets


class geral_sistemas(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 301)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 110, 61, 21))
        self.label.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        # self.form_nome = QtWidgets.QLineEdit(Form)
        # self.form_nome.setGeometry(QtCore.QRect(80, 110, 251, 21))
        # self.form_nome.setObjectName("form_nome")
        self.botao_cancelar = QtWidgets.QPushButton(Form)
        self.botao_cancelar.setGeometry(QtCore.QRect(60, 170, 75, 71))
        self.botao_cancelar.setStyleSheet("image: url(:/botao_cancelar/cancelar.png)")
        self.botao_cancelar.setText("")
        self.botao_cancelar.setObjectName("botao_cancelar")

        self.cod = QtWidgets.QLabel(Form)
        self.cod.setGeometry(QtCore.QRect(20, 60, 61, 21))
        self.cod.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.cod.setObjectName("cod")
        # self.form_codigo = QtWidgets.QLineEdit(Form)
        # self.form_codigo.setGeometry(QtCore.QRect(80, 60, 51, 21))
        # self.form_codigo.setObjectName("form_codigo")
        # self.form_codigo.setText(variaveis.id_consulta)

        self.botao_cancelar.clicked.connect(lambda: self.sairTela(Form))

        if variaveis.tipo_tela == 'consulta':
            obj = SistemaController(codigo=int(variaveis.id_consulta))
            pqp = obj.get_sistema()
            self.form_codigo = QtWidgets.QLineEdit(Form)
            self.form_codigo.setGeometry(QtCore.QRect(80, 60, 251, 21))
            self.form_codigo.setObjectName("form_codigo")
            self.form_codigo.setEnabled(False)
            self.form_codigo.setText(str("{:015}".format(pqp.codigo)))
            self.form_nome = QtWidgets.QLineEdit(Form)
            self.form_nome.setGeometry(QtCore.QRect(80, 110, 251, 21))
            self.form_nome.setObjectName("form_nome")
            self.form_nome.setText(str(pqp.nome))
            self.form_nome.setEnabled(False)

        if variaveis.tipo_tela == 'altera':
            obj = SistemaController(codigo=int(variaveis.id_consulta))
            pqp = obj.get_sistema()
            self.form_codigo = QtWidgets.QLineEdit(Form)
            self.form_codigo.setGeometry(QtCore.QRect(80, 60, 251, 21))
            self.form_codigo.setObjectName("form_codigo")
            self.form_codigo.setEnabled(False)
            self.form_codigo.setText(str("{:015}".format(pqp.codigo)))
            self.form_nome = QtWidgets.QLineEdit(Form)
            self.form_nome.setGeometry(QtCore.QRect(80, 110, 251, 21))
            self.form_nome.setObjectName("form_nome")
            self.form_nome.setText(str(pqp.nome))
            self.form_nome.setEnabled(True)
            self.botao_cadastrar = QtWidgets.QPushButton(Form)
            self.botao_cadastrar.setGeometry(QtCore.QRect(230, 170, 75, 71))
            self.botao_cadastrar.setStyleSheet("image: url(:/botao_cadastrar/cadastrar.png)")
            self.botao_cadastrar.setText("")
            self.botao_cadastrar.setObjectName("botao_cadastrar")
            self.botao_cadastrar.clicked.connect(self.salva_alteracao)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def sairTela(self, formSistema):
        formSistema.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Nome"))
        self.cod.setText(_translate("Form", "Cód"))

    def salva_alteracao(self):
        obj = SistemaController(codigo=int(variaveis.id_consulta))
        obj.update_sistema(novo_nome=self.form_nome.text())
        print('Alterouuuu')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = geral_sistemas()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
