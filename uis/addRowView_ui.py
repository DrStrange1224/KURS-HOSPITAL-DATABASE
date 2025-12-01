# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addRowView.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QSizePolicy, QVBoxLayout, QWidget)

class Ui_addRowView(object):
    def setupUi(self, addRowView):
        if not addRowView.objectName():
            addRowView.setObjectName(u"addRowView")
        addRowView.resize(400, 296)
        self.verticalLayout = QVBoxLayout(addRowView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")

        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(addRowView)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(addRowView)
        self.buttonBox.accepted.connect(addRowView.accept)
        self.buttonBox.rejected.connect(addRowView.reject)

        QMetaObject.connectSlotsByName(addRowView)
    # setupUi

    def retranslateUi(self, addRowView):
        addRowView.setWindowTitle(QCoreApplication.translate("addRowView", u"Dialog", None))
    # retranslateUi

