from nicer import *
from db import *
from py_uis.curTableView import Ui_curTableView
from py_uis.tablesView import Ui_tableViewWindow
from py_uis.addRowView import Ui_addRowView
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6 import QtCore

class TableViewWindow(QMainWindow):
    def __init__(self):
        super(TableViewWindow, self).__init__()
        self.ui = Ui_tableViewWindow()
        self.ui.setupUi(self)

        self.tablesList = self.__requestTables()
        for i in self.tablesList:
            listItem = QListWidgetItem(niceTableNames[i])
            listItem.setData(1,i)
            self.ui.listWidget.addItem(listItem)
        self.connect(self.ui.listWidget,
                    QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem *)"),
                    self.goToTable)

        self.ui.reportBtn.triggered.connect(self.startReport)
        self.updateStatus("ОК")
    
    def startReport(self):
        print("Starting report")

    def goToTable(self, listItem:QListWidgetItem):
        print(f"Table {listItem.data(1)} chosen")
        self.newWindow = CurTableViewWindow(listItem.data(1),self)
        self.hide()
        self.newWindow.show()

    def __requestTables(self) -> list:
        return list(i[0] for i in DBParser.execute("select table_name from information_schema.tables where table_schema = 'public' and table_type='BASE TABLE'"))
    
    def updateStatus(self, newStatus:str):
        self.ui.statusbar.showMessage(newStatus)

class AddRowDialog(QDialog):
    def __init__(self, cols:dict, tableName:str):
        super(AddRowDialog, self).__init__()
        self.ui = Ui_addRowView()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.cols = cols

        for colInd in range(len(cols.keys())):
            colName = list(cols.keys())[colInd]
            label = QLabel(niceTableHeaders[tableName][colName], self)
            self.ui.formLayout.setWidget(colInd, QFormLayout.ItemRole.LabelRole, label)
            self.cols[colName] = QLineEdit(self)
            self.ui.formLayout.setWidget(colInd, QFormLayout.ItemRole.FieldRole, self.cols[colName])

    def closeEvent(self, arg__1):
        self.setResult(0)
        return super().closeEvent(arg__1)

class ColFilter(QLineEdit):
    def init(self, parentw):
        self.parentw = parentw

    def focusOutEvent(self, arg__1):
        self.parentw.updateFilters()
        return super().focusOutEvent(arg__1)

class CurTableViewWindow(QMainWindow):
    def __init__(self, tableName:str, tablesViewWindow:TableViewWindow):
        super(CurTableViewWindow, self).__init__()
        self.ui = Ui_curTableView()
        self.ui.setupUi(self)

        self.tableName = tableName
        self.tablesViewWindow = tablesViewWindow

        print(f"Loading table {self.tableName}")

        ##START SETTING OF TABLE
        self.ui.tableNameLabel.setText(niceTableNames[self.tableName])
        self.curTable = self.__requestTable()
        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.tableWidget.setColumnCount(len(self.curTable[0]))
        self.ui.tableWidget.setRowCount(len(self.curTable) + 1)
        for rowTupleInd in range(len(self.curTable)):
            for colItemInd in range(len(self.curTable[rowTupleInd])):
                item = QTableWidgetItem(str(self.curTable[rowTupleInd][colItemInd]))
                self.ui.tableWidget.setItem(rowTupleInd + 1, colItemInd,item)
        
        ##SETTING HEADERS
        self.curTableHeaders = self.__requestTableHeaders()
        self.ui.tableWidget.setHorizontalHeaderLabels([niceTableHeaders[self.tableName][i] for i in self.curTableHeaders])
        h = self.ui.tableWidget.horizontalHeader()
        h.setDefaultAlignment(Qt.AlignmentFlag.AlignLeft)

        ##SETTING FILTERS
        self.colFilters = dict()
        for colInd in range(self.ui.tableWidget.columnCount()):
            self.colFilters[self.curTableHeaders[colInd]] = ColFilter("",self.ui.tableWidget)
            self.colFilters[self.curTableHeaders[colInd]].init(self)
            self.colFilters[self.curTableHeaders[colInd]].setPlaceholderText("Фильтр")
            self.colFilters[self.curTableHeaders[colInd]].returnPressed.connect(self.updateFilters)
            self.ui.tableWidget.setCellWidget(0,colInd,self.colFilters[self.curTableHeaders[colInd]])

        self.ui.addBtn.triggered.connect(self.addTableRow)
        self.ui.backBtn.triggered.connect(self.close)
        self.ui.saveBtn_2.triggered.connect(self.saveChanges)
        self.ui.reportBtn.triggered.connect(self.startReport)

        self.finalSqlRq = ""

    def updateFilters(self):
        for i in self.colFilters.values():
            print(i)

    def startReport(self):
        print("Starting report")

    def saveChanges(self):
        print(f"Saving changes in {self.tableName}")
        res = list()
        try:
            res = DBParser.execute(self.finalSqlRq)
            print(res)
        except:
            print("Error while table saving")
            self.tablesViewWindow.updateStatus("Ошибка при сохранении таблицы")
            #TODO logging

    def addTableRow(self):
        print(f"Adding row to table {self.tableName}")

        #creating dictionary: <header_name> : <null> (there will be qLineEdit)
        d = {}
        for i in map(lambda x: x[0], self.curTableHeaders):
            d[i] = ""

        self.dialog = AddRowDialog(d, self.tableName)

        wrap = lambda x: '\'' + x + '\''

        def onAccept():
            newVals = list(self.dialog.cols.values())
            self.finalSqlRq = self.finalSqlRq + f"insert into {self.tableName} values ({','.join(map(lambda x: wrap(x.text()), newVals))});\n"
            print(f"SQL request updated:\n{self.finalSqlRq}")
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(row + 1)
            for i in range(self.ui.tableWidget.columnCount()):
                self.ui.tableWidget.setItem(row, i, QTableWidgetItem(newVals[i].text()))

        def onReject():
            print("Row adding rejected")

        self.dialog.accepted.connect(onAccept)
        self.dialog.rejected.connect(onReject)

        self.dialog.show()

    def __requestTableHeaders(self):
        return list(map(lambda x: x[0], DBParser.execute(
            "select column_name from information_schema.columns "+
            f"where table_schema='public' and table_name='{self.tableName}';")))

    def __requestTable(self, filters:dict={}):
        if len(filters) == 0:
            return DBParser.execute(f"select * from {self.tableName};")
        else:
            pass

    def closeEvent(self, event):
        if len(self.finalSqlRq) == 0:
            self.tablesViewWindow.show()
            return super().closeEvent(event)
        
        self.doSaveDialog = QMessageBox()
        self.doSaveDialog.setInformativeText("Вы хотите сохранить изменения?")
        self.doSaveDialog.setStandardButtons(QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel)
        self.doSaveDialog.setDefaultButton(QMessageBox.StandardButton.Save)
        run = self.doSaveDialog.exec()

        if run == QMessageBox.StandardButton.Save:
            self.saveChanges()
            event.accept()
            self.tablesViewWindow.show()
        elif run == QMessageBox.StandardButton.Cancel:
            event.ignore()
        elif run == QMessageBox.StandardButton.Discard:
            event.accept()
            self.tablesViewWindow.show()

