from tkinter import *
from tkinter.font import Font
from db import *

class App(Tk):
    """
    Main
    """
    selectedTable = ""
    def __init__(self):
        super().__init__()
        self.title("Hospital DB")
        self.geometry(f"{1000}x{800}+{0}+{0}")

        self.option_add('*tearOff', FALSE)

        self.container = Frame(self)
        self.container.config(background="#FF0000")
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        DBParser.init('config.ini', 'postgresql')

        self.frames = {}
        self.initFrames(TablesListFrame, TableRowsListFrame)

        self.showFrame("TablesListFrame")
    
    def initFrames(self,*frameClasses:type):
        for FrameClass in frameClasses:
            if not (Frame in FrameClass.__bases__):
                raise TypeError('Expected list of classes')
            self.frames[FrameClass.__name__] = FrameClass(master=self.container, controller=self)

    def showFrame(self, frameName:str):
        if not self.frames.keys().__contains__(frameName):
            raise KeyError(f'Frame with name {frameName} is not found')
        for i in self.frames.values():
            i.pack_forget()
        self.frames[frameName].tkraise()
        self.frames[frameName].pack(side="top", fill="both", expand=True)

class TablesListFrame(Frame):
    def __init__(self, master, controller):
        super(TablesListFrame, self).__init__(master=master)
        self.config(bg="#00ff4c")

        tablesListEl = Listbox(self, font=Font(family="Helvetica", size=18))

        scrollBarEl = Scrollbar(self, orient="vertical")
        scrollBarEl.config(command=tablesListEl.yview)

        def onListElClick(e):
            for i in tablesListEl.curselection():
                controller.selectedTable = tablesListEl.get(i)
            controller.showFrame("TableRowsListFrame")
        tablesListEl.config(bg='#3D3D3D', yscrollcommand=scrollBarEl.set)
        tablesListEl.bind('<Double-1>', onListElClick)

        tablesListEl.grid(row=0, column=0, padx=(10,0), pady=10, sticky='nsew')
        scrollBarEl.grid(row=0, column=1, padx=(0,10), pady=10, sticky='ns')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.__requestTablesList()
        for i in self.tablesList:
            tablesListEl.insert(END, i)
    
    def __requestTablesList(self):
        res = DBParser.execute("select table_name from information_schema.tables where table_schema = 'public' and table_type='BASE TABLE'")
        self.tablesList = list(i[0] for i in res)

class TableRowsListFrame(Frame):
    def __init__(self, master, controller:App):
        super(TableRowsListFrame, self).__init__(master=master)
        __class__.controller = controller

    def returnToTableList(self):
        __class__.controller.showFrame("TablesListFrame")
    
    def addRow(self):
        pass

    def saveChanges(self):
        pass

    def startReport(self):
        pass

    def tkraise(self):
        super().tkraise()
        print("Started")
        
        #======MENUBAR======
        self.menubar = Menu(self)
        self.fileMenu = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.fileMenu,label="Действия")
        self.fileMenu.add_command(label='Вернуться',command=self.returnToTableList)
        self.fileMenu.add_command(label='Добавить запись',command=self.addRow)
        self.fileMenu.add_command(label='Сохранить изменения',command=self.saveChanges)
        self.fileMenu.add_command(label='Создать отчет',command=self.startReport)
        self.controller.config(menu=self.menubar)

        #======TABLEFRAME======
        self.fullTableFrame = Frame(self)
        self.tableHeaders = self.__requestTableHeaders()
        self.tableContent = self.__requestTable()

        h = Scrollbar(self,orient="horizontal")
        v = Scrollbar(self,orient="vertical",command=self.onScroll)

        colNames = list(map(lambda x: x[0],self.tableHeaders))
        self.columns = list()
        for colInd in range(len(colNames)):
            header = Label(self.fullTableFrame, text=colNames[colInd],font=Font(family="Helvetica",size=16))
            column = Listbox(self.fullTableFrame,
                             font=Font(family="Helvetica",size=16),
                             yscrollcommand=v.set)
            column.bind("<MouseWheel>",self.onMouseWheel)
            for i in self.tableContent:
                print(f"{colInd} = {i[colInd]}")
                if i[colInd] == None:
                    column.insert(END,"[null]")
                column.insert(END,i[colInd])
            header.grid(column=colInd,row=0)
            column.grid(column=colInd,row=1)
            self.fullTableFrame.grid_columnconfigure(colInd,weight=1)
            self.columns.append(column)
        
        # h.pack(side='bottom',anchor='s',fill='x',expand=1)
        v.pack(side='right',anchor='e',fill='y',expand=1)

        self.fullTableFrame.grid_rowconfigure(0,weight=1)
        self.fullTableFrame.grid_rowconfigure(1,weight=1)
        self.fullTableFrame.pack()
    
    def onScroll(self,*args):
        for c in self.columns:
            c.yview(*args)
    
    def onMouseWheel(self,event):
        for c in self.columns:
            c.yview("scroll",event.delta,"units")
        return "break"
    
    def __requestTableHeaders(self) -> list:
        res = DBParser.execute(
            f"select column_name from information_schema.columns where table_schema='public' and table_name='{__class__.controller.selectedTable}';")
        print(res)
        return res

    def __requestTable(self):
        res = DBParser.execute(f"select * from {__class__.controller.selectedTable};")
        print(res)
        return res