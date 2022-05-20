import sys

from GUI.MainWindow import MainWindow
from PySide2.QtWidgets import *

if __name__ == '__main__':
    app = QApplication()
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
