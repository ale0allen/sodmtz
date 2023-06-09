import view.botao_cadastrar
import view.botao_cancelar

from PyQt5 import QtCore, QtGui, QtWidgets
import view.variaveis
from view import variaveis
from controller.sod import SodController
from controller.perfil import PerfilController

class geral_sod(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(527, 394)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 110, 61, 21))
        self.label.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.botao_cancelar = QtWidgets.QPushButton(Form)
        self.botao_cancelar.setGeometry(QtCore.QRect(130, 300, 75, 71))
        self.botao_cancelar.setStyleSheet("image: url(:/botao_cancelar/cancelar.png)")
        self.botao_cancelar.setText("")
        self.botao_cancelar.setObjectName("botao_cancelar")

        self.cod = QtWidgets.QLabel(Form)
        self.cod.setGeometry(QtCore.QRect(20, 20, 61, 21))
        self.cod.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.cod.setObjectName("cod")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 61, 21))
        self.label_2.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 61, 21))
        self.label_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 60, 61, 21))
        self.label_4.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(290, 190, 61, 21))
        self.label_5.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(290, 110, 61, 21))
        self.label_6.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(290, 150, 61, 21))
        self.label_7.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(340, 60, 61, 21))
        self.label_8.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.botao_cancelar.clicked.connect(lambda: self.sairTela(Form))

        if variaveis.tipo_tela == 'consulta':
            obj = SodController(codigo=int(variaveis.id_consulta))
            pqp = obj.get_sod()

            self.form_codigo = QtWidgets.QLineEdit(Form)
            self.form_codigo.setGeometry(QtCore.QRect(80, 20, 51, 21))
            self.form_codigo.setText(str(pqp.codigo))
            self.form_codigo.setObjectName("form_codigo")

            self.form_codigo.setEnabled(False)

            self.form_codigo_perfil1 = QtWidgets.QLineEdit(Form)
            self.form_codigo_perfil1.setGeometry(QtCore.QRect(80, 110, 131, 21))
            self.form_codigo_perfil1.setObjectName("form_codigo_perfil1")
            self.form_codigo_perfil1.setText(str(pqp.codigo_perfil1))
            self.form_codigo_perfil1.setEnabled(False)

            self.form_nome_perfil_1 = QtWidgets.QLineEdit(Form)
            self.form_nome_perfil_1.setGeometry(QtCore.QRect(80, 150, 131, 21))
            self.form_nome_perfil_1.setObjectName("form_nome_perfil_1")
            self.form_nome_perfil_1.setText(str(pqp.nome_perfil1))
            self.form_nome_perfil_1.setEnabled(False)

            self.form_sistema_perfil1 = QtWidgets.QLineEdit(Form)
            self.form_sistema_perfil1.setGeometry(QtCore.QRect(80, 190, 131, 21))
            self.form_sistema_perfil1.setObjectName("form_sistema_perfil1")
            self.form_sistema_perfil1.setText(str(pqp.sistema_perfil1))
            self.form_sistema_perfil1.setEnabled(False)

            self.form_codigo_perfil2 = QtWidgets.QLineEdit(Form)
            self.form_codigo_perfil2.setGeometry(QtCore.QRect(350, 110, 131, 21))
            self.form_codigo_perfil2.setObjectName("form_codigo_perfil2")
            self.form_codigo_perfil2.setText(str(pqp.codigo_perfil2))
            self.form_codigo_perfil2.setEnabled(False)

            self.form_nome_perfil2 = QtWidgets.QLineEdit(Form)
            self.form_nome_perfil2.setGeometry(QtCore.QRect(350, 150, 131, 21))
            self.form_nome_perfil2.setObjectName("form_nome_perfil2")
            self.form_nome_perfil2.setText(str(pqp.nome_perfil2))
            self.form_nome_perfil2.setEnabled(False)

            self.form_sistema_perfil2 = QtWidgets.QLineEdit(Form)
            self.form_sistema_perfil2.setGeometry(QtCore.QRect(350, 190, 131, 21))
            self.form_sistema_perfil2.setObjectName("form_sistema_perfil2")
            self.form_sistema_perfil2.setText(str(pqp.sistema_perfil2))
            self.form_sistema_perfil2.setEnabled(False)

        if variaveis.tipo_tela == 'altera':
            obj = SodController(codigo=int(variaveis.id_consulta))
            pqp = obj.get_sod()

            lista = self.carrega_opcoes()
            print(lista)

            self.form_codigo = QtWidgets.QLineEdit(Form)
            self.form_codigo.setGeometry(QtCore.QRect(80, 20, 51, 21))
            self.form_codigo.setText(str(pqp.codigo))
            self.form_codigo.setObjectName("form_codigo")
            self.form_codigo.setEnabled(False)

            self.box_codigo_perfil1 = QtWidgets.QComboBox(Form)
            self.box_codigo_perfil1.setGeometry(QtCore.QRect(80, 110, 131, 21))
            self.box_codigo_perfil1.setObjectName("box_codigo_perfil1")
            for sis in lista:
                self.box_codigo_perfil1.addItem(str(sis.codigo))
            self.box_codigo_perfil1.currentIndexChanged.connect(self.atualizar_info1)


            self.form_nome_perfil_1 = QtWidgets.QLineEdit(Form)
            self.form_nome_perfil_1.setGeometry(QtCore.QRect(80, 150, 131, 21))
            self.form_nome_perfil_1.setObjectName("form_nome_perfil_1")
            self.form_nome_perfil_1.setText(str(pqp.nome_perfil1))
            self.form_nome_perfil_1.setEnabled(False)

            self.form_sistema_perfil1 = QtWidgets.QLineEdit(Form)
            self.form_sistema_perfil1.setGeometry(QtCore.QRect(80, 190, 131, 21))
            self.form_sistema_perfil1.setObjectName("form_sistema_perfil1")
            self.form_sistema_perfil1.setText(str(pqp.sistema_perfil1))
            self.form_sistema_perfil1.setEnabled(False)

            self.box_codigo_perfil2 = QtWidgets.QComboBox(Form)
            self.box_codigo_perfil2.setGeometry(QtCore.QRect(350, 110, 131, 21))
            self.box_codigo_perfil2.setObjectName("box_codigo_perfil2")
            for sis in lista:
                self.box_codigo_perfil2.addItem(str(sis.codigo))
            self.box_codigo_perfil2.currentIndexChanged.connect(self.atualizar_info2)

            self.form_nome_perfil2 = QtWidgets.QLineEdit(Form)
            self.form_nome_perfil2.setGeometry(QtCore.QRect(350, 150, 131, 21))
            self.form_nome_perfil2.setObjectName("form_nome_perfil2")
            self.form_nome_perfil2.setText(str(pqp.nome_perfil2))
            self.form_nome_perfil2.setEnabled(False)

            self.form_sistema_perfil2 = QtWidgets.QLineEdit(Form)
            self.form_sistema_perfil2.setGeometry(QtCore.QRect(350, 190, 131, 21))
            self.form_sistema_perfil2.setObjectName("form_sistema_perfil2")
            self.form_sistema_perfil2.setText(str(pqp.sistema_perfil2))
            self.form_sistema_perfil2.setEnabled(False)

            self.botao_cadastrar = QtWidgets.QPushButton(Form)
            self.botao_cadastrar.setGeometry(QtCore.QRect(310, 300, 75, 71))
            self.botao_cadastrar.setStyleSheet("image: url(:/botao_cadastrar/cadastrar.png)")
            self.botao_cadastrar.setText("")
            self.botao_cadastrar.setObjectName("botao_cadastrar")
            self.botao_cadastrar.clicked.connect(self.altera_sod)

    def sairTela(self, formSOD):
        formSOD.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Cód"))
        self.cod.setText(_translate("Form", "Cód"))
        self.label_2.setText(_translate("Form", "Nome"))
        self.label_3.setText(_translate("Form", "Sistema"))
        self.label_4.setText(_translate("Form", "Perfil 1"))
        self.label_5.setText(_translate("Form", "Sistema"))
        self.label_6.setText(_translate("Form", "Cód"))
        self.label_7.setText(_translate("Form", "Nome"))
        self.label_8.setText(_translate("Form", "Perfil 2"))

    def atualizar_info1(self, index):
        opcao_selecionada = self.box_codigo_perfil1.currentText()
        obj = PerfilController(codigo_perfil=int(opcao_selecionada))
        dados = obj.get_perfil()
        self.form_nome_perfil_1.setText(dados.nome_perfil)
        self.form_sistema_perfil1.setText(dados.nome_sistema)

    def atualizar_info2(self, index):
        opcao_selecionada = self.box_codigo_perfil2.currentText()
        obj = PerfilController(codigo_perfil=int(opcao_selecionada))
        dados = obj.get_perfil()
        self.form_nome_perfil2.setText(dados.nome_perfil)
        self.form_sistema_perfil2.setText(dados.nome_sistema)

    def carrega_opcoes(self):
        lista = self.todos_sod()
        return lista

    def altera_sod(self):
        obj = SodController(codigo=int(variaveis.id_consulta))
        novo_codigo_perfil1 = self.box_codigo_perfil1.currentText()
        novo_nome_perfil1 = self.form_nome_perfil_1.text()
        novo_sistema_perfil1 = self.form_sistema_perfil1.text()
        novo_codigo_perfil2 = self.box_codigo_perfil2.currentText()
        novo_nome_perfil2 = self.form_nome_perfil2.text()
        novo_sistema_perfil2 = self.form_sistema_perfil2.text()

        obj.update_sod(novo_codigo_perfil1=novo_codigo_perfil1, novo_nome_perfil1=novo_nome_perfil1,
                       novo_sistema_perfil1=novo_sistema_perfil1, novo_codigo_perfil2=novo_codigo_perfil2,
                       novo_nome_perfil2=novo_nome_perfil2, novo_sistema_perfil2=novo_sistema_perfil2)
        print('alterou')

    def todos_sod(self):
        sod = SodController()
        todos = sod.todos_sod()
        return todos



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = geral_sod()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
