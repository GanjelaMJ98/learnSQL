import sys
from PyQt5 import QtWidgets
import subprocess
import model # Это наш конвертированный файл дизайна
import api
import sqlite3


conn = sqlite3.connect('PhoneBookDB.db')
cursor = conn.cursor()

textID = list()
textSurname = list()
textName = list()
textPatron = list()
textStreet = list()
textBild = list()
textBlock = list()
textAppr = list()
textNumber = list()

currentID = str()
currentSurname = str()
currentName = str()
currentPatron = str()
currentStreet = str()
currentBild = str()
currentBlock = str()
currentAppr = str()
currentNumber = str()

class ExampleApp(QtWidgets.QMainWindow, model.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле model.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.LoadDB_but.clicked.connect(self.loadData) #обработчик кнопки
        self.updateComboBox()

        self.Search_but.clicked.connect(self.Search_data)
        self.Add_but.clicked.connect(self.Add_data)
        self.Update_but.clicked.connect(self.Update_all)
        self.Delete_but.clicked.connect(self.Delete)

        self.ID_t.textChanged.connect(self.onTextID)
        self.Surname_t.textChanged.connect(self.onTextSurname)
        self.Name_t.textChanged.connect(self.onTextName)
        self.Patron_t.textChanged.connect(self.onTextPatron)
        self.Street_t.textChanged.connect(self.onTextStreet)
        self.Bild_t.textChanged.connect(self.onTextBild)
        self.Block_t.textChanged.connect(self.onTextBlock)
        self.Appr_t.textChanged.connect(self.onTextAppr)
        self.Number_t.textChanged.connect(self.onTextNumber)


        self.Sur_ok.clicked.connect(self.Surname)
        self.Name_ok.clicked.connect(self.Name)
        self.Patron_ok.clicked.connect(self.Patron)
        self.Street_ok.clicked.connect(self.Street)

    def Surname(self):
        subprocess.run(["python", "Surname.py"])
    def Name(self):
        subprocess.run(["python", "Name.py"])
    def Patron(self):
        subprocess.run(["python", "Patron.py"])
    def Street(self):
        subprocess.run(["python", "Street.py"])
'''
#_________Поиск по одному признаку____________
    def Search_whereSurname(self):
        sql = api.searchSurname(currentSurname)
        res = conn.execute(sql)
        self.Table.setRowCount(0)
        for row_number, row_data in enumerate(res):
            self.Table.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.Table.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
    def Search_whereName(self):
        sql = api.searchName(currentName)
        res = conn.execute(sql)
        self.Table.setRowCount(0)
        for row_number, row_data in enumerate(res):
            self.Table.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.Table.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
    def Search_wherePatron(self):
        sql = api.searchPatron(currentPatron)
        res = conn.execute(sql)
        self.Table.setRowCount(0)
        for row_number, row_data in enumerate(res):
            self.Table.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.Table.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
    def Search_whereStreet(self):
        sql = api.searchStreet(currentStreet)
        res = conn.execute(sql)
        self.Table.setRowCount(0)
        for row_number, row_data in enumerate(res):
            self.Table.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.Table.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
#_________Поиск по 4м признакам_______________
'''


    def Search_data(self):
        sql = api.NEWsearchMain(currentSurname,currentName,currentPatron,currentStreet,currentBild,currentBlock,currentAppr,currentNumber)
        res = conn.execute(sql)
        self.Table.setRowCount(0)
        for row_number, row_data in enumerate(res):
            self.Table.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.Table.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

    def Add_data(self):
        api.addMain(surname = currentSurname,name = currentName, patron = currentPatron,street = currentStreet, bild =currentBild, block = currentBlock, appr = currentAppr, number = currentNumber)

    def Delete(self):
        api.DeleteByID(currentID)
#_________Обновление выпадающих списков_______
    def updateComboBox(self):
        self.comboSurname.clear()
        self.comboName.clear()
        self.comboPatron.clear()
        self.comboStreet.clear()
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
#_________Обновление полей ввода текста_______
    def onTextID(self, text):
        textID.append(text)
        global currentID
        currentID = textID[-1]
    def onTextSurname(self, text):
        textSurname.append(text)
        global currentSurname
        currentSurname = textSurname[-1]
    def onTextName(self, text):
        textName.append(text)
        global currentName
        currentName = textName[-1]
    def onTextPatron(self, text):
        textPatron.append(text)
        global currentPatron
        currentPatron = textPatron[-1]
    def onTextStreet(self, text):
        textStreet.append(text)
        global currentStreet
        currentStreet = textStreet[-1]
    def onTextBild(self, text):
        textBild.append(text)
        global currentBild
        currentBild = textBild[-1]
    def onTextBlock(self, text):
        textBlock.append(text)
        global currentBlock
        currentBlock = textBlock[-1]
    def onTextAppr(self, text):
        textAppr.append(text)
        global currentAppr
        currentAppr = textAppr[-1]
    def onTextNumber(self, text):
        textNumber.append(text)
        global currentNumber
        currentNumber = textNumber[-1]


    def Update_all(self):
        self.updateComboBox()
    '''
    def saveTextSername(self):
        global currentSurname
        currentSurname = textSurname[-1]
    def saveTextName(self):
        global currentName
        currentName = textName[-1]
    def saveTextPatron(self):
        global currentPatron
        currentPatron = textPatron[-1]
    def saveTextStreet(self):
        global currentStreet
        currentStreet = textStreet[-1]
    '''
#__________Обновление поля ввода текста через выпадающее окно____
    def TextUpdateSurname(self, text):
        self.Surname_t.setText(text)
    def TextUpdateName(self, text):
        self.Name_t.setText(text)
    def TextUpdatePatron(self, text):
        self.Patron_t.setText(text)
    def TextUpdateStreet(self, text):
        self.Street_t.setText(text)
#_____________Загрузка полной базы данных_____________________
    def loadData(self,sql):
        sql = api.searchMain()
        res = conn.execute(sql)
        self.Table.setRowCount(0)
        for row_number, row_data in enumerate(res):
            self.Table.insertRow(row_number)
            for colum_number , data in enumerate(row_data):
                self.Table.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(data)))
                #print(type(data))


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':
    main()