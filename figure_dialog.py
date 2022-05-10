# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'figure_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Figure import Figure
from figure_item import FigureItem


class FigureDialog(QDialog):
    #if currentFigure = None then it's adding operation
    def __init__(self, currentFigure:Figure, mainWindow=None, widgetItem=None):
        super(FigureDialog, self).__init__()
        self.setupUi()
        self.mainWindow = mainWindow
        self.parentFigureItem = widgetItem
        self.figure = currentFigure
        self.thereAreFigure = True if self.figure != None else False
        if not self.thereAreFigure:
            self.figure = Figure()
        if not self.thereAreFigure:
            self.max_textbox.setText('100')
            self.min_textbox.setText('-100')
            self.figure_name_textbox.setText("")
            self.function_textbox.setText("")
        else:
            self.max_textbox.setText(self.figure.max)
            self.min_textbox.setText(self.figure.min)
            self.figure_name_textbox_textbox.setText(self.figure.name)
            self.function_textbox.setText(self.figure.function)


    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"figure_properity_dialog")
        self.resize(344, 142)
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 324, 81))
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.max_textbox = QTextEdit(self.widget)
        self.max_textbox.setObjectName(u"max_textbox")
        font = QFont()
        font.setPointSize(13)
        self.max_textbox.setFont(font)

        self.horizontalLayout_2.addWidget(self.max_textbox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.min_textbox = QTextEdit(self.widget)
        self.min_textbox.setObjectName(u"min_textbox")
        self.min_textbox.setFont(font)

        self.horizontalLayout.addWidget(self.min_textbox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.figure_name_textbox = QTextEdit(self.widget)
        self.figure_name_textbox.setObjectName(u"figure_name_textbox")
        font1 = QFont()
        font1.setPointSize(11)
        self.figure_name_textbox.setFont(font1)

        self.horizontalLayout_4.addWidget(self.figure_name_textbox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.function_textbox = QTextEdit(self.widget)
        self.function_textbox.setObjectName(u"function_textbox")
        self.function_textbox.setFont(font1)

        self.horizontalLayout_3.addWidget(self.function_textbox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.widget1 = QWidget(self)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(60, 110, 221, 24))
        self.horizontalLayout_6 = QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ok_button = QPushButton(self.widget1)
        self.ok_button.setObjectName(u"ok_button")

        self.horizontalLayout_6.addWidget(self.ok_button)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.cancel_button = QPushButton(self.widget1)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout_6.addWidget(self.cancel_button)


        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("figure_properity_dialog", u"Figure properity", None))
        self.label_3.setText(QCoreApplication.translate("figure_properity_dialog", u"Max", None))
        self.label_4.setText(QCoreApplication.translate("figure_properity_dialog", u"Min", None))
        self.label.setText(QCoreApplication.translate("figure_properity_dialog", u"Figure name", None))
        self.label_2.setText(QCoreApplication.translate("figure_properity_dialog", u"Function", None))
        self.ok_button.setText(QCoreApplication.translate("figure_properity_dialog", u"OK", None))
        self.cancel_button.setText(QCoreApplication.translate("figure_properity_dialog", u"Cancel", None))
        # setting alignment to be center
        self.max_textbox.setAlignment(Qt.AlignCenter)
        self.min_textbox.setAlignment(Qt.AlignCenter)
        self.ok_button.clicked.connect(self.verifyAndSendFigure)
        self.cancel_button.clicked.connect( self.close)
    # retranslateUi

    def verifyAndSendFigure(self):
        currentMax = int(self.max_textbox.toPlainText())
        currentMin = int(self.min_textbox.toPlainText())
        currentName = self.figure_name_textbox.toPlainText().strip()
        currentFunction = self.function_textbox.toPlainText().strip()
        errorMessage = ""
        valied = True
        if currentMax < currentMin:
            valied = False
            errorMessage += f"Max less than Min\n"

        if len(currentName) > 5:
            valied = False
            errorMessage += f"length of figure name must be less than 6\n"

        # TODO here syntax valiedation
        if valied:
            if not self.thereAreFigure:
                self.figure.name = currentName
                self.figure.function = currentFunction
                self.figure.min = currentMin
                self.figure.max = currentMax

                itemWidget = FigureItem(self.figure)
                itemWidgetElement = QListWidgetItem(self.mainWindow.figure_list)
                itemWidgetElement.setSizeHint(itemWidget.sizeHint())
                self.mainWindow.figure_list.addItem(itemWidgetElement)
                self.mainWindow.figure_list.setItemWidget(itemWidgetElement, itemWidget)
                self.mainWindow.figure_list.update()
            else:
                self.figure.name = currentName
                self.figure.function = currentFunction
                self.figure.min = currentMin
                self.figure.max = currentMax
                self.parentFigureItem.UpdateFigure(self.figure)
                self.mainWindow.figure_list.update()
            self.close()

        else:
            errorMessageBox = QMessageBox()
            errorMessageBox.setText(errorMessage)
            errorMessageBox.show()
