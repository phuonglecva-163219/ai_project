import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic
import constant

qtCreatorFile = "homepage.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class Homepage(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.result.clicked.connect(self.get_params)
        self.show()

    def get_params(self):
        ram = self.ram.currentIndex()
        rom = self.rom.currentIndex()
        screen = self.screen.currentIndex()
        mcam = self.mcam.currentIndex()
        excam = self.excam.currentIndex()
        bat = self.bat.currentIndex()
        price = self.price.currentIndex()
        print(ram, rom, screen, mcam, excam, bat, price)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Homepage()
    sys.exit(app.exec_())
