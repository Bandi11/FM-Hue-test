# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'colorLabel.ui'
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


class Ui_ColorLabel(object):
    def setupUi(self, ColorLabel):
        if not ColorLabel.objectName():
            ColorLabel.setObjectName(u"ColorLabel")
        ColorLabel.resize(100, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ColorLabel.sizePolicy().hasHeightForWidth())
        ColorLabel.setSizePolicy(sizePolicy)
        ColorLabel.setMaximumSize(QSize(100, 100))
        self.gridLayout = QGridLayout(ColorLabel)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(ColorLabel)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(231221, 3221321))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(1)
        self.label.setIndent(0)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.retranslateUi(ColorLabel)

        QMetaObject.connectSlotsByName(ColorLabel)
    # setupUi

    def retranslateUi(self, ColorLabel):
        ColorLabel.setWindowTitle(QCoreApplication.translate("ColorLabel", u"Form", None))
        self.label.setText("")
    # retranslateUi

