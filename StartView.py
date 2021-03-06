import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import MainView
import threading

class Ui_Form(object):
    def setupUi(self, Form):
        self.MainView = MainView.Main_Form()
        self.mainApp = QtWidgets.QApplication(sys.argv)
        self.mainForm = QtWidgets.QWidget()
        self.form = Form
        Form.setObjectName("Form")
        Form.resize(400, 159)
        Form.setWindowIcon(QtGui.QIcon('data\icon.png'))
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 90, 131, 28))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 90, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 40, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.show()
        self.pushButton.clicked.connect(self.loadButton)
        self.pushButton_2.clicked.connect(self.learnButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Menu"))
        self.pushButton.setText(_translate("Form", "Load neural network"))
        self.pushButton_2.setText(_translate("Form", "Start learning"))
        self.label.setText(_translate("Form", "Choose what you want to do"))


    def loadButton(self):
        try:
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            files, _ = QtWidgets.QFileDialog.getOpenFileNames()
            path = str(QtCore.QDir.toNativeSeparators(files[0]))
            self.form.hide()
            self.MainView.controller.load_data()
            self.form = QtWidgets.QWidget()
            self.MainView.setupUi(self.form)
            self.MainView.controller.normalize_data()
            self.MainView.controller.split_data()
            self.MainView.controller.load_network(path)
        except:
            print("Wrong neural network path")

    def learnButton(self):
        learnThread = threading.Thread(target=self.MainView.initialize())
        learnThread.start()
        learnThread.join()
        self.form.hide()
        self.form = QtWidgets.QWidget()
        self.MainView.setupUi(self.form)