import sqlite3
import collections
import sys
import threading
import subprocess

import Dialog, MainWindow
from PySide6 import QtCore, QtGui, QtWidgets


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        # ? Start up tasks
        super(MainApp, self).__init__()
        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        # ? Connections
        self.ui.add_edit_btn.clicked.connect(self.add_edit_btn)

    # & btn fucntions
    def act_btn(self):
        pass

    def del_btn(self):
        pass

    def add_edit_btn(self):
        self.dialog = DialogApp()
        self.dialog.exec()

    def ping_btn(self):
        pass

    def flush_btn(self):
        pass

    def dhcp_btn(self):
        pass

    def release_btn(self):
        pass

    # & get adapter function : get all adapters in the computer for easy access
    # & defualt adapter is Wi-fi
    def get_adp(self):
        pass

    # & logging function : writes logs inside the log textfeild after any task is finished for clarity, might contain errors also
    def log(self, message):
        pass

    # & dns table functions : functions for clicking and double clicking as well as general tasks
    def get_dns(self):
        pass


class DialogApp(QtWidgets.QDialog):
    def __init__(self):
        # ? Start up tasks
        super(DialogApp, self).__init__()
        self.ui = Dialog.Ui_Dialog()
        self.ui.setupUi(self)

        # ? connections

    # & btn functions
    def ok(self):
        pass

    def cancel(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainApp()
    window.show()

    sys.exit(app.exec())
