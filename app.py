import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic
import constant, inference_engine
import urllib.request

qtCreatorFile1 = "homepage.ui" # Enter file here.
qtCreatorFile2 = "phone.ui" # Enter file here.
qtCreatorFile3 = "rule_lv2.ui" # Enter file here.
Ui_MainWindow1, QtBaseClass1 = uic.loadUiType(qtCreatorFile1)
Ui_MainWindow2, QtBaseClass2 = uic.loadUiType(qtCreatorFile2)
Ui_MainWindow3, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)

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
game_cond = ["", "{} {} {}".format("game", constant.BAD, ""),
                "{} {} {}".format("game", constant.MEDIUM, ""),
                "{} {} {}".format("game", constant.GOOD, "")]
student_cond = ["", "{} {} {}".format("game", constant.BAD, ""),
                "{} {} {}".format("game", constant.GOOD, "")]

class Homepage(QtWidgets.QMainWindow, Ui_MainWindow1):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow1.__init__(self)
        self.setupUi(self)
        self.center()
        self.result.clicked.connect(self.find)
        self.level2.clicked.connect(self.switch_to_lv2)
        self.show()

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def switch_to_lv2(self):
        self.main = Level2()
        self.main.show()
        self.close()

    def find(self):
        ram = self.ram.currentIndex()
        rom = self.rom.currentIndex()
        screen = self.screen.currentIndex()
        mcam = self.mcam.currentIndex()
        excam = self.excam.currentIndex()
        bat = self.bat.currentIndex()
        price = self.price.currentIndex()

        params = [ram, rom, screen, mcam, excam, bat, price]
        if params == [0, 0, 0, 0, 0, 0, 0]:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please select at least 1 category!")
            x = msg.exec_()
        else:
            listCond = [ram_cond[ram], 
                        rom_cond[rom], 
                        screen_cond[screen],
                        mcam_cond[mcam],
                        excam_cond[excam],
                        bat_cond[bat],
                        price_cond[price]]
            listCond = [condition for condition in listCond if condition != ""]

            global listId
            listId = inference_engine.runAll(listCond)
            self.main = Result()
            self.main.show()

class Level2(QtWidgets.QMainWindow, Ui_MainWindow3):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow3.__init__(self)
        self.setupUi(self)
        self.center()
        self.result.clicked.connect(self.find)
        self.level1.clicked.connect(self.switch_to_lv1)
        self.show()

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def switch_to_lv1(self):
        self.main = Homepage()
        self.main.show()
        self.close()

    def find(self):
        game = self.game.currentIndex()
        student = self.student.currentIndex()

        params = [game, student]
        if params == [0, 0]:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please select at least 1 category!")
            x = msg.exec_()
        else:
            listCond = [game_cond[game],
                        student_cond[student]]
            listCond = [condition for condition in listCond if condition != ""]

            global listId
            listId = inference_engine.runAll(listCond)
            self.main = Result()
            self.main.show()

class Result(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)
        self.setGeometry(200, 100, 400, 600)
        self.setWindowTitle("Result")
        self.listwidget = QtWidgets.QListWidget()

        global listId
        for i in listId:
            self.listwidget.insertItem(i, inference_engine.getData(i)["name"])
        self.listwidget.clicked.connect(self.clicked)
        layout.addWidget(self.listwidget)

    def clicked(self, qmodelindex):
        global item
        item = self.listwidget.currentRow()
        self.main = Phone()
        self.main.move(900, 100)
        self.main.show()

class Phone(QtWidgets.QMainWindow, Ui_MainWindow2):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow2.__init__(self)
        self.setupUi(self)

        global listId, item
        phoneId = listId[item]
        img = QtGui.QImage()
        img_data = urllib.request.urlopen(inference_engine.getData(phoneId)["img"]).read()
        img.loadFromData(img_data)
        self.img.setPixmap(QtGui.QPixmap(img))
        self.name.setText(inference_engine.getData(phoneId)["name"])
        self.ram.setText(inference_engine.getData(phoneId)["ram"])
        self.rom.setText(inference_engine.getData(phoneId)["rom"])
        self.screen.setText(inference_engine.getData(phoneId)["screen"])
        self.cpu.setText(inference_engine.getData(phoneId)["cpu"])
        self.mcam.setText(inference_engine.getData(phoneId)["camera"])
        self.excam.setText(inference_engine.getData(phoneId)["selfie"])
        self.bat.setText(inference_engine.getData(phoneId)["pin"])
        self.price.setText(inference_engine.getData(phoneId)["price"])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Homepage()
    sys.exit(app.exec_())
