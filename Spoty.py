import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit

def findWholeWord(w):
        return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

class MyWindow(QWidget):

    def __init__(self, win):
        super().__init__()
        self.wind = win
        self.input = QLineEdit(self.wind)
        self.lbl = QLabel(self.wind)

    def changeColor(self, color):
        self.wind.setStyleSheet("background : " + color + ";")

    def checkSpotifyUrl(self):
        urls = self.input.text()
        if findWholeWord("https://open.spotify.com/album/")(urls) == None:
            self.input.setStyleSheet("background:#fc4242; font-weight:600; font-size: 10px")
        else:
            self.input.setStyleSheet("background:#79f7a5; font-weight:600; font-size: 10px")

    def build(self):
        self.wind.setWindowTitle("App, object approach")
        self.wind.setFixedWidth(800)
        self.wind.setFixedHeight(500)

        self.lbl.setGeometry(150, 20, 500, 50)
        self.lbl.setText("Coller les liens des albums juste en dessous")
        self.lbl.setStyleSheet("color:black; font-size:22px; padding-left:32px")

        self.input.setGeometry(150, 100, 500, 50)
        self.input.textChanged.connect(self.checkSpotifyUrl)
        self.input.setStyleSheet("font-size: 15px")

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = QWidget()
    myapp = MyWindow(root)
    myapp.build()
    myapp.changeColor("white")
    root.show()

    sys.exit(app.exec_())        