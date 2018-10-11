# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modelName.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 407)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Table = QtWidgets.QTableWidget(self.centralwidget)
        self.Table.setGeometry(QtCore.QRect(10, 40, 291, 301))
        self.Table.setRowCount(10)
        self.Table.setColumnCount(2)
        self.Table.setObjectName("Table")
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(1, item)
        self.Search_but = QtWidgets.QPushButton(self.centralwidget)
        self.Search_but.setGeometry(QtCore.QRect(10, 350, 75, 23))
        self.Search_but.setObjectName("Search_but")
        self.Delete_but = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_but.setGeometry(QtCore.QRect(100, 350, 75, 23))
        self.Delete_but.setObjectName("Delete_but")
        self.OK_But = QtWidgets.QPushButton(self.centralwidget)
        self.OK_But.setGeometry(QtCore.QRect(230, 350, 75, 23))
        self.OK_But.setObjectName("OK_But")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 111, 21))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "name_id"))
        item = self.Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        self.Search_but.setText(_translate("MainWindow", "Search"))
        self.Delete_but.setText(_translate("MainWindow", "Delete"))
        self.OK_But.setText(_translate("MainWindow", "OK"))
        self.label.setText(_translate("MainWindow", "NAMES"))

