import sys
from PyQt5 import QtWidgets

import modelName # Это наш конвертированный файл дизайна
import api
import sqlite3
conn = sqlite3.connect('PhoneBookDB.db')
cursor = conn.cursor()

class ExampleName(QtWidgets.QMainWindow, modelName.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.Search_but.clicked.connect(self.loadData)  # обработчик кнопки
        #self.Table.clicked.connect(self.on_click)
        self.Table.itemChanged.connect(self.cell_changed)
        self.Table.itemClicked.connect(self.on_clicked)

    def cell_changed(self,item):
        print("aaa",item.text())
    def on_click(self,index):
        print("eeee",index)
    def on_clicked(self,index):
        print("row",index.row())
        print("colum", index.column())
        print(self.Table.item(1,1).text())

    def loadData(self,sql):
        sql = api.Name()
        res = conn.execute(sql)
        self.Table.setRowCount(0)
        for row_number, row_data in enumerate(res):
            self.Table.insertRow(row_number)
            for colum_number , data in enumerate(row_data):
                self.Table.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(data)))
                #print(type(data))


def main():
        app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
        Name = ExampleName()  # Создаём объект класса ExampleApp
        Name.show()  # Показываем окно
        app.exec_()  # и запускаем приложение

if __name__ == '__main__':
        main()