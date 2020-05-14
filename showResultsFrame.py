# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'showResultsFrame.ui'
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


class Ui_testResults(object):
    def setupUi(self, testResults):
        if not testResults.objectName():
            testResults.setObjectName(u"testResults")
        testResults.resize(365, 614)
        self.gridLayout = QGridLayout(testResults)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(testResults)
        self.frame.setObjectName(u"frame")
        font = QFont()
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.histogramLabel = QLabel(self.frame)
        self.histogramLabel.setObjectName(u"histogramLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.histogramLabel.sizePolicy().hasHeightForWidth())
        self.histogramLabel.setSizePolicy(sizePolicy)
        self.histogramLabel.setScaledContents(True)
        self.histogramLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.histogramLabel, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(50, 15))

        self.horizontalLayout.addWidget(self.pushButton)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(18)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.nameLabel = QLabel(self.frame)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.scoreLabel = QLabel(self.frame)
        self.scoreLabel.setObjectName(u"scoreLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.scoreLabel)

        self.dateLabel = QLabel(self.frame)
        self.dateLabel.setObjectName(u"dateLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.dateLabel)

        self.colorBlindnessLabel = QLabel(self.frame)
        self.colorBlindnessLabel.setObjectName(u"colorBlindnessLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.colorBlindnessLabel)

        self.colorBlindnessCheckBox = QCheckBox(self.frame)

        self.colorBlindnessCheckBox.setObjectName(u"colorBlindnessCheckBox")
        self.colorBlindnessCheckBox.setEnabled(False)
        self.colorBlindnessCheckBox.setCheckable(True)
        self.colorBlindnessCheckBox.setChecked(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.colorBlindnessCheckBox)

        self.nameEditLabel = QLabel(self.frame)
        self.nameEditLabel.setObjectName(u"nameEditLabel")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameEditLabel)

        self.scoreEditLabel = QLabel(self.frame)
        self.scoreEditLabel.setObjectName(u"scoreEditLabel")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.scoreEditLabel)

        self.dateEditLabel = QLabel(self.frame)
        self.dateEditLabel.setObjectName(u"dateEditLabel")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dateEditLabel)


        self.gridLayout_2.addLayout(self.formLayout, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)


        self.retranslateUi(testResults)

        QMetaObject.connectSlotsByName(testResults)
    # setupUi

    def retranslateUi(self, testResults):
        testResults.setWindowTitle(QCoreApplication.translate("testResults", u"Form", None))
        self.histogramLabel.setText("")
        self.pushButton.setText(QCoreApplication.translate("testResults", u"Back", None))
        self.label.setText(QCoreApplication.translate("testResults", u"Results", None))
        self.nameLabel.setText(QCoreApplication.translate("testResults", u"Name:", None))
        self.scoreLabel.setText(QCoreApplication.translate("testResults", u"Score :", None))
        self.dateLabel.setText(QCoreApplication.translate("testResults", u"Date of test:", None))
        self.colorBlindnessLabel.setText(QCoreApplication.translate("testResults", u"Color Blindness", None))
        self.nameEditLabel.setText("")
        self.scoreEditLabel.setText("")
        self.dateEditLabel.setText("")
    # retranslateUi

