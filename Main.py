from PyQt5 import QtWidgets
import sys
import StartView

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = StartView.Ui_Form()
ui.setupUi(Form)
sys.exit(app.exec_())