from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import StartView

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = StartView.Ui_Form()
ui.setupUi(Form)
app.exec_()
