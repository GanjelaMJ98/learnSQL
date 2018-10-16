import sys
from PyQt5 import QtWidgets
import subprocess
import model            #файл дизайна
import api
import sqlite3

conn = sqlite3.connect('PhoneBookDB.db')
cursor = conn.cursor()

#TODO: Убрать глобальные переменные
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
    currentItemRow = None
    currentItemColumn = None
    currentItemText = None
    newItemText = None
    deleteIndex = None
    updateFlag = 0
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле model.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.LoadDB_but.clicked.connect(self.loadData) #обработчик кнопки
        self.updateComboBox()
        # Основные кнопки
        self.Search_but.clicked.connect(self.Search_data)
        self.Add_but.clicked.connect(self.Add_data)
        self.Update_but.clicked.connect(self.Update)
        self.Delete_but.clicked.connect(self.Delete)
        # Ввод текста
        self.ID_t.textChanged.connect(self.onTextID)
        self.Surname_t.textChanged.connect(self.onTextSurname)
        self.Name_t.textChanged.connect(self.onTextName)
        self.Patron_t.textChanged.connect(self.onTextPatron)
        self.Street_t.textChanged.connect(self.onTextStreet)
        self.Bild_t.textChanged.connect(self.onTextBild)
        self.Block_t.textChanged.connect(self.onTextBlock)
        self.Appr_t.textChanged.connect(self.onTextAppr)
        self.Number_t.textChanged.connect(self.onTextNumber)
        # Запуск диалоговых окон
        self.Sur_ok.clicked.connect(self.Surname)
        self.Name_ok.clicked.connect(self.Name)
        self.Patron_ok.clicked.connect(self.Patron)
        self.Street_ok.clicked.connect(self.Street)
        # Действия с таблицей
        self.Table.clicked.connect(self.onClickTable)
        self.Table.itemChanged.connect(self.cellChangedTable)

    def Surname(self):
        subprocess.run(["python", "Surname.py"])
    def Name(self):
        subprocess.run(["python", "Name.py"])
    def Patron(self):
        subprocess.run(["python", "Patron.py"])
    def Street(self):
        subprocess.run(["python", "Street.py"])


    def loadData(self,sql):
        sql = api.searchMain()
        res = conn.execute(sql)
        self.Table.setRowCount(0)
        for row_number, row_data in enumerate(res):
            self.Table.insertRow(row_number)
            for colum_number , data in enumerate(row_data):
                self.Table.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(data)))
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
        self.Update_all()
    def Delete(self):
        api.DeleteByID(self.deleteIndex)
        #api.DeleteByID(currentID)
    def Update(self):
        self.updateFlag = 1

    def cellChangedTable(self,item):
        if self.updateFlag == 1:
            self.updateFlag = 0
            self.newItemText = item.text()
            api.updateMain(self.newItemText,self.currentItemText,self.currentItemColumn,self.SearchIndexInTable(item.row(),item.column()))
            self.Update_all()
        else:
            return

#_________Обновление выпадающих списков_______
    def onClickTable(self, item):
        self.currentItemRow = item.row()
        self.currentItemColumn = item.column()
        self.deleteIndex = self.SearchIndexInTable(item.row(), item.column())
        self.currentItemText = self.Table.item(item.row(),item.column()).text()
    def SearchIndexInTable(self, row, column):
        index_row = row
        index_column = 0
        return (self.Table.item(index_row, index_column).text())


    def Update_all(self):
        self.updateComboBox()
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


    def onTextID(self, text):
        textID.append(text)
        global currentID
        currentID = textID[-1]
        self.deleteIndex = textID[-1]
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


    def TextUpdateSurname(self, text):
        self.Surname_t.setText(text)
    def TextUpdateName(self, text):
        self.Name_t.setText(text)
    def TextUpdatePatron(self, text):
        self.Patron_t.setText(text)
    def TextUpdateStreet(self, text):
        self.Street_t.setText(text)







def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':
    main()