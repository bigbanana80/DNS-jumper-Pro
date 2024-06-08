import sqlite3
import Dialog, MainWindow
import collections
import sys
from PySide6 import QtCore, QtGui, QtWidgets


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainApp()
    window.show()

    sys.exit(app.exec())
