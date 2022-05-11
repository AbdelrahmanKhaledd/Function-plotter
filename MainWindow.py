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

from AddFigureDialog import AddFigureDialog
from Figure import Figure
from FigureListItem import FigureListItem
from EditFigureDialog import EditFigureDialog

import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg, NavigationToolbar2QT)
from matplotlib import figure
from pylab import *

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = figure.Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.selectedItemIndex = 0

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
        self.drawing_area.setStyleSheet(u"background-color: rgb(7, 7, 7);")
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
        self._fig = figure(facecolor="white" )
        self._ax = self._fig.add_subplot(111)

        self._canvas = FigureCanvasQTAgg(self._fig)
        self._canvas.setParent(self.drawing_area)
        self._canvas.setFocusPolicy(Qt.StrongFocus)
        self.vBox.addWidget(self._canvas)
        self.drawing_area.setLayout(self.vBox)
        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi
    def plotRandom(self ):
        self.x = linspace(0, 4 * pi, 1000)
        self._ax.plot(self.x, sin(2 * pi * rand() * 2 * self.x), lw=2)
        self._canvas.draw()

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("main_window", u"Plotter", None))
        self.action_open_state.setText(QCoreApplication.translate("main_window", u"Open state", None))
        self.action_save_State_As.setText(QCoreApplication.translate("main_window", u"Save State As", None))
        self.add_push_button.setText(QCoreApplication.translate("main_window", u"Add", None))
        self.reset_push_button.setText(QCoreApplication.translate("main_window", u"Reset", None))
        self.menuFile.setTitle(QCoreApplication.translate("main_window", u"File", None))
        self.add_push_button.clicked.connect(self.addFigureEvent)
        self.reset_push_button.clicked.connect(self.resetAll)
        self.figure_list.itemDoubleClicked.connect(self.EditEvent)
    # retranslateUi

    def EditEvent(self, item : QListWidgetItem):
        print(Figure.FigureListItemToFigure(item))
        self.editFigureDialog = EditFigureDialog(Figure.FigureListItemToFigure(item), self)
        self.editFigureDialog.show()
        self.selectedItemIndex = self.figure_list.row(item)

    def addFigureEvent(self):
        self.addFigureDialog = AddFigureDialog(self)
        self.addFigureDialog.show()

    def getFigureToAdd(self):
        figure = copy(self.addFigureDialog.figure)
        listItemWidgit = FigureListItem()
        listItem = QListWidgetItem(self.figure_list)
        listItem.setSizeHint(listItemWidgit.sizeHint())
        Figure.FigureToFigureListItem(figure, listItem)
        self.figure_list.addItem(listItem)
        self.figure_list.setItemWidget(listItem, listItemWidgit)
        self.figure_list.update()

    def DeleteFigure(self):
        self.figure_list.takeItem(self.selectedItemIndex)

    def resetAll(self):
        self.figure_list.reset()
        self.figure_list.update()


