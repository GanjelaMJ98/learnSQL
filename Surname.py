import sys
from PyQt5 import QtWidgets
import modelSurname
import api
import sqlite3

conn = sqlite3.connect('PhoneBookDB.db')
cursor = conn.cursor()

class ExampleName(QtWidgets.QMainWindow, modelSurname.Ui_MainWindow):
    currentItemRow = None
    currentItemColumn = None
    currentItemText = None
    deleteIndex = None
    searchText = None
    updateFlag = 0
    newItemText = None
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Load_but.clicked.connect(self.loadData)
        self.Delete_but.clicked.connect(self.Delete)
        self.Search_but.clicked.connect(self.Search)
        self.Update_but.clicked.connect(self.Update)
        self.Table.clicked.connect(self.onClickTable)
        self.Search_t.textChanged.connect(self.onTextSearch)
        self.Table.itemChanged.connect(self.cellChangedTable)

    def cellChangedTable(self, item):
        if self.updateFlag == 1:
            self.updateFlag = 0
            self.newItemText = item.text()
            id = str(self.SearchIndexInTable(item.row()))
            api.windowSurnameUpdate(self.newItemText,id)
        else:
            return
    def onClickTable(self, item):
        self.currentItemRow = item.row()
        self.currentItemColumn = item.column()
        self.deleteIndex = self.SearchIndexInTable(item.row(), item.column())
        self.currentItemText = self.Table.item(item.row(),item.column()).text()
    def SearchIndexInTable(self,row,column = None):
        index_row = row
        index_column = 0
        return(self.Table.item(index_row, index_column).text())

    def loadData(self,name = False):
        if name is not False:
            sql = api.windowSurnameLoadTable(name)
            res = conn.execute(sql)
        else:
            sql = api.windowSurnameLoadTable()
            res = conn.execute(sql)
        self.Table.setRowCount(0)
        for row_number, row_data in enumerate(res):
            self.Table.insertRow(row_number)
            for colum_number , data in enumerate(row_data):
                self.Table.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(data)))
    def Delete(self):
        api.windowSurnameDelete(self.deleteIndex)
    def Update(self):
        self.updateFlag = 1

    def onTextSearch(self, text):
        self.searchText = text
    def Search(self):
        self.loadData(self.searchText)




def main():
        app = QtWidgets.QApplication(sys.argv)
        Surname = ExampleName()
        Surname.show()
        Surname.loadData()
        app.exec_()

if __name__ == '__main__':
        main()