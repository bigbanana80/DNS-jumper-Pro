import sqlite3
import sqlalchemy
import collections
import sys
import os
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
        self.ui.act_btn.clicked.connect(self.act)
        self.ui.add_edit_btn.clicked.connect(self.add_edit)
        self.ui.del_btn.clicked.connect(self.delete)
        self.ui.ping_btn.clicked.connect(self.ping)

        self.ui.flush_btn.clicked.connect(self.flush)
        self.ui.dhcp_btn.clicked.connect(self.dhcp)
        self.ui.release_btn.clicked.connect(self.release)

    # & btn fucntions
    def act(self):
        print("activated")

    def delete(self):
        print("DELETE")

    def add_edit(self):
        self.dialog = DialogApp()
        self.dialog.exec()

    def ping(self):
        print("PING THE DNS")

    def flush(self):
        print("FLUSHED")

    def dhcp(self):
        print("dhcp")

    def release(self):
        print("release and renew")

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
        self.ui.buttonBox.accepted.connect(self.ok)
        self.ui.buttonBox.rejected.connect(self.cancel)

    # & btn functions

    def ok(self):
        print("OK")

    def cancel(self):
        print("CANECL")


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)

    window = MainApp()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
