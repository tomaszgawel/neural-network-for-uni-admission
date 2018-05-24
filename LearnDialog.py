from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Dialog_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(475, 160)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, -1, 471, 161))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        Form.show()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Learning process has started, please hold on"))

def showDialog(app, Form):
    ui = Dialog_Form()
    ui.setupUi(Form)
    app.exec_()

# app = QtWidgets.QApplication(sys.argv)
# Form = QtWidgets.QWidget()
# ui = Ui_Form()
# ui.setupUi(Form)
# Form.show()
# app.exec_()

