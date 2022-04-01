# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'card.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
                           QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(617, 27)
        Form.setLayoutDirection(Qt.RightToLeft)
        Form.setStyleSheet(u"QWidget{\n"
                           "background-color: rgb(103, 103, 103);\n"
                           "}")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.name_file_card = QLabel(Form)
        self.name_file_card.setObjectName(u"name_file_card")
        self.name_file_card.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                          "font: 18pt \"Arial\";")
        self.name_file_card.setAlignment(Qt.AlignCenter)
        self.name_file_card.setWordWrap(True)

        self.horizontalLayout.addWidget(self.name_file_card)

        self.delete__btn_card = QToolButton(Form)
        self.delete__btn_card.setObjectName(u"delete__btn_card")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete__btn_card.sizePolicy().hasHeightForWidth())
        self.delete__btn_card.setSizePolicy(sizePolicy)
        self.delete__btn_card.setMaximumSize(QSize(70, 16777215))
        self.delete__btn_card.setLayoutDirection(Qt.RightToLeft)
        #self.delete__btn_card.clicked.connect(self.delete)
        self.delete__btn_card.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "font: 14pt \"Arial\";\n"
                                            " border: 0px solid;")

        self.horizontalLayout.addWidget(self.delete__btn_card)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.name_file_card.setText(QCoreApplication.translate("Form", u"ICS 102.pdf", None))
        self.delete__btn_card.setText(QCoreApplication.translate("Form", u"\u062d\u0630\u0641", None))
    # retranslateUi
