# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'randomFinal.ui'
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


class Ui_randomFinal(object):
    def setupUi(self, randomFinal):
        if not randomFinal.objectName():
            randomFinal.setObjectName(u"randomFinal")
        randomFinal.resize(400, 300)
        self.gridLayout = QGridLayout(randomFinal)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(randomFinal)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.saveButton = QPushButton(self.frame)
        self.saveButton.setObjectName(u"saveButton")

        self.gridLayout_2.addWidget(self.saveButton, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)


        self.retranslateUi(randomFinal)

        QMetaObject.connectSlotsByName(randomFinal)
    # setupUi

    def retranslateUi(self, randomFinal):
        randomFinal.setWindowTitle(QCoreApplication.translate("randomFinal", u"Form", None))
        self.label.setText(QCoreApplication.translate("randomFinal", u"Name", None))
        self.saveButton.setText(QCoreApplication.translate("randomFinal", u"Save", None))
    # retranslateUi

