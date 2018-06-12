from PyQt5 import QtCore, QtGui, QtWidgets
import Controller

class Main_Form(object):
    def __init__(self):
        self.controller = Controller.Control()
        self.indexOfGraph = 0

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(511, 658)
        Form.setWindowIcon(QtGui.QIcon('data\icon.png'))
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
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(0, 250, 511, 380))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 509, 380))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 511, 383))
        self.label_6.setObjectName("label_6")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 630, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(418, 630, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.graph = QtGui.QPixmap("graphs/0.png")
        self.label_6.setPixmap(self.graph.scaled(511,383,
                                                 QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.pushButton_2.setEnabled(False)
        self.pushButton.clicked.connect(self.check_action)
        self.pushButton_2.clicked.connect(self.prevButton)
        self.pushButton_3.clicked.connect(self.nextButton)
        Form.show()



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "NeuroUni"))
        self.label.setText(_translate("Form", "Test your results"))
        self.label_2.setText(_translate("Form", "GRE"))
        self.label_3.setText(_translate("Form", "GPA"))
        self.label_4.setText(_translate("Form", "PRESTIGE"))
        self.label_5.setText(_translate("Form", "..."))
        self.pushButton.setText(_translate("Form", "CHECK"))
        self.label_6.setText(_translate("Form", ""))
        self.pushButton_2.setText(_translate("Form", "Prev"))
        self.pushButton_3.setText(_translate("Form", "Next"))

    def check_action(self):
        if self.lineEdit.text() == "" or self.lineEdit_2.text() =="" or self.lineEdit_3.text() =="":
            self.label_5.setText("<font color='Red'>Fill all fields</font>")
        else:
            try:
                self.controller.copy_data()
                self.controller.add_user_input_into_data(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text())
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.controller.normalize_data()
                out = self.controller.test_user_input()
                self.label_5.setText("You have "+(str(int(round(out[0][0],2)*100))+"%")+" chance!")
            except:
                self.label_5.setText("<font color='Red'>Wrong format</font>")


    def initialize(self):
        self.controller.load_data()
        self.controller.normalize_data()
        self.controller.split_data()
        self.controller.create_and_learn_naural_net()

    def load_network(self,path):
        self.controller.load_network(path)

    def nextButton(self):
        if self.indexOfGraph == 0:
            self.indexOfGraph = 1
            self.graph = QtGui.QPixmap("graphs/1.png")
            self.label_6.setPixmap(self.graph.scaled(511, 383,
                                                     QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(True)
        elif self.indexOfGraph == 1:
            self.indexOfGraph = 2
            self.graph = QtGui.QPixmap("graphs/2.png")
            self.label_6.setPixmap(self.graph.scaled(511, 383,
                                                     QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(False)

    def prevButton(self):
        if self.indexOfGraph == 1:
            self.indexOfGraph = 0
            self.graph = QtGui.QPixmap("graphs/0.png")
            self.label_6.setPixmap(self.graph.scaled(511, 383,
                                                     QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
            self.pushButton_2.setEnabled(False)
            self.pushButton_3.setEnabled(True)
        elif self.indexOfGraph == 2:
            self.indexOfGraph = 1
            self.graph = QtGui.QPixmap("graphs/1.png")
            self.label_6.setPixmap(self.graph.scaled(511, 383,
                                                     QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(True)