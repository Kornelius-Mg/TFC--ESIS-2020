from main import Ui_MainWindow
from authentification import Ui_Form
import sys, pickle
from PyQt5 import QtWidgets
import session as session_mod

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

user = None

try:
    with open("session.dat", "rb") as fichier:
        session_deplicker = pickle.Unpickler(fichier)
        user = session_deplicker.load()
        print(user)
except:
    pass

if user != None:
    print("L'utilisateur de la session n'est plus None")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

sys.exit(app.exec_())