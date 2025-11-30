# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tablesView.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QScrollArea,
    QSizePolicy, QStatusBar, QWidget)

class Ui_tableViewWindow(object):
    def setupUi(self, tableViewWindow):
        if not tableViewWindow.objectName():
            tableViewWindow.setObjectName(u"tableViewWindow")
        tableViewWindow.resize(699, 503)
        self.reportBtn = QAction(tableViewWindow)
        self.reportBtn.setObjectName(u"reportBtn")
        self.contentWidget = QWidget(tableViewWindow)
        self.contentWidget.setObjectName(u"contentWidget")
        self.gridLayout = QGridLayout(self.contentWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(self.contentWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 679, 440))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.listWidget = QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setItemAlignment(Qt.AlignmentFlag.AlignLeading)

        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        tableViewWindow.setCentralWidget(self.contentWidget)
        self.menubar = QMenuBar(tableViewWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 699, 22))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        tableViewWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(tableViewWindow)
        self.statusbar.setObjectName(u"statusbar")
        tableViewWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.reportBtn)

        self.retranslateUi(tableViewWindow)

        QMetaObject.connectSlotsByName(tableViewWindow)
    # setupUi

    def retranslateUi(self, tableViewWindow):
        tableViewWindow.setWindowTitle(QCoreApplication.translate("tableViewWindow", u"MainWindow", None))
        self.reportBtn.setText(QCoreApplication.translate("tableViewWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043e\u0442\u0447\u0435\u0442", None))
        self.menu.setTitle(QCoreApplication.translate("tableViewWindow", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u044f", None))
    # retranslateUi

