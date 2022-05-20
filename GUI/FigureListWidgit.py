from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from GUI.Figure import Figure

class FigureListWidgit(QWidget):
    def __init__(self, figure:Figure=None):
        super(FigureListWidgit, self).__init__()
        self.setupUi()
        self.figure = figure
        self.UpdateWidgit(self.figure)


    def setupUi(self):
        self.resize(290, 33)
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setGeometry(QRect(0, 0, 291, 32))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.figureName = QLabel(self.layoutWidget)
        self.figureName.setMinimumSize(QSize(70, 30))
        self.figureName.setMaximumSize(QSize(70, 16777215))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.figureName.setFont(font)
        self.figureName.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_2.addWidget(self.figureName)
        self.equation = QLabel(self.layoutWidget)
        self.equation.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.equation.setFont(font1)
        self.equation.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_2.addWidget(self.equation)
        self.RetranslateUi()
        self.setLayout(self.horizontalLayout_2)
        QMetaObject.connectSlotsByName(self)


    def RetranslateUi(self):
        self.figureName.setText(QCoreApplication.translate("figure_item", u"A", None))
        self.equation.setText(QCoreApplication.translate("figure_item", u"x^2 +2 ", None))

    def UpdateWidgit(self, figure:Figure):
        self.figureName.setText(figure.name)
        self.equation.setText(figure.function)
        self.figureName.setStyleSheet(f"color: rgb({self.figure.color[0]},{self.figure.color[1]},{self.figure.color[2]})")
