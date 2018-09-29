import sys
from PyQt5 import QtWidgets

import model # Это наш конвертированный файл дизайна
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
    def loadData(self):
        sql = """SELECT s.surname,
                    n.name,
                    p.patron,
                    st.street,
                    m.bild,
                    m.block,
                    m.appr,
                    m.number
                     FROM surname_t s, name_t n, patron_t p ,street_t st NATURAL JOIN main m """
        res = conn.execute(sql)
        self.Table.setRowCount(0)
        for row_number, row_data in enumerate(res):
            self.Table.insertRow(row_number)
            for colum_number , data in enumerate(row_data):
                self.Table.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(data))



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':
    main()