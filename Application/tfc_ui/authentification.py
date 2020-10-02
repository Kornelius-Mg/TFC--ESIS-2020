# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'authentification.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(783, 585)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(225, 120, 361, 31))
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(60, 180, 661, 256))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(15, 60, 586, 31))
        self.lineEdit.setText("")
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(15, 165, 586, 31))
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(15, 180, 61, 46))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(15, 195, 586, 30))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(15, 90, 586, 30))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(60, 435, 661, 80))
        self.widget.setObjectName("widget")
        self.btn_exit = QtWidgets.QPushButton(self.widget)
        self.btn_exit.setGeometry(QtCore.QRect(497, 30, 106, 30))
        self.btn_exit.setAutoDefault(False)
        self.btn_exit.setDefault(False)
        self.btn_exit.setObjectName("btn_exit")
        self.btn_save = QtWidgets.QPushButton(self.widget)
        self.btn_save.setGeometry(QtCore.QRect(330, 27, 106, 31))
        self.btn_save.setAutoDefault(True)
        self.btn_save.setObjectName("btn_save")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">AUTHENTIFIER UTILISATEUR</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Adresse email"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Mot de passe"))
        self.btn_exit.setText(_translate("Form", "Annuler"))
        self.btn_save.setText(_translate("Form", "Connecter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
