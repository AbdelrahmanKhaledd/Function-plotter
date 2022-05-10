# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'figure_item.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from copy import copy

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Figure import Figure


class FigureItem(QWidget):
    def __init__(self, figure:Figure):
        super().__init__()
        self.setupUi()
        self.figure = copy(figure)
        self.UpdateWidget()


    def setupUi(self):
        self.setGeometry(QRect(0, 0, 291, 31))
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.figure_name = QLabel()
        self.figure_name.setObjectName(u"figure_name")
        self.figure_name.setMinimumSize(QSize(40, 0))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.figure_name.setFont(font)
        self.figure_name.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.figure_name)

        self.equation = QLabel()
        self.equation.setObjectName(u"equation")
        font1 = QFont()
        font1.setPointSize(12)
        self.equation.setFont(font1)
        self.equation.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.equation)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.edit_button = QPushButton()
        self.edit_button.setObjectName(u"edit_button")
        self.edit_button.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u"assets/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_button.setIcon(icon)

        self.horizontalLayout.addWidget(self.edit_button)

        self.delete_button = QPushButton()
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u"assets/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_button.setIcon(icon1)

        self.horizontalLayout.addWidget(self.delete_button)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.setLayout(self.horizontalLayout_2)
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.figure_name.setText(QCoreApplication.translate("figure_item", u"A", None))
        self.equation.setText(QCoreApplication.translate("figure_item", u"x^2 +2 ", None))
        self.edit_button.setText("")
        self.delete_button.setText("")
    # retranslateUi


    def UpdateFigure(self, figure:Figure):
        self.figure.name = figure.name
        self.figure.function = figure.function
        self.figure.max = figure.max
        self.figure.min = figure.min

    def UpdateWidget(self):
        self.figure_name.setText(self.figure.name)
        self.equation.setText(self.figure.function)

