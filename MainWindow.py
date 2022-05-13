# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from copy import copy

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from CanvasFigure import MplCanvas
import FunctionFigure
from AddFigureDialog import AddFigureDialog
from FunctionFigure import Figure, FigureList
from FigureListWidgit import FigureListWidgit
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from EditFigureDialog import EditFigureDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.selectedItemIndex = 0
        self.figureList = FigureList()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"main_window")
        self.resize(1037, 605)
        self.action_open_state = QAction(self)
        self.action_open_state.setObjectName(u"action_open_state")
        self.action_save_State_As = QAction(self)
        self.action_save_State_As.setObjectName(u"action_save_State_As")
        self.centralwidget = QWidget(self)
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
        self.drawing_area.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.splitter.addWidget(self.drawing_area)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1037, 19))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.action_open_state)
        self.menuFile.addAction(self.action_save_State_As)



        self.vBox = QVBoxLayout()
        self.canv = MplCanvas()
        # self._fig.add_axes((0, 0, 1, 1))
        self.canv.setParent(self.drawing_area)
        self.canv.setFocusPolicy(Qt.StrongFocus)
        self.vBox.addWidget(self.canv)
        self.drawing_area.setLayout(self.vBox)
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("main_window", u"Plotter", None))
        self.action_open_state.setText(QCoreApplication.translate("main_window", u"Open state", None))
        self.action_save_State_As.setText(QCoreApplication.translate("main_window", u"Save State As", None))
        self.add_push_button.setText(QCoreApplication.translate("main_window", u"Add", None))
        self.reset_push_button.setText(QCoreApplication.translate("main_window", u"Reset", None))
        self.menuFile.setTitle(QCoreApplication.translate("main_window", u"File", None))
        self.add_push_button.clicked.connect(self.ShowAddFigureEvent)
        self.reset_push_button.clicked.connect(self.resetAll)
        self.figure_list.itemDoubleClicked.connect(self.EditEvent)
    # retranslateUi

    def EditEvent(self, item : QListWidgetItem):
        self.selectedItemIndex = self.figure_list.row(item)
        print(self.figureList.list[self.selectedItemIndex])
        self.editFigureDialog = EditFigureDialog(self.figureList.list[self.selectedItemIndex], self)
        self.editFigureDialog.show()

    def ShowAddFigureEvent(self):
        self.addFigureDialog = AddFigureDialog(self)
        self.addFigureDialog.show()

    def GetFigureToAdd(self):
        listItemFigure = self.addFigureDialog.figure
        print(self.addFigureDialog.figure)
        self.figureList.Add(listItemFigure)
        self.figureList.Render(self, self.canv)


    def DeleteFigure(self):
        self.figureList.Delete(self.selectedItemIndex)
        self.figureList.Render(self, self.canv)

    def UpdateFigure(self):
        newFigure = self.editFigureDialog.figure
        self.figureList.list[self.selectedItemIndex] = newFigure
        print(newFigure)
        self.figureList.Render(self, self.canv)

    def resetAll(self):
       self.figureList.Clear()
       self.figureList.Render(self, self.canv)


