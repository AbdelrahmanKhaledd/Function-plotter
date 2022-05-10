import sys

from Figure import Figure
from figure_item import FigureItem
from mainwindow import MainWindow

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *



if __name__ == '__main__':
    app = QApplication()
    mainWindow = MainWindow()
    for i in range(10):
        widg = FigureItem(Figure('a' , 'sd' , 23 ,23 ))

        itemList = QListWidgetItem(mainWindow.figure_list)
        itemList.setSizeHint(widg.sizeHint())
        mainWindow.figure_list.addItem(itemList)
        mainWindow.figure_list.setItemWidget(itemList, widg)

    mainWindow.show()


    sys.exit(app.exec_())
