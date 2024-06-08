# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHeaderView, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(827, 610)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.dns_table = QTableWidget(self.centralwidget)
        if (self.dns_table.rowCount() < 1):
            self.dns_table.setRowCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.dns_table.setVerticalHeaderItem(0, __qtablewidgetitem)
        self.dns_table.setObjectName(u"dns_table")
        self.dns_table.setGeometry(QRect(10, 10, 451, 571))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(480, 10, 341, 121))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.act_btn = QPushButton(self.groupBox)
        self.act_btn.setObjectName(u"act_btn")

        self.gridLayout.addWidget(self.act_btn, 0, 0, 1, 1)

        self.del_btn = QPushButton(self.groupBox)
        self.del_btn.setObjectName(u"del_btn")

        self.gridLayout.addWidget(self.del_btn, 0, 1, 1, 1)

        self.add_edit_btn = QPushButton(self.groupBox)
        self.add_edit_btn.setObjectName(u"add_edit_btn")

        self.gridLayout.addWidget(self.add_edit_btn, 1, 0, 1, 1)

        self.ping_btn = QPushButton(self.groupBox)
        self.ping_btn.setObjectName(u"ping_btn")

        self.gridLayout.addWidget(self.ping_btn, 1, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(480, 150, 341, 121))
        self.commands_grid = QGridLayout(self.groupBox_2)
        self.commands_grid.setObjectName(u"commands_grid")
        self.flush_btn = QPushButton(self.groupBox_2)
        self.flush_btn.setObjectName(u"flush_btn")

        self.commands_grid.addWidget(self.flush_btn, 0, 0, 1, 1)

        self.dhcp_btn = QPushButton(self.groupBox_2)
        self.dhcp_btn.setObjectName(u"dhcp_btn")

        self.commands_grid.addWidget(self.dhcp_btn, 0, 1, 1, 1)

        self.release_btn = QPushButton(self.groupBox_2)
        self.release_btn.setObjectName(u"release_btn")

        self.commands_grid.addWidget(self.release_btn, 1, 0, 1, 1)

        self.adapters_cbox = QComboBox(self.groupBox_2)
        self.adapters_cbox.setObjectName(u"adapters_cbox")

        self.commands_grid.addWidget(self.adapters_cbox, 1, 1, 1, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(480, 280, 341, 281))
        self.logs = QTextEdit(self.groupBox_3)
        self.logs.setObjectName(u"logs")
        self.logs.setGeometry(QRect(10, 20, 321, 251))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 827, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"DNS Controls", None))
        self.act_btn.setText(QCoreApplication.translate("MainWindow", u"Activate", None))
        self.del_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.add_edit_btn.setText(QCoreApplication.translate("MainWindow", u"Add - Edit", None))
        self.ping_btn.setText(QCoreApplication.translate("MainWindow", u"Ping", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Commands", None))
        self.flush_btn.setText(QCoreApplication.translate("MainWindow", u"Flush", None))
        self.dhcp_btn.setText(QCoreApplication.translate("MainWindow", u"DHCP", None))
        self.release_btn.setText(QCoreApplication.translate("MainWindow", u"Release IP ( Auto Renew)", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Logs", None))
    # retranslateUi

