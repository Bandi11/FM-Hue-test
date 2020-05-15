# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testFrame.ui'
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


class Ui_testPage(object):
    def setupUi(self, testPage):
        if not testPage.objectName():
            testPage.setObjectName(u"testPage")
        testPage.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(testPage.sizePolicy().hasHeightForWidth())
        testPage.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(testPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(1)
        self.gridLayout.setContentsMargins(1, 1, 1, -1)
        self.frame = QFrame(testPage)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)

        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 4, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(testPage)

        QMetaObject.connectSlotsByName(testPage)
    # setupUi

    def retranslateUi(self, testPage):
        testPage.setWindowTitle(QCoreApplication.translate("testPage", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("testPage", u"Next Page", None))
    # retranslateUi

