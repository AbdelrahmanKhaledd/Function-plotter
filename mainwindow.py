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


class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(1037, 605)
        self.action_open_state = QAction(main_window)
        self.action_open_state.setObjectName(u"action_open_state")
        self.action_save_State_As = QAction(main_window)
        self.action_save_State_As.setObjectName(u"action_save_State_As")
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(0, 0, 1041, 561))
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.figure_list = QListWidget(self.layoutWidget)
        self.figure_list.setObjectName(u"figure_list")

        self.verticalLayout.addWidget(self.figure_list)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_push_button = QPushButton(self.layoutWidget)
        self.add_push_button.setObjectName(u"add_push_button")

        self.horizontalLayout.addWidget(self.add_push_button)

        self.reset_push_button = QPushButton(self.layoutWidget)
        self.reset_push_button.setObjectName(u"reset_push_button")

        self.horizontalLayout.addWidget(self.reset_push_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.layoutWidget)
        self.drawing_area = QWidget(self.splitter)
        self.drawing_area.setObjectName(u"drawing_area")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drawing_area.sizePolicy().hasHeightForWidth())
        self.drawing_area.setSizePolicy(sizePolicy)
        self.drawing_area.setStyleSheet(u"background-color: rgb(7, 7, 7);")
        self.splitter.addWidget(self.drawing_area)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1037, 19))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.action_open_state)
        self.menuFile.addAction(self.action_save_State_As)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"Plotter", None))
        self.action_open_state.setText(QCoreApplication.translate("main_window", u"Open state", None))
        self.action_save_State_As.setText(QCoreApplication.translate("main_window", u"Save State As", None))
        self.add_push_button.setText(QCoreApplication.translate("main_window", u"Add", None))
        self.reset_push_button.setText(QCoreApplication.translate("main_window", u"Reset", None))
        self.menuFile.setTitle(QCoreApplication.translate("main_window", u"File", None))
    # retranslateUi

