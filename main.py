import sys

from FunctionFigure import Figure
from MainWindow import MainWindow
from FigureListItem import FigureListItem
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

def show(item):
    print(item)

if __name__ == '__main__':
    app = QApplication()
    mainWindow = MainWindow()

    # for i in range(10):
    #     widg = FigureListItem()
    #
    #     itemList = QListWidgetItem(mainWindow.figure_list)
    #     itemList.setSizeHint(widg.sizeHint())
    #     Figure.FigureToFigureListItem(Figure(str(i) , "s*2" ,23, 0), itemList)
    #     widg.UpdateWidgit(Figure(str(i) , "s*2" ,23, 0))
    #     mainWindow.figure_list.addItem(itemList)
    #     mainWindow.figure_list.setItemWidget(itemList, widg)
    mainWindow.show()

    sys.exit(app.exec_())
