# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'figure_item.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from FunctionFigure import Figure

class FigureListWidgit(QWidget):
    def __init__(self, figure:Figure=None):
        super(FigureListWidgit, self).__init__()
        self.setupUi()
        self.figure = figure
        self.UpdateWidgit(self.figure)


    def setupUi(self):
        self.resize(290, 33)
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 291, 32))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.figure_name = QLabel(self.layoutWidget)
        self.figure_name.setObjectName(u"figure_name")
        self.figure_name.setMinimumSize(QSize(70, 30))
        self.figure_name.setMaximumSize(QSize(70, 16777215))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.figure_name.setFont(font)
        self.figure_name.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_2.addWidget(self.figure_name)
        self.equation = QLabel(self.layoutWidget)
        self.equation.setObjectName(u"equation")
        self.equation.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.equation.setFont(font1)
        self.equation.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_2.addWidget(self.equation)
        self.retranslateUi()
        self.setLayout(self.horizontalLayout_2)
        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.figure_name.setText(QCoreApplication.translate("figure_item", u"A", None))
        self.equation.setText(QCoreApplication.translate("figure_item", u"x^2 +2 ", None))
    # retranslateUi

    def UpdateWidgit(self, figure:Figure):
        self.figure_name.setText(figure.name)
        self.equation.setText(figure.function)
        self.figure_name.setStyleSheet(f"color: rgb({self.figure.color[0]},{self.figure.color[1]},{self.figure.color[2]})")
