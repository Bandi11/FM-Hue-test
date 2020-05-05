# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_mainwidget(object):
    def setupUi(self, mainwidget):
        if not mainwidget.objectName():
            mainwidget.setObjectName(u"mainwidget")
        mainwidget.resize(400, 300)
        self.gridLayout = QGridLayout(mainwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.welcome = QLabel(mainwidget)
        self.welcome.setObjectName(u"welcome")
        font = QFont()
        font.setPointSize(22)
        self.welcome.setFont(font)
        self.welcome.setScaledContents(True)
        self.welcome.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.welcome, 0, 0, 1, 1)


        self.retranslateUi(mainwidget)

        QMetaObject.connectSlotsByName(mainwidget)
    # setupUi

    def retranslateUi(self, mainwidget):
        mainwidget.setWindowTitle(QCoreApplication.translate("mainwidget", u"Form", None))
        self.welcome.setText(QCoreApplication.translate("mainwidget", u"Farnsworth-Munsell 100 Hue test", None))
    # retranslateUi

