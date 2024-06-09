import sqlite3
import Dialog, MainWindow
import collections
import sys
from PySide6 import QtCore, QtGui, QtWidgets


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        # ? Start up tasks
        super(MainApp, self).__init__()
        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        # ? Connections
        self.ui.act_btn.clicked.connect(self.act_btn)

    def act_btn(self):
        self.dialog = DialogApp()
        self.dialog.exec()


class DialogApp(QtWidgets.QDialog):
    def __init__(self):
        super(DialogApp, self).__init__()
        self.ui = Dialog.Ui_Dialog()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainApp()
    window.show()

    sys.exit(app.exec())
