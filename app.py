import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic
import constant, inference_engine

qtCreatorFile = "homepage.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

ram_cond = ["", "{} {} {}".format("ram", constant.LESS_THAN, 5),
                "{} {} {} {} {}".format("ram", constant.GREATER_THAN, 5, constant.LESS_THAN, 10),
                "{} {} {}".format("ram", constant.GREATER_THAN, 10)]
rom_cond = ["", "{} {} {}".format("rom", constant.LESS_THAN, 32.1),
                "{} {} {} {} {}".format("rom", constant.GREATER_THAN, 32.1, constant.LESS_THAN, 64.1),
                "{} {} {}".format("rom", constant.GREATER_THAN, 64.1)]
screen_cond = ["", "{} {} {}".format("screen", constant.LESS_THAN, 5.01),
                "{} {} {} {} {}".format("screen", constant.GREATER_THAN, 5.01, constant.LESS_THAN, 6.51),
                "{} {} {}".format("screen", constant.GREATER_THAN, 6.51)]
mcam_cond = ["", "{} {} {}".format("main_camera", constant.LESS_THAN, 40.5),
                "{} {} {} {} {}".format("main_camera", constant.GREATER_THAN, 40.5, constant.LESS_THAN, 80),
                "{} {} {}".format("main_camera", constant.GREATER_THAN, 80)]
excam_cond = ["", "{} {} {}".format("extra_camera", constant.LESS_THAN, 30),
                "{} {} {}".format("extra_camera", constant.GREATER_THAN, 30)]
bat_cond = ["", "{} {} {}".format("battery", constant.LESS_THAN, 3005),
                "{} {} {} {} {}".format("battery", constant.GREATER_THAN, 3005, constant.LESS_THAN, 4005),
                "{} {} {}".format("battery", constant.GREATER_THAN, 4005)]
price_cond = ["", "{} {} {}".format("price", constant.LESS_THAN, 10.1),
                "{} {} {} {} {}".format("price", constant.GREATER_THAN, 10.1, constant.LESS_THAN, 20.1),
                "{} {} {} {} {}".format("price", constant.GREATER_THAN, 20.1, constant.LESS_THAN, 30.1),
                "{} {} {}".format("price", constant.GREATER_THAN, 30.1)]

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

        params = [ram, rom, screen, mcam, excam, bat, price]
        # for param in params:
        #     if param == 0:
        #         print(itemID for itemID in inference_engine(ram_cond[1]) if
        #             itemID in inference_engine(rom_cond[1]))
        # print(inference_engine(rom_cond[1]))  
        if ram == 1:
            init_condition = ram_cond[1]
            listID_ram = inference_engine.run(init_condition)
            print(listID)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Homepage()
    sys.exit(app.exec_())
