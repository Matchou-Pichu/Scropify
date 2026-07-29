import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
import Scrotify


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("dialog.ui", self)
        self.DownloadButton.clicked.connect(self.pushButton)
        self.progressBar.setValue(0)

    def listableLinks(self):
        listLink = []
        unarrangedList = self.links.toPlainText() + ' '
        rawStr = ''
        for l in unarrangedList:
            if (l == ',') | (l == ' '):
                listLink.append(rawStr)
                rawStr = '' 
            else:
                rawStr = rawStr + l
        return listLink

    def pushButton(self):
        Scrotify.scroptify(self.listableLinks(), self.progressBar)
        self.progressBar.setValue(100)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()