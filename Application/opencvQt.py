import cv2
import sys
from PyQt5.QtWidgets import  QWidget, QLabel, QApplication
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap


class Thread(QThread):
    changePixmap = pyqtSignal(QImage)

    def run(self):
        while True:
            face_cascade = cv2.CascadeClassifier("cascades/cascade.xml")
            cap = cv2.VideoCapture(0)
            while True:
                ret, frame = cap.read()

                face = face_cascade.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=1)

                for x, y, w, h in face:
                    cv2.rectangle(frame, (x,y), (w+x, h+y), (255,0,0), 2)

                if ret:
            #       https://stackoverflow.com/a/55468544/6622587
                    rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    h, w, ch = rgbImage.shape
                    bytesPerLine = ch * w
                    convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                    p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                    self.changePixmap.emit(p)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Visualiser caméras"
        self.left = 200
        self.top = 120
        self.width = 640
        self.height = 480
        self.initUI()

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, 1141, 736)
        self.resize(600, 400)
        # create a label
        self.label = QLabel(self)
        self.label.move(250, 150)
        self.label.resize(640, 480)
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = App()
    sys.exit(app.exec_())
    
