import botao_cadastrar
import botao_cancelar
import variaveis

from PyQt5 import QtCore, QtGui, QtWidgets
from controller.perfil import PerfilController
from controller.sistema import SistemaController

class geral_perfil(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 70, 61, 21))
        self.label.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")

        self.botao_cancelar = QtWidgets.QPushButton(Form)
        self.botao_cancelar.setGeometry(QtCore.QRect(60, 220, 75, 71))
        self.botao_cancelar.setStyleSheet("image: url(:/botao_cancelar/cancelar.png)")
        self.botao_cancelar.setText("")
        self.botao_cancelar.setObjectName("botao_cancelar")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 61, 21))
        self.label_2.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 61, 21))
        self.label_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")


        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 61, 21))
        self.label_4.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")


        if variaveis.tipo_tela == "consulta":
            perf = PerfilController(codigo_perfil=int(variaveis.id_consulta))
            pqp = perf.get_perfil()
            print(pqp.codigo_perfil)

            self.form_codigo = QtWidgets.QLineEdit(Form)
            self.form_codigo.setGeometry(QtCore.QRect(90, 30, 71, 21))
            self.form_codigo.setObjectName("form_codigo")
            self.form_codigo.setText(str(pqp.codigo_perfil))
            self.form_codigo.setEnabled(False)


            self.form_nome = QtWidgets.QLineEdit(Form)
            self.form_nome.setGeometry(QtCore.QRect(90, 70, 241, 21))
            self.form_nome.setObjectName("form_nome")
            self.form_nome.setText(str(pqp.nome_perfil))
            self.form_nome.setEnabled(False)


            self.box_sistema = QtWidgets.QComboBox(Form)
            self.box_sistema.setGeometry(QtCore.QRect(90, 100, 241, 22))
            self.box_sistema.setObjectName("box_sistema")
            lista = self.carrega_opcoes()
            for sis in lista:
                self.box_sistema.addItem("")
            self.box_sistema.setCurrentText(str(pqp.nome_sistema))
            self.box_sistema.setEnabled(False)


            self.form_descricao = QtWidgets.QTextEdit(Form)
            self.form_descricao.setGeometry(QtCore.QRect(93, 140, 231, 71))
            self.form_descricao.setObjectName("form_descricao")
            self.form_descricao.setText(str(pqp.descricao_perfil))
            self.form_descricao.setEnabled(False)
            self.botao_cancelar.clicked.connect(lambda: self.sairTela(Form))

        if variaveis.tipo_tela == "altera":
            perf = PerfilController(codigo_perfil=int(variaveis.id_consulta))
            pqp = perf.get_perfil()
            print(pqp.codigo_perfil)

            self.form_codigo = QtWidgets.QLineEdit(Form)
            self.form_codigo.setGeometry(QtCore.QRect(90, 30, 71, 21))
            self.form_codigo.setObjectName("form_codigo")
            self.form_codigo.setText(str(pqp.codigo_perfil))
            self.form_codigo.setEnabled(False)

            self.form_nome = QtWidgets.QLineEdit(Form)
            self.form_nome.setGeometry(QtCore.QRect(90, 70, 241, 21))
            self.form_nome.setObjectName("form_nome")
            self.form_nome.setText(str(pqp.nome_perfil))


            self.box_sistema = QtWidgets.QComboBox(Form)
            self.box_sistema.setGeometry(QtCore.QRect(90, 100, 241, 22))
            self.box_sistema.setObjectName("box_sistema")
            lista = self.carrega_opcoes()
            for sis in lista:
                self.box_sistema.addItem("")
            self.box_sistema.setCurrentText(str(pqp.nome_sistema))


            self.form_descricao = QtWidgets.QTextEdit(Form)
            self.form_descricao.setGeometry(QtCore.QRect(93, 140, 231, 71))
            self.form_descricao.setObjectName("form_descricao")
            self.form_descricao.setText(str(pqp.descricao_perfil))

            self.botao_cadastrar = QtWidgets.QPushButton(Form)
            self.botao_cadastrar.setGeometry(QtCore.QRect(230, 220, 75, 71))
            self.botao_cadastrar.setStyleSheet("image: url(:/botao_cadastrar/cadastrar.png)")
            self.botao_cadastrar.setText("")
            self.botao_cadastrar.setObjectName("botao_cadastrar")
            self.botao_cadastrar.clicked.connect(self.altera_perfil)
            self.botao_cancelar.clicked.connect(lambda: self.sairTela(Form))


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def carrega_opcoes(self):
        lista = self.todos_sistemas()
        return lista

    def todos_sistemas(self):
        sist = SistemaController()
        todos = sist.todos_sistemas()
        return todos

    def altera_perfil(self):
        obj = PerfilController(codigo_perfil=variaveis.id_consulta)
        print(self.form_nome.text())
        print(self.box_sistema.currentText())
        print(self.form_descricao.toPlainText())
        obj.update_perfil(novo_nome=self.form_nome.text(), novo_sistema=self.box_sistema.currentText(),
                          nova_descricao=self.form_descricao.toPlainText())
        print('alterou')

    def sairTela(self, formDadosPerfil):
        formDadosPerfil.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Nome"))
        self.label_2.setText(_translate("Form", "Sistema"))
        self.label_3.setText(_translate("Form", "Descrição"))
        lista = self.todos_sistemas()
        indice = 0
        for sis in lista:
            self.box_sistema.setItemText(indice, _translate("Form", str(sis.nome)))
            indice += 1

        self.label_4.setText(_translate("Form", "Código"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = geral_perfil()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
