# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectReportView.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QDialog,
    QDialogButtonBox, QListWidget, QListWidgetItem, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_selectReportView(object):
    def setupUi(self, selectReportView):
        if not selectReportView.objectName():
            selectReportView.setObjectName(u"selectReportView")
        selectReportView.resize(400, 247)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(selectReportView.sizePolicy().hasHeightForWidth())
        selectReportView.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(selectReportView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(selectReportView)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy1)
        self.listWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listWidget.setAutoScroll(True)
        self.listWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listWidget.setItemAlignment(Qt.AlignmentFlag.AlignLeading)

        self.verticalLayout.addWidget(self.listWidget)

        self.buttonBox = QDialogButtonBox(selectReportView)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(selectReportView)
        self.buttonBox.accepted.connect(selectReportView.accept)
        self.buttonBox.rejected.connect(selectReportView.reject)

        QMetaObject.connectSlotsByName(selectReportView)
    # setupUi

    def retranslateUi(self, selectReportView):
        selectReportView.setWindowTitle(QCoreApplication.translate("selectReportView", u"Dialog", None))
    # retranslateUi

