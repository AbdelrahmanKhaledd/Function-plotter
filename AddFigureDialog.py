# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_figure_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from FunctionFigure import Figure

class AddFigureDialog(QDialog):
    def __init__(self, mainWindow):
        super(AddFigureDialog, self).__init__()
        self.setupUi()
        self.figure = Figure()
        self.mainWindow = mainWindow

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"add_figure_dialog")
        self.resize(372, 196)
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 351, 94))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 0))
        self.label_3.setMaximumSize(QSize(16777215, 40))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.max_textbox = QTextEdit(self.layoutWidget)
        self.max_textbox.setObjectName(u"max_textbox")
        self.max_textbox.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(13)
        self.max_textbox.setFont(font)

        self.horizontalLayout_2.addWidget(self.max_textbox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(30, 0))
        self.label_4.setMaximumSize(QSize(16777215, 40))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_4)

        self.min_textbox = QTextEdit(self.layoutWidget)
        self.min_textbox.setObjectName(u"min_textbox")
        self.min_textbox.setMaximumSize(QSize(16777215, 40))
        self.min_textbox.setFont(font)

        self.horizontalLayout.addWidget(self.min_textbox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(47, 0))
        self.label.setMaximumSize(QSize(16777215, 40))
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.figure_name_textbox = QTextEdit(self.layoutWidget)
        self.figure_name_textbox.setObjectName(u"figure_name_textbox")
        self.figure_name_textbox.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setPointSize(11)
        self.figure_name_textbox.setFont(font1)

        self.horizontalLayout_4.addWidget(self.figure_name_textbox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.function_textbox = QTextEdit(self.layoutWidget)
        self.function_textbox.setObjectName(u"function_textbox")
        self.function_textbox.setMaximumSize(QSize(16777215, 40))
        self.function_textbox.setFont(font1)

        self.horizontalLayout_3.addWidget(self.function_textbox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.layoutWidget_2 = QWidget(self)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(70, 160, 221, 24))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ok_button = QPushButton(self.layoutWidget_2)
        self.ok_button.setObjectName(u"ok_button")

        self.horizontalLayout_6.addWidget(self.ok_button)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.cancel_button = QPushButton(self.layoutWidget_2)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout_6.addWidget(self.cancel_button)

        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(140, 120, 58, 22))
        self.horizontalLayout_7 = QHBoxLayout(self.widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.color_button = QPushButton(self.widget)
        self.color_button.setObjectName(u"color_button")
        self.color_button.setMinimumSize(QSize(20, 20))
        self.color_button.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_7.addWidget(self.color_button)


        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("figure_properity_dialog", u"Figure properity", None))
        self.label_3.setText(QCoreApplication.translate("figure_properity_dialog", u"Max", None))
        self.label_4.setText(QCoreApplication.translate("figure_properity_dialog", u"Min", None))
        self.label.setText(QCoreApplication.translate("figure_properity_dialog", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("figure_properity_dialog", u"Function", None))
        self.ok_button.setText(QCoreApplication.translate("figure_properity_dialog", u"OK", None))
        self.cancel_button.setText(QCoreApplication.translate("figure_properity_dialog", u"Cancel", None))
        self.label_5.setText(QCoreApplication.translate("figure_properity_dialog", u"Color", None))
        self.color_button.setText("")
        self.min_textbox.setAlignment(Qt.AlignCenter)
        self.max_textbox.setAlignment(Qt.AlignCenter)
        self.figure_name_textbox.setFont(QFont(pointSize=13))
        self.function_textbox.setFont(QFont(pointSize=13))
        self.min_textbox.setText("-100")
        self.max_textbox.setText("100")

        self.ok_button.clicked.connect(self.OkEvent)
        self.cancel_button.clicked.connect(self.close)
    # retranslateUi

    def OkEvent(self):
        errorMessage = self.isValid()
        if len(errorMessage) > 0:
            self.errorDialog = QErrorMessage()
            self.errorDialog.showMessage(errorMessage)
        else:
            self.figure = Figure(
                self.figure_name_textbox.toPlainText().strip(),
                self.function_textbox.toPlainText().strip(),
                int(self.max_textbox.toPlainText().strip()),
                int(self.min_textbox.toPlainText().strip())
            )
            self.mainWindow.GetFigureToAdd()
            self.close()


    def isValid(self):
        valid = True
        currentMax = int(self.max_textbox.toPlainText())
        currentMin = int(self.min_textbox.toPlainText())
        currentName = self.figure_name_textbox.toPlainText()
        currentFunction = self.function_textbox.placeholderText()
        errorMessage = ""
        if currentMin > currentMax:
            valid = False
            errorMessage += "Max must be bigger than min\n"

        if len(currentName) > 6:
            valid = False
            errorMessage += "Name's length must be smaller than 6\n"

        #TODO syntax
        if valid:
            return ""
        else:
            errorMessage
