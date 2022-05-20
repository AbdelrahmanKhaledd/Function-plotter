import random

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from GUI.Figure import Figure
from Interpreter.Interpreter import *

class FigureDialog(QDialog):
    def __init__(self):
        super(FigureDialog, self).__init__()
        self.figure = Figure()

    def setupUi(self):
        self.resize(372, 196)
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setGeometry(QRect(140, 120, 58, 22))

        self.resize(372, 196)
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setGeometry(QRect(10, 10, 351, 94))
        self.horizontalLayoutFeatures = QHBoxLayout(self.layoutWidget)

        self.verticalLayout = QVBoxLayout()
        self.horizontalLayoutMax = QHBoxLayout()
        self.labelMax = QLabel(self.layoutWidget)
        self.labelMax.setMinimumSize(QSize(30, 0))
        self.labelMax.setMaximumSize(QSize(16777215, 40))

        self.maxTextBox = QTextEdit(self.layoutWidget)
        self.maxTextBox.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayoutMax.addWidget(self.labelMax)
        self.horizontalLayoutMax.addWidget(self.maxTextBox)

        self.verticalLayout.addLayout(self.horizontalLayoutMax)

        self.horizontalLayoutMin = QHBoxLayout()
        self.labelMin = QLabel(self.layoutWidget)
        self.labelMin.setMinimumSize(QSize(30, 0))
        self.labelMin.setMaximumSize(QSize(16777215, 40))
        self.minTextBox = QTextEdit(self.layoutWidget)
        self.minTextBox.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayoutMin.addWidget(self.labelMin)
        self.horizontalLayoutMin.addWidget(self.minTextBox)

        self.verticalLayout.addLayout(self.horizontalLayoutMin)

        self.horizontalLayoutFeatures.addLayout(self.verticalLayout)
        self.verticalLayout2 = QVBoxLayout()
        self.horizontalLayoutName = QHBoxLayout()
        self.labelName = QLabel(self.layoutWidget)
        self.labelName.setMinimumSize(QSize(47, 0))
        self.labelName.setMaximumSize(QSize(16777215, 40))
        self.figureNameTextBox = QTextEdit(self.layoutWidget)
        self.figureNameTextBox.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayoutName.addWidget(self.labelName)
        self.horizontalLayoutName.addWidget(self.figureNameTextBox)

        self.verticalLayout2.addLayout(self.horizontalLayoutName)
        self.horizontalLayoutFunction = QHBoxLayout()
        self.labelFunction = QLabel(self.layoutWidget)
        self.labelFunction.setMinimumSize(QSize(0, 30))
        self.labelFunction.setMaximumSize(QSize(16777215, 40))
        self.functionTextBox = QTextEdit(self.layoutWidget)
        self.functionTextBox.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayoutFunction.addWidget(self.labelFunction)
        self.horizontalLayoutFunction.addWidget(self.functionTextBox)

        self.verticalLayout2.addLayout(self.horizontalLayoutFunction)
        self.horizontalLayoutFeatures.addLayout(self.verticalLayout2)
        self.layoutWidget2 = QWidget(self)
        self.layoutWidget2.setGeometry(QRect(70, 160, 221, 24))
        self.horizontalLayout6 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout6.setContentsMargins(0, 0, 0, 0)
        self.okButton = QPushButton(self.layoutWidget2)
        self.horizontalLayout6.addWidget(self.okButton)
        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout6.addItem(self.horizontalSpacer)

        self.EditChangeSetup()
        self.cancelButton = QPushButton(self.layoutWidget2)
        self.horizontalLayout6.addWidget(self.cancelButton)

        self.widget = QWidget(self)
        self.widget.setGeometry(QRect(140, 120, 58, 22))
        self.horizontalLayoutColor = QHBoxLayout(self.widget)
        self.horizontalLayoutColor.setContentsMargins(0, 0, 0, 0)

        self.labelColor = QLabel(self.widget)
        self.colorButton = QPushButton(self.widget)
        self.colorButton.setMinimumSize(QSize(20, 20))
        self.colorButton.setMaximumSize(QSize(20, 20))
        self.horizontalLayoutColor.addWidget(self.labelColor)
        self.horizontalLayoutColor.addWidget(self.colorButton)
        self.RetranslateUi()


    def RetranslateUi(self):
        self.maxTextBox.setAlignment(Qt.AlignCenter)
        self.minTextBox.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(15)
        self.maxTextBox.setFont(font)
        self.minTextBox.setFont(font)

        self.figureNameTextBox.setFont(font)
        self.functionTextBox.setFont(font)

        self.setWindowTitle(QCoreApplication.translate("Edit", u"Edit figure", None))
        self.labelColor.setText(QCoreApplication.translate("figure_properity_dialog", u"Color", None))
        self.colorButton.setText("")
        self.labelMax.setText(QCoreApplication.translate("figure_properity_dialog", u"Max", None))
        self.labelMin.setText(QCoreApplication.translate("figure_properity_dialog", u"Min", None))
        self.labelName.setText(QCoreApplication.translate("figure_properity_dialog", u"Name", None))
        self.labelFunction.setText(QCoreApplication.translate("figure_properity_dialog", u"Function", None))
        self.okButton.setText(QCoreApplication.translate("figure_properity_dialog", u"OK", None))
        self.cancelButton.setText(QCoreApplication.translate("figure_properity_dialog", u"Cancel", None))
        self.EditChangeRetranslate()
        self.Connect()

    def Connect(self):
        pass

    def IsValid(self):
        valid = True
        currentMax = int(self.maxTextBox.toPlainText())
        currentMin = int(self.minTextBox.toPlainText())
        currentName = self.figureNameTextBox.toPlainText()
        currentFunction = self.functionTextBox.toPlainText()
        errorMessage = ""
        if currentMin > currentMax:
            valid = False
            errorMessage += "Max must be bigger than min\n"

        if len(currentName) > 6:
            valid = False
            errorMessage += "Name's length must be smaller than 6\n"
        try :
            self.figure.interpreter = Interpreter(currentFunction)
        except Exception as e:
            valid = False
            errorMessage += str(e)

        if valid:
            return ""
        else:
            return errorMessage

    def ColorBick(self):
        color = QColorDialog.getColor()
        if color.isValid():
            print(color.red(), color.green(), color.blue())
            self.figure.color = (color.red(), color.green(), color.blue())
            self.UpdateColorButton(self.figure.color)

    def UpdateColorButton(self, color):
        self.colorButton.setStyleSheet(f"background-color: rgb({color[0]},{color[1]},{color[2]});")

    def EditChangeSetup(self):
        pass

    def EditChangeRetranslate(self):
        pass



class AddFigureDialog(FigureDialog):
    def __init__(self, mainWindow):
        super(AddFigureDialog, self).__init__()
        self.setupUi()
        self.mainWindow = mainWindow
        self.Prepare()

    def Prepare(self):
        self.figure.color = (random.randint(0,244), random.randint(0,244), random.randint(0,244))
        self.UpdateColorButton(self.figure.color)
        self.maxTextBox.setText('100')
        self.minTextBox.setText('-100')
        self.maxTextBox.setAlignment(Qt.AlignCenter)
        self.minTextBox.setAlignment(Qt.AlignCenter)


    def Connect(self):
        self.okButton.clicked.connect(self.OkEvent)
        self.colorButton.clicked.connect(self.ColorBick)
        self.cancelButton.clicked.connect(self.close)

    def OkEvent(self):
        print('sd')
        errorMessage = self.IsValid()
        if len(errorMessage) > 0:
            self.errorDialog = QErrorMessage()
            self.errorDialog.showMessage(errorMessage)
        else:
            self.figure = Figure(
                self.figureNameTextBox.toPlainText().strip(),
                self.functionTextBox.toPlainText().strip(),
                int(self.maxTextBox.toPlainText().strip()),
                int(self.minTextBox.toPlainText().strip()),
                self.figure.color,
                self.figure.interpreter
            )
            self.mainWindow.GetFigureToAdd()
            self.close()


class EditFigureDialog(FigureDialog):
    def __init__(self, figure, mainWindow):
        super(EditFigureDialog, self).__init__()
        self.setupUi()
        self.figure = figure
        self.UpdateFigure()
        self.mainWindow = mainWindow

    def EditChangeSetup(self):
        self.horizontalSpacer2 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.removeButton = QPushButton(self.layoutWidget2)
        self.horizontalLayout6.addWidget(self.removeButton)
        self.horizontalLayout6.addItem(self.horizontalSpacer2)

    def EditChangeRetranslate(self):
        self.removeButton.setText(QCoreApplication.translate("figure_properity_dialog", u"Remove", None))

    def Connect(self):
        self.cancelButton.clicked.connect(self.close)
        self.removeButton.clicked.connect(self.DeleteEvent)
        self.colorButton.clicked.connect(self.ColorBick)
        self.okButton.clicked.connect(self.OkEvent)

    def UpdateFigure(self):
        self.figureNameTextBox.setText(self.figure.name)
        self.functionTextBox.setText(self.figure.function)
        self.maxTextBox.setText(str(self.figure.max))
        self.minTextBox.setText(str(self.figure.min))
        self.UpdateColorButton(self.figure.color)
        self.maxTextBox.setAlignment(Qt.AlignCenter)
        self.minTextBox.setAlignment(Qt.AlignCenter)

    def DeleteEvent(self):
        self.mainWindow.DeleteFigure()
        self.close()

    def OkEvent(self):
        print('sd')
        errorMessage = self.IsValid()
        if len(errorMessage) > 0:
            self.errorDialog = QErrorMessage()
            self.errorDialog.showMessage(errorMessage)
        else:
            self.figure = Figure(
                self.figureNameTextBox.toPlainText().strip(),
                self.functionTextBox.toPlainText().strip(),
                int(self.maxTextBox.toPlainText().strip()),
                int(self.minTextBox.toPlainText().strip()),
                self.figure.color,
                self.figure.interpreter
            )
            self.mainWindow.UpdateFigure()
            self.close()



