# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectingStartData.ui'
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


class Ui_selectingStartData(object):
    def setupUi(self, selectingStartData):
        if not selectingStartData.objectName():
            selectingStartData.setObjectName(u"selectingStartData")
        selectingStartData.resize(430, 373)
        self.gridLayout = QGridLayout(selectingStartData)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(selectingStartData)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.startDataList = QComboBox(self.frame)
        self.startDataList.addItem("")
        self.startDataList.setObjectName(u"startDataList")
        self.startDataList.setEnabled(True)
        self.startDataList.setEditable(False)
        self.startDataList.setFrame(False)

        self.verticalLayout.addWidget(self.startDataList)

        self.selectButton = QPushButton(self.frame)
        self.selectButton.setObjectName(u"selectButton")

        self.verticalLayout.addWidget(self.selectButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(selectingStartData)

        QMetaObject.connectSlotsByName(selectingStartData)
    # setupUi

    def retranslateUi(self, selectingStartData):
        selectingStartData.setWindowTitle(QCoreApplication.translate("selectingStartData", u"Form", None))
        self.label.setText(QCoreApplication.translate("selectingStartData", u"Choose a randomization", None))
        self.startDataList.setItemText(0, QCoreApplication.translate("selectingStartData", u"No randomization", None))

        self.selectButton.setText(QCoreApplication.translate("selectingStartData", u"Select", None))
    # retranslateUi

