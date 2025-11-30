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
    
    def startReport(self):
        print("Starting report")

    def goToTable(self, listItem:QListWidgetItem):
        print(f"Table {listItem.data(1)} chosen")
        self.newWindow = CurTableViewWindow(listItem.data(1),self)
        self.hide()
        self.newWindow.show()

    def __requestTables(self) -> list:
        return list(i[0] for i in DBParser.execute("select table_name from information_schema.tables where table_schema = 'public' and table_type='BASE TABLE'"))

class AddRowDialog(QDialog):
    def __init__(self, cols:dict):
        super(AddRowDialog, self).__init__()
        self.ui = Ui_addRowView()
        self.ui.setupUi(self)
        self.contentWidget = QWidget(self)
        self.verticalLayout = QVBoxLayout(self.contentWidget)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.resize(800,600)

        for colName in cols.keys():
            hLayout = QHBoxLayout()
            label = QLabel(colName, self)
            cols[colName] = QComboBox(self)
            hLayout.addWidget(cols[colName])
            hLayout.addWidget(label)
    
    def closeEvent(self, arg__1):
        return super().closeEvent(arg__1)

class CurTableViewWindow(QMainWindow):
    def __init__(self, tableName:str, tablesViewWindow:TableViewWindow):
        super(CurTableViewWindow, self).__init__()
        self.ui = Ui_curTableView()
        self.ui.setupUi(self)

        self.tableName = tableName
        self.tablesViewWindow = tablesViewWindow

        print(f"Loading table {self.tableName}")

        self.ui.tableNameLabel.setText(niceTableNames[self.tableName])
        self.curTable = self.__requestTable()
        self.ui.tableWidget.setColumnCount(len(self.curTable[0]))
        self.ui.tableWidget.setRowCount(len(self.curTable))
        for rowTupleInd in range(len(self.curTable)):
            for colItemInd in range(len(self.curTable[rowTupleInd])):
                item = QTableWidgetItem(str(self.curTable[rowTupleInd][colItemInd]))
                self.ui.tableWidget.setItem(rowTupleInd, colItemInd,item)
        self.curTableHeaders = self.__requestTableHeaders()
        self.ui.tableWidget.setHorizontalHeaderLabels([niceTableHeaders[self.tableName][i[0]] for i in self.curTableHeaders])
        h = self.ui.tableWidget.horizontalHeader()
        h.setDefaultAlignment(Qt.AlignmentFlag.AlignLeft)

        self.ui.addBtn.triggered.connect(lambda x: self.addTableRow(self.curTable))
        self.ui.backBtn.triggered.connect(self.closeEvent)
        self.ui.saveBtn.triggered.connect(lambda x: self.saveChanges(self.curTable))
        self.ui.reportBtn.triggered.connect(self.startReport)

    def startReport(self):
        print("Starting report")

    def saveChanges(self,tableName:str):
        print(f"Saving changes in {tableName}")

    def addTableRow(self,tableName:str):
        print(f"Adding row to table {tableName}")
        d = {}
        for i in map(lambda x: x[0], self.curTableHeaders):
            d[i] = ""
        self.dialog = AddRowDialog(d)
        self.dialog.show()
        # self.setWindowModality(Qt.WindowModality.WindowModal)

    def __requestTableHeaders(self):
        return DBParser.execute(
            "select column_name from information_schema.columns "+
            f"where table_schema='public' and table_name='{self.tableName}';")

    def __requestTable(self):
        return DBParser.execute(f"select * from {self.tableName};")

    def closeEvent(self, event):
        self.tablesViewWindow.show()
        return super().closeEvent(event)

