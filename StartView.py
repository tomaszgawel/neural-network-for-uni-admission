import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import DataNormalization
import DataController
import NeuralNetwork
import PyplotGraphs
import MainView
import Controller
import LearnDialog
import threading

class Ui_Form(object):
    def setupUi(self, Form):
        self.mainApp = QtWidgets.QApplication(sys.argv)
        self.mainForm = QtWidgets.QWidget()

        self.DialogApp = QtWidgets.QApplication(sys.argv)
        self.DialogForm = QtWidgets.QWidget()

        self.form = Form
        Form.setObjectName("Form")
        Form.resize(400, 159)
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
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Load neural network"))
        self.pushButton_2.setText(_translate("Form", "Start learning"))
        self.label.setText(_translate("Form", "Choose what you want to do"))


    def loadButton(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        files, _ = QtWidgets.QFileDialog.getOpenFileNames()
        path = str(QtCore.QDir.toNativeSeparators(files[0]))


    def learnButton(self):
        ui = MainView.Main_Form()
        mainThread = threading.Thread(target=MainView.showMainWindow(self.mainApp, self.mainForm, ui))
        mainThread.start()
        dialogThread = threading.Thread(target=LearnDialog.showDialog(self.DialogApp, self.DialogForm))
        dialogThread.start()
        mainThread.join()
        dialogThread.join()
        self.form.hide()
