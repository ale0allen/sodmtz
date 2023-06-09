from PyQt5 import QtCore, QtGui, QtWidgets
import view.icone_matriz
import view.icone_perfil
import view.icone_sistema
import view.icone_usuarios
import view.logo_agl

from view.sistema import tela_sistema
from view.perfil import tela_perfis
from view.sod import tela_matriz
from view.usuario import tela_usuario

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(822, 353)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.botao_perfil_consulta = QtWidgets.QPushButton(self.centralwidget)
        self.botao_perfil_consulta.setGeometry(QtCore.QRect(230, 0, 161, 161))
        self.botao_perfil_consulta.setStyleSheet("image: url(:/icone_perfil/icones/2.png)")
        self.botao_perfil_consulta.setText("")
        self.botao_perfil_consulta.setObjectName("botao_perfil_consulta")
        self.botao_sistema_consulta = QtWidgets.QPushButton(self.centralwidget)
        self.botao_sistema_consulta.setGeometry(QtCore.QRect(40, 0, 161, 161))
        self.botao_sistema_consulta.setStyleSheet("image: url(:/icone_sistema/icones/1.png)")
        self.botao_sistema_consulta.setText("")
        self.botao_sistema_consulta.setObjectName("botao_sistema_consulta")
        self.botao_matriz_consulta = QtWidgets.QPushButton(self.centralwidget)
        self.botao_matriz_consulta.setGeometry(QtCore.QRect(450, 0, 161, 161))
        self.botao_matriz_consulta.setStyleSheet("image: url(:/icone_matriz/icones/3.png)")
        self.botao_matriz_consulta.setText("")
        self.botao_matriz_consulta.setObjectName("botao_matriz_consulta")
        self.botao_usuarios_consulta = QtWidgets.QPushButton(self.centralwidget)
        self.botao_usuarios_consulta.setGeometry(QtCore.QRect(640, 0, 161, 161))
        self.botao_usuarios_consulta.setStyleSheet("image: url(:/icone_usuarios/icones/USUARIOS.png)")
        self.botao_usuarios_consulta.setText("")
        self.botao_usuarios_consulta.setObjectName("botao_usuarios_consulta")
        self.logo_agl = QtWidgets.QPushButton(self.centralwidget)
        self.logo_agl.setEnabled(True)
        self.logo_agl.setGeometry(QtCore.QRect(260, 180, 331, 121))
        self.logo_agl.setStyleSheet("image: url(:/logo_agl/icones/agl.png);\n"
"border: none;")
        self.logo_agl.setText("")
        self.logo_agl.setObjectName("logo_agl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 822, 21))
        self.menubar.setObjectName("menubar")
        self.menuSistemas = QtWidgets.QMenu(self.menubar)
        self.menuSistemas.setObjectName("menuSistemas")
        self.menuPerfiil = QtWidgets.QMenu(self.menubar)
        self.menuPerfiil.setObjectName("menuPerfiil")
        self.menuMatriz_SOD = QtWidgets.QMenu(self.menubar)
        self.menuMatriz_SOD.setObjectName("menuMatriz_SOD")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu_sistema_novo = QtWidgets.QAction(MainWindow)
        self.menu_sistema_novo.setObjectName("menu_sistema_novo")
        self.menu_sistema_consulta = QtWidgets.QAction(MainWindow)
        self.menu_sistema_consulta.setObjectName("menu_sistema_consulta")
        self.menu_perfil_novo = QtWidgets.QAction(MainWindow)
        self.menu_perfil_novo.setObjectName("menu_perfil_novo")
        self.menu_perfil_Consulta = QtWidgets.QAction(MainWindow)
        self.menu_perfil_Consulta.setObjectName("menu_perfil_Consulta")
        self.menu_matriz_novo = QtWidgets.QAction(MainWindow)
        self.menu_matriz_novo.setObjectName("menu_matriz_novo")
        self.menu_matriz_consulta = QtWidgets.QAction(MainWindow)
        self.menu_matriz_consulta.setObjectName("menu_matriz_consulta")
        self.menuSistemas.addAction(self.menu_sistema_novo)
        self.menuSistemas.addAction(self.menu_sistema_consulta)
        self.menuPerfiil.addAction(self.menu_perfil_novo)
        self.menuPerfiil.addAction(self.menu_perfil_Consulta)
        self.menuMatriz_SOD.addAction(self.menu_matriz_novo)
        self.menuMatriz_SOD.addAction(self.menu_matriz_consulta)
        self.menubar.addAction(self.menuSistemas.menuAction())
        self.menubar.addAction(self.menuPerfiil.menuAction())
        self.menubar.addAction(self.menuMatriz_SOD.menuAction())
        self.botao_sistema_consulta.clicked.connect(self.abre_tela_sistema)
        self.menuSistemas.triggered.connect(self.abre_tela_sistema)
        self.botao_perfil_consulta.clicked.connect(self.abre_tela_perfil)
        self.botao_matriz_consulta.clicked.connect(self.abre_tela_matriz)
        self.botao_usuarios_consulta.clicked.connect(self.abre_tela_usuarios)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuSistemas.setTitle(_translate("MainWindow", "Sistemas"))
        self.menuPerfiil.setTitle(_translate("MainWindow", "Perfiil"))
        self.menuMatriz_SOD.setTitle(_translate("MainWindow", "Matriz SOD"))
        self.menu_sistema_novo.setText(_translate("MainWindow", "Novo"))
        self.menu_sistema_consulta.setText(_translate("MainWindow", "Consulta"))
        self.menu_perfil_novo.setText(_translate("MainWindow", "Novo"))
        self.menu_perfil_Consulta.setText(_translate("MainWindow", "Consulta"))
        self.menu_matriz_novo.setText(_translate("MainWindow", "Novo"))
        self.menu_matriz_consulta.setText(_translate("MainWindow", "Consulta"))


    def abre_tela_sistema(self):
        self.Form = QtWidgets.QWidget()
        self.ui = tela_sistema()
        self.ui.setupUi(self.Form)
        self.Form.show()
        print('abre tela sistema')

    def abre_tela_perfil(self):
        self.Form = QtWidgets.QWidget()
        self.ui = tela_perfis()
        self.ui.setupUi(self.Form)
        self.Form.show()
        print('Tela Sistema')

    def abre_tela_matriz(self):
        self.Form = QtWidgets.QWidget()
        self.ui = tela_matriz()
        self.ui.setupUi(self.Form)
        self.Form.show()
        print('Tela Sistema')

    def abre_tela_usuarios(self):
        self.Form = QtWidgets.QWidget()
        self.ui = tela_usuario()
        self.ui.setupUi(self.Form)
        self.Form.show()
        print('Tela Sistema')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
