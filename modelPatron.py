# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modelPatron.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(310, 363)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Table = QtWidgets.QTableWidget(self.centralwidget)
        self.Table.setGeometry(QtCore.QRect(20, 40, 271, 221))
        self.Table.setRowCount(10)
        self.Table.setColumnCount(2)
        self.Table.setObjectName("Table")
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(1, item)
        self.Load_but = QtWidgets.QPushButton(self.centralwidget)
        self.Load_but.setGeometry(QtCore.QRect(20, 310, 75, 23))
        self.Load_but.setObjectName("Load_but")
        self.Delete_but = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_but.setGeometry(QtCore.QRect(140, 310, 75, 23))
        self.Delete_but.setObjectName("Delete_but")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 10, 111, 21))
        self.label.setObjectName("label")
        self.Update_but = QtWidgets.QPushButton(self.centralwidget)
        self.Update_but.setGeometry(QtCore.QRect(210, 310, 75, 23))
        self.Update_but.setObjectName("Update_but")
        self.Search_t = QtWidgets.QLineEdit(self.centralwidget)
        self.Search_t.setGeometry(QtCore.QRect(20, 280, 191, 20))
        self.Search_t.setObjectName("Search_t")
        self.Search_but = QtWidgets.QPushButton(self.centralwidget)
        self.Search_but.setGeometry(QtCore.QRect(210, 280, 75, 23))
        self.Search_but.setObjectName("Search_but")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Patron"))
        item = self.Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "patron_id"))
        item = self.Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Patron"))
        self.Load_but.setText(_translate("MainWindow", "Load"))
        self.Delete_but.setText(_translate("MainWindow", "Delete"))
        self.label.setText(_translate("MainWindow", "PATRONS"))
        self.Update_but.setText(_translate("MainWindow", "Update"))
        self.Search_but.setText(_translate("MainWindow", "Search"))

