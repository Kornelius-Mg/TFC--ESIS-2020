# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_form.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(783, 758)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 45, 376, 46))
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(60, 135, 661, 436))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(15, 15, 106, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(165, 15, 436, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(15, 120, 91, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(165, 105, 436, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(15, 300, 76, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(165, 285, 436, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(15, 390, 61, 30))
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(165, 375, 436, 46))
        self.textEdit.setObjectName("textEdit")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(15, 210, 91, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(165, 195, 436, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(60, 570, 661, 80))
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
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">ENREGISTRER UN UTILISATEUR</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "Nom Complet"))
        self.label_3.setText(_translate("Form", "Email"))
        self.label_4.setText(_translate("Form", "Telephone"))
        self.label_5.setText(_translate("Form", "Adresse"))
        self.label_6.setText(_translate("Form", "Mot de passe"))
        self.btn_exit.setText(_translate("Form", "Annuler"))
        self.btn_save.setText(_translate("Form", "Enregistrer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
