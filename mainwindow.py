# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1037, 605)
        self.action_open_state = QAction(MainWindow)
        self.action_open_state.setObjectName(u"action_open_state")
        self.action_save_State_As = QAction(MainWindow)
        self.action_save_State_As.setObjectName(u"action_save_State_As")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(0, 0, 1041, 561))
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.figure_list = QListWidget(self.widget)
        self.figure_list.setObjectName(u"figure_list")

        self.verticalLayout.addWidget(self.figure_list)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_push_button = QPushButton(self.widget)
        self.add_push_button.setObjectName(u"add_push_button")

        self.horizontalLayout.addWidget(self.add_push_button)

        self.reset_push_button = QPushButton(self.widget)
        self.reset_push_button.setObjectName(u"reset_push_button")

        self.horizontalLayout.addWidget(self.reset_push_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.widget)
        self.drawing_area = QWidget(self.splitter)
        self.drawing_area.setObjectName(u"drawing_area")
        self.drawing_area.setStyleSheet(u"background-color: rgb(7, 7, 7);")
        self.splitter.addWidget(self.drawing_area)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1037, 19))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.action_open_state)
        self.menuFile.addAction(self.action_save_State_As)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_open_state.setText(QCoreApplication.translate("MainWindow", u"Open state", None))
        self.action_save_State_As.setText(QCoreApplication.translate("MainWindow", u"Save State As", None))
        self.add_push_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.reset_push_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

