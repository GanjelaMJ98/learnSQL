import sys
from PyQt5 import QtWidgets

import model # Это наш конвертированный файл дизайна
import api
import sqlite3

conn = sqlite3.connect('PhoneBookDB.db')
cursor = conn.cursor()

class ExampleApp(QtWidgets.QMainWindow, model.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле model.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.Sur_ok.clicked.connect(self.loadData) #обработчик кнопки
        self.updateComboDox()


    def updateComboDox(self):
        surnames = api.searchOnlySurname()
        self.comboSurname.addItems(surnames)
        self.comboSurname.activated[str].connect(self.TextUpdateSurname)

        names = api.searchOnlyName()
        self.comboName.addItems(names)
        self.comboName.activated[str].connect(self.TextUpdateName)

        patrons = api.searchOnlyPatron()
        self.comboPatron.addItems(patrons)
        self.comboPatron.activated[str].connect(self.TextUpdatePatron)

        streets = api.searchOnlyStreet()
        self.comboStreet.addItems(streets)
        self.comboStreet.activated[str].connect(self.TextUpdateStreet)


    def TextUpdateSurname(self, text):
        self.Surname_t.setText(text)

    def TextUpdateName(self, text):
        self.Name_t.setText(text)

    def TextUpdatePatron(self, text):
        self.Patron_t.setText(text)

    def TextUpdateStreet(self, text):
        self.Street_t.setText(text)

    def loadData(self,sql):
        sql = api.searchMain()
        res = conn.execute(sql)
        self.Table.setRowCount(0)
        for row_number, row_data in enumerate(res):
            self.Table.insertRow(row_number)
            for colum_number , data in enumerate(row_data):
                self.Table.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(data)))
                print(type(data))


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':
    main()