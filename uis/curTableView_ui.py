# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'curTableView.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_curTableView(object):
    def setupUi(self, curTableView):
        if not curTableView.objectName():
            curTableView.setObjectName(u"curTableView")
        curTableView.resize(800, 600)
        curTableView.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.backBtn = QAction(curTableView)
        self.backBtn.setObjectName(u"backBtn")
        self.saveBtn = QAction(curTableView)
        self.saveBtn.setObjectName(u"saveBtn")
        self.addBtn = QAction(curTableView)
        self.addBtn.setObjectName(u"addBtn")
        self.reportBtn = QAction(curTableView)
        self.reportBtn.setObjectName(u"reportBtn")
        self.saveBtn_2 = QAction(curTableView)
        self.saveBtn_2.setObjectName(u"saveBtn_2")
        self.contentWidget = QWidget(curTableView)
        self.contentWidget.setObjectName(u"contentWidget")
        self.gridLayout = QGridLayout(self.contentWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget = QTableWidget(self.contentWidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.tableNameLabel = QLabel(self.contentWidget)
        self.tableNameLabel.setObjectName(u"tableNameLabel")
        self.tableNameLabel.setStyleSheet(u"font: 18pt \"Helvetica\";padding-left: 10pt;")
        self.tableNameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tableNameLabel.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout.addWidget(self.tableNameLabel, 0, 0, 1, 1)

        curTableView.setCentralWidget(self.contentWidget)
        self.menubar = QMenuBar(curTableView)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        curTableView.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(curTableView)
        self.statusbar.setObjectName(u"statusbar")
        curTableView.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.backBtn)
        self.menu.addAction(self.saveBtn_2)
        self.menu.addAction(self.addBtn)
        self.menu.addAction(self.reportBtn)

        self.retranslateUi(curTableView)

        QMetaObject.connectSlotsByName(curTableView)
    # setupUi

    def retranslateUi(self, curTableView):
        curTableView.setWindowTitle(QCoreApplication.translate("curTableView", u"MainWindow", None))
        self.backBtn.setText(QCoreApplication.translate("curTableView", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f", None))
        self.saveBtn.setText(QCoreApplication.translate("curTableView", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.addBtn.setText(QCoreApplication.translate("curTableView", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.reportBtn.setText(QCoreApplication.translate("curTableView", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043e\u0442\u0447\u0435\u0442", None))
        self.saveBtn_2.setText(QCoreApplication.translate("curTableView", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.tableNameLabel.setText(QCoreApplication.translate("curTableView", u"UNKNOWN_TABLE", None))
        self.menu.setTitle(QCoreApplication.translate("curTableView", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u044f", None))
    # retranslateUi

