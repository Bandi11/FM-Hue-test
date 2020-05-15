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
        ColorLabel.resize(82, 80)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ColorLabel.sizePolicy().hasHeightForWidth())
        ColorLabel.setSizePolicy(sizePolicy)
        ColorLabel.setMinimumSize(QSize(50, 50))
        ColorLabel.setMaximumSize(QSize(82, 80))
        self.gridLayout = QGridLayout(ColorLabel)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(ColorLabel)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(16777215, 80))
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

