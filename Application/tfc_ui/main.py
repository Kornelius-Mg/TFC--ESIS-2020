# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
import cv2
from opencvQt import App, Thread


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1226, 914)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(15, 15, 1186, 841))
        self.tabWidget.setObjectName("tabWidget")
        self.visual_tab = App()
        self.visual_tab.setObjectName("visual_tab")
        self.label_3 = QtWidgets.QLabel(self.visual_tab)
        self.label_3.setGeometry(QtCore.QRect(30, 765, 226, 31))
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(self.visual_tab)
        self.widget.setGeometry(QtCore.QRect(30, 15, 1141, 736))
        self.widget.setObjectName("widget")
        self.labelVisual = QtWidgets.QLabel(self.widget)
        self.labelVisual.setGeometry(QtCore.QRect(0, 0, 1141, 736))
        self.labelVisual.setObjectName("labelVisual")
        self.tabWidget.addTab(self.visual_tab, "")
        self.admin_tab = QtWidgets.QWidget()
        self.admin_tab.setObjectName("admin_tab")
        self.tableView = QtWidgets.QTableView(self.admin_tab)
        self.tableView.setGeometry(QtCore.QRect(30, 120, 961, 586))
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(self.admin_tab)
        self.label.setGeometry(QtCore.QRect(360, 30, 271, 46))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.admin_tab)
        self.pushButton.setGeometry(QtCore.QRect(1020, 120, 151, 31))
        self.pushButton.setStyleSheet("font-size : 12px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.admin_tab)
        self.pushButton_2.setGeometry(QtCore.QRect(1020, 195, 151, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.admin_tab)
        self.pushButton_3.setGeometry(QtCore.QRect(1020, 270, 151, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.admin_tab)
        self.label_2.setGeometry(QtCore.QRect(30, 735, 211, 30))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.admin_tab)
        self.label_4.setGeometry(QtCore.QRect(30, 780, 226, 16))
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.admin_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1226, 26))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuAides = QtWidgets.QMenu(self.menubar)
        self.menuAides.setObjectName("menuAides")
        self.menuAides_2 = QtWidgets.QMenu(self.menubar)
        self.menuAides_2.setObjectName("menuAides_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionA_propos = QtWidgets.QAction(MainWindow)
        self.actionA_propos.setObjectName("actionA_propos")
        self.actionoptions = QtWidgets.QAction(MainWindow)
        self.actionoptions.setObjectName("actionoptions")
        self.menuFichier.addAction(self.actionExit)
        self.menuAides.addAction(self.actionA_propos)
        self.menuAides.addAction(self.actionoptions)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuAides.menuAction())
        self.menubar.addAction(self.menuAides_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Status : Visualisation des images"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.visual_tab), _translate("MainWindow", "Visualisation"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">UTILISATEURS</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Nouvel utilisateur"))
        self.pushButton_2.setText(_translate("MainWindow", "Modifier"))
        self.pushButton_3.setText(_translate("MainWindow", "Supprimer"))
        self.label_2.setText(_translate("MainWindow", "Action: Gestion des utilisateurs"))
        self.label_4.setText(_translate("MainWindow", "Nombre d\'elements : 100"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.admin_tab), _translate("MainWindow", "Administration"))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
        self.menuAides.setTitle(_translate("MainWindow", "Parametres"))
        self.menuAides_2.setTitle(_translate("MainWindow", "Aides"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionA_propos.setText(_translate("MainWindow", "Source des images"))
        self.actionoptions.setText(_translate("MainWindow", "options"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
