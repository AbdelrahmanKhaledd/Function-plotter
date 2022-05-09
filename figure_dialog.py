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


class Ui_figure_properity_dialog(object):
    def setupUi(self, figure_properity_dialog):
        if not figure_properity_dialog.objectName():
            figure_properity_dialog.setObjectName(u"figure_properity_dialog")
        figure_properity_dialog.resize(340, 143)
        self.widget = QWidget(figure_properity_dialog)
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

        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")
        font = QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.textEdit.setFont(font)

        self.horizontalLayout_2.addWidget(self.textEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.textEdit_2 = QTextEdit(self.widget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        font1 = QFont()
        font1.setPointSize(13)
        self.textEdit_2.setFont(font1)

        self.horizontalLayout.addWidget(self.textEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.textEdit_3 = QTextEdit(self.widget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        font2 = QFont()
        font2.setPointSize(11)
        self.textEdit_3.setFont(font2)

        self.horizontalLayout_4.addWidget(self.textEdit_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.textEdit_4 = QTextEdit(self.widget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setFont(font2)

        self.horizontalLayout_3.addWidget(self.textEdit_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.widget1 = QWidget(figure_properity_dialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(50, 110, 221, 24))
        self.horizontalLayout_6 = QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget1)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_6.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.widget1)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_6.addWidget(self.pushButton_2)


        self.retranslateUi(figure_properity_dialog)

        QMetaObject.connectSlotsByName(figure_properity_dialog)
    # setupUi

    def retranslateUi(self, figure_properity_dialog):
        figure_properity_dialog.setWindowTitle(QCoreApplication.translate("figure_properity_dialog", u"Figure properity", None))
        self.label_3.setText(QCoreApplication.translate("figure_properity_dialog", u"Max", None))
        self.textEdit.setHtml(QCoreApplication.translate("figure_properity_dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("figure_properity_dialog", u"Min", None))
        self.label.setText(QCoreApplication.translate("figure_properity_dialog", u"Figure name", None))
        self.label_2.setText(QCoreApplication.translate("figure_properity_dialog", u"Function", None))
        self.pushButton.setText(QCoreApplication.translate("figure_properity_dialog", u"OK", None))
        self.pushButton_2.setText(QCoreApplication.translate("figure_properity_dialog", u"Cancel", None))
    # retranslateUi

