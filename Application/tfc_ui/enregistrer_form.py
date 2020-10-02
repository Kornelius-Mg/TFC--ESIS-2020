# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_form.ui'
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
        self.label.setGeometry(QtCore.QRect(180, 45, 361, 46))
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(60, 135, 661, 451))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(15, 15, 586, 31))
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(15, 105, 586, 31))
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(15, 300, 586, 30))
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(15, 375, 586, 61))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(15, 195, 586, 31))
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setFrame(False)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(15, 225, 586, 30))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(15, 180, 61, 46))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(15, 135, 586, 30))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(15, 45, 586, 30))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(15, 330, 586, 30))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(60, 615, 661, 80))
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
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">ENREGISTRER UTILISATEUR</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Nom complet"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "monadresse@email.com"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Telephone"))
        self.textEdit.setPlaceholderText(_translate("Form", "Adresse physique"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Mot de passe"))
        self.btn_exit.setText(_translate("Form", "Annuler"))
        self.btn_save.setText(_translate("Form", "Modifier"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
