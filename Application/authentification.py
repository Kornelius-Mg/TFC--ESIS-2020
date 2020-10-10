# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'authentification.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from models import Utilisateur
from session import set_session
from datas import login_user
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(783, 729)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 210, 361, 31))
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(60, 315, 661, 256))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(120, 60, 481, 61))
        self.lineEdit.setText("")
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 180, 481, 61))
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(15, 180, 91, 76))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("fonts/ic_lock_black_48dp.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(120, 240, 481, 30))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(120, 120, 481, 30))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(15, 45, 91, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("fonts/ic_email_black_36dp.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(60, 600, 661, 80))
        self.widget.setObjectName("widget")
        self.btn_exit = QtWidgets.QPushButton(self.widget)
        self.btn_exit.setGeometry(QtCore.QRect(497, 14, 136, 46))
        self.btn_exit.setAutoDefault(False)
        self.btn_exit.setDefault(False)
        self.btn_exit.setObjectName("btn_exit")
        self.btn_exit.clicked.connect(self.exit)
        self.btn_save = QtWidgets.QPushButton(self.widget)
        self.btn_save.setGeometry(QtCore.QRect(300, 12, 136, 46))
        self.btn_save.setAutoDefault(True)
        self.btn_save.setDefault(True)
        self.btn_save.setObjectName("btn_save")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(300, 30, 181, 151))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:/Users/Corneille Mungumwa/Pictures/armes/Armes/Pistolet/negatives/images/15.jpeg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.message_error = QtWidgets.QLabel(Form)
        self.message_error.setEnabled(False)
        self.message_error.setVisible(False)
        self.message_error.setGeometry(QtCore.QRect(150, 255, 406, 30))
        self.message_error.setWordWrap(True)
        self.message_error.setObjectName("message_error")

        self.btn_save.clicked.connect(self.login)

        self.form = Form

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
        self.message_error.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#dc0000;\">Login ou mot de passe invalide</span></p></body></html>"))

    def login(self):
        email = self.lineEdit.text()
        password = self.lineEdit_2.text()

        response = login_user(email=email, password=password)

        if response:
            self.exit()
        else:
            self.message_error.setVisible(True)
    
    def exit(self):
        self.form.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
