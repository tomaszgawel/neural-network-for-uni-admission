from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

import MainView
import Controller
import sys
import threading

class Main_Form(object):
    def __init__(self):
        self.controller = Controller.Control()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(522, 252)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(40, 100, 121, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 30, 521, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 100, 121, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(360, 100, 121, 31))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 70, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(250, 70, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(380, 70, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(0, 200, 521, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 150, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.check_action)
        Form.show()



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Test your results"))
        self.label_2.setText(_translate("Form", "GPA"))
        self.label_3.setText(_translate("Form", "GRE"))
        self.label_4.setText(_translate("Form", "PRESTIGE"))
        self.label_5.setText(_translate("Form", "..."))
        self.pushButton.setText(_translate("Form", "CHECK"))

    def check_action(self):
        self.controller.copy_data()
        print([self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text()])
        self.controller.add_user_input_into_data(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text())
        self.controller.normalize_data()
        print(str(self.controller.test_user_input()))
        # self.label_5.setText()

    def initialize(self):
        self.controller.load_data()
        self.controller.normalize_data()
        self.controller.split_data()
        self.controller.create_and_learn_naural_net()

    def load_network(self,path):
        self.controller.NN.load_neural_network(path)



