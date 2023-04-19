from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 110, 61, 51))
        self.label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 120, 211, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 20, 241, 51))
        self.label_2.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.btSalvar = QtWidgets.QPushButton(Dialog)
        self.btSalvar.setGeometry(QtCore.QRect(50, 220, 101, 41))
        self.btSalvar.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.btSalvar.setObjectName("btSalvar")
        self.btCancelar = QtWidgets.QPushButton(Dialog)
        self.btCancelar.setGeometry(QtCore.QRect(220, 220, 101, 41))
        self.btCancelar.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.btCancelar.setObjectName("btCancelar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.btSalvar.clicked.connect(self.salvar)
        self.btCancelar.clicked.connect(self.cancelar)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Nome"))
        self.label_2.setText(_translate("Dialog", "NOVO SISTEMA"))
        self.btSalvar.setText(_translate("Dialog", "SALVAR"))
        self.btCancelar.setText(_translate("Dialog", "CANCELAR"))

    def salvar(self):
        print('Salvou')

    def cancelar(self):
        print('Cancelou!')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
