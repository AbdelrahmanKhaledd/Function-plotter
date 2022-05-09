# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
from PySide2 import QtCore, QtWidgets, QtGui, QtUiTools
from mainwindow import Ui_main_window
from figure_dialog import Ui_figure_properity_dialog

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)

class FigureDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_figure_properity_dialog()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    mainWindow = MainWindow()
    mainWindow.show()
    pop = FigureDialog()
    pop.show()
    sys.exit(app.exec_())
