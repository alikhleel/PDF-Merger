# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 650)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
#if QT_CONFIG(statustip)
        MainWindow.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        MainWindow.setLayoutDirection(Qt.RightToLeft)
        MainWindow.setStyleSheet(u"QPushButton, QLineEdit, QPlainTextEdit{\n"
" margin-top: 10px;\n"
"\n"
"}\n"
"QRadioButton{\n"
"	font:  10pt \"Arial\";\n"
"font-weight:900;\n"
"}")
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.input_text = QLineEdit(self.widget)
        self.input_text.setObjectName(u"input_text")
        font = QFont()
        font.setPointSize(12)
        self.input_text.setFont(font)
        self.input_text.setStyleSheet(u"QLineEdit{\n"
"padding: 10 10 10 10;\n"
"\n"
"}\n"
"")
        self.input_text.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.input_text)

        self.input_btn = QPushButton(self.widget)
        self.input_btn.setObjectName(u"input_btn")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setBold(True)
        font1.setWeight(75)
        self.input_btn.setFont(font1)
        self.input_btn.setStyleSheet(u"QPushButton{\n"
"	background:linear-gradient(to bottom, #599bb3 5%, #408c99 100%);\n"
"	background-color:#599bb3;\n"
"	border-radius:8px;\n"
"	color:#ffffff;\n"
"	font-family:Arial;\n"
"	font-size:18px;\n"
"	font-weight:bold;\n"
"	padding:10px 10px 10px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background:linear-gradient(to bottom, #408c99 5%, #599bb3 100%);\n"
"	background-color:#408c99;\n"
"}\n"
"QPushButton:active {\n"
"	position:relative;\n"
"	top:1px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.input_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMinimumSize(QSize(0, 150))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setKerning(True)
        self.scrollArea.setFont(font2)
        self.scrollArea.setWidgetResizable(True)
        self.scroll_list_input_files = QWidget()
        self.scroll_list_input_files.setObjectName(u"scroll_list_input_files")
        self.scroll_list_input_files.setGeometry(QRect(0, 0, 560, 148))
        self.verticalLayout_2 = QVBoxLayout(self.scroll_list_input_files)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea.setWidget(self.scroll_list_input_files)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.output_text = QLineEdit(self.widget)
        self.output_text.setObjectName(u"output_text")
        self.output_text.setFont(font)
        self.output_text.setStyleSheet(u"QLineEdit{\n"
"padding: 10 10 10 10;\n"
"}")
        self.output_text.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.output_text)

        self.output_btn = QPushButton(self.widget)
        self.output_btn.setObjectName(u"output_btn")
        self.output_btn.setFont(font1)
        self.output_btn.setStyleSheet(u"QPushButton{\n"
"	background:linear-gradient(to bottom, #599bb3 5%, #408c99 100%);\n"
"	background-color:#599bb3;\n"
"	border-radius:8px;\n"
"	color:#ffffff;\n"
"	font-family:Arial;\n"
"	font-size:18px;\n"
"	font-weight:bold;\n"
"	padding:10px 10px 10px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background:linear-gradient(to bottom, #408c99 5%, #599bb3 100%);\n"
"	background-color:#408c99;\n"
"}\n"
"QPushButton:active {\n"
"	position:relative;\n"
"	top:1px;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.output_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 1)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        font3 = QFont()
        self.progressBar.setFont(font3)
        self.progressBar.setStyleSheet(u"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
" font-size: 18px;\n"
"	color:black;\n"
"\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: green;\n"
"    width: 2.15px;\n"
"}")
        self.progressBar.setValue(50)

        self.gridLayout_2.addWidget(self.progressBar, 3, 0, 1, 1)

        self.log_text = QTextEdit(self.widget)
        self.log_text.setObjectName(u"log_text")
        self.log_text.setFont(font)
        self.log_text.setReadOnly(True)

        self.gridLayout_2.addWidget(self.log_text, 4, 0, 1, 1)

        self.generate_btn = QPushButton(self.widget)
        self.generate_btn.setObjectName(u"generate_btn")
        sizePolicy1.setHeightForWidth(self.generate_btn.sizePolicy().hasHeightForWidth())
        self.generate_btn.setSizePolicy(sizePolicy1)
        self.generate_btn.setFont(font1)
        self.generate_btn.setStyleSheet(u"QPushButton{\n"
"	background:linear-gradient(to bottom, #599bb3 5%, #408c99 100%);\n"
"	background-color:#599bb3;\n"
"	border-radius:8px;\n"
"	color:#ffffff;\n"
"	font-family:Arial;\n"
"	font-size:25px;\n"
"	font-weight:bold;\n"
"	padding:13px 32px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background:linear-gradient(to bottom, #408c99 5%, #599bb3 100%);\n"
"	background-color:#408c99;\n"
"}\n"
"QPushButton:active {\n"
"	position:relative;\n"
"	top:1px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.generate_btn, 6, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.radioButton_op_1 = QRadioButton(self.widget)
        self.radioButton_op_1.setObjectName(u"radioButton_op_1")

        self.horizontalLayout_2.addWidget(self.radioButton_op_1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.radioButton_op_2 = QRadioButton(self.widget)
        self.radioButton_op_2.setObjectName(u"radioButton_op_2")

        self.horizontalLayout_2.addWidget(self.radioButton_op_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.log_text.raise_()
        self.generate_btn.raise_()
        self.progressBar.raise_()

        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.input_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0645\u0633\u0627\u0631 \u0645\u062c\u0644\u062f \u0627\u0644\u0625\u062f\u062e\u0627\u0644", None))
        self.input_btn.setText(QCoreApplication.translate("MainWindow", u"\u0627\u062e\u062a\u064a\u0627\u0631 \u0645\u0643\u0627\u0646 \u0627\u0644\u0625\u062e\u0627\u0644", None))
        self.output_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0645\u0633\u0627\u0631 \u0645\u062c\u0644\u062f \u0627\u0644\u0625\u062e\u0631\u0627\u062c", None))
        self.output_btn.setText(QCoreApplication.translate("MainWindow", u"\u0627\u062e\u062a\u064a\u0627\u0631 \u0645\u0643\u0627\u0646 \u0627\u0644\u0625\u062e\u0631\u0627\u062c", None))
        self.generate_btn.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0645\u062c", None))
        self.radioButton_op_1.setText(QCoreApplication.translate("MainWindow", u"\u0628\u062a\u0646\u0633\u0628\u0642 \u0645\u0644\u0641\u0627\u062a \u0627\u0644\u0645\u0627\u0644\u064a\u0629", None))
        self.radioButton_op_2.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0645\u062c \u0645\u0644\u0641\u0627\u062a \u0639\u0627\u062f\u064a\u0629", None))
    # retranslateUi

