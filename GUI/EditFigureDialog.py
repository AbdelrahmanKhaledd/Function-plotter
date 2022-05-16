from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Interpreter.Interpreter import Interpreter
from GUI.Figure import Figure

class EditFigureDialog(QDialog):
    def __init__(self, figure, mainWindow):
        super(EditFigureDialog, self).__init__()
        self.setupUi()
        self.figure = figure
        self.UpdateFigure()
        self.mainWindow = mainWindow

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"edit_figure_dialog")
        self.resize(372, 196)
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(140, 120, 58, 22))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.color_button = QPushButton(self.layoutWidget)
        self.color_button.setObjectName(u"color_button")
        self.color_button.setMinimumSize(QSize(20, 20))
        self.color_button.setMaximumSize(QSize(20, 20))
        self.horizontalLayout_7.addWidget(self.color_button)
        self.layoutWidget_2 = QWidget(self)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 10, 351, 94))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 0))
        self.label_3.setMaximumSize(QSize(16777215, 40))
        self.label_3.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_2.addWidget(self.label_3)
        self.max_textbox = QTextEdit(self.layoutWidget_2)
        self.max_textbox.setObjectName(u"max_textbox")
        self.max_textbox.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(13)
        self.max_textbox.setFont(font)
        self.horizontalLayout_2.addWidget(self.max_textbox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.layoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(30, 0))
        self.label_4.setMaximumSize(QSize(16777215, 40))
        self.label_4.setAlignment(Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.label_4)
        self.min_textbox = QTextEdit(self.layoutWidget_2)
        self.min_textbox.setObjectName(u"min_textbox")
        self.min_textbox.setMaximumSize(QSize(16777215, 40))
        self.min_textbox.setFont(font)
        self.horizontalLayout.addWidget(self.min_textbox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.layoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(47, 0))
        self.label.setMaximumSize(QSize(16777215, 40))
        self.label.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_4.addWidget(self.label)
        self.figure_name_textbox = QTextEdit(self.layoutWidget_2)
        self.figure_name_textbox.setObjectName(u"figure_name_textbox")
        self.figure_name_textbox.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setPointSize(11)
        self.figure_name_textbox.setFont(font1)
        self.horizontalLayout_4.addWidget(self.figure_name_textbox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.layoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_3.addWidget(self.label_2)
        self.function_textbox = QTextEdit(self.layoutWidget_2)
        self.function_textbox.setObjectName(u"function_textbox")
        self.function_textbox.setMaximumSize(QSize(16777215, 40))
        self.function_textbox.setFont(font1)
        self.horizontalLayout_3.addWidget(self.function_textbox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(21, 161, 326, 24))
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ok_button = QPushButton(self.widget)
        self.ok_button.setObjectName(u"ok_button")
        self.horizontalLayout_6.addWidget(self.ok_button)
        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(self.horizontalSpacer)
        self.remove_button = QPushButton(self.widget)
        self.remove_button.setObjectName(u"remove_button")
        self.horizontalLayout_6.addWidget(self.remove_button)
        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)
        self.cancel_button = QPushButton(self.widget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.horizontalLayout_6.addWidget(self.cancel_button)
        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Edit", u"Edit figure", None))
        self.label_5.setText(QCoreApplication.translate("figure_properity_dialog", u"Color", None))
        self.color_button.setText("")
        self.min_textbox.setAlignment(Qt.AlignCenter)
        self.max_textbox.setAlignment(Qt.AlignCenter)
        self.label_3.setText(QCoreApplication.translate("figure_properity_dialog", u"Max", None))
        self.label_4.setText(QCoreApplication.translate("figure_properity_dialog", u"Min", None))
        self.label.setText(QCoreApplication.translate("figure_properity_dialog", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("figure_properity_dialog", u"Function", None))
        self.ok_button.setText(QCoreApplication.translate("figure_properity_dialog", u"Edit", None))
        self.remove_button.setText(QCoreApplication.translate("figure_properity_dialog", u"Remove", None))
        self.cancel_button.setText(QCoreApplication.translate("figure_properity_dialog", u"Cancel", None))

        self.cancel_button.clicked.connect(self.close)
        self.remove_button.clicked.connect(self.DeleteEvent)
        self.color_button.clicked.connect(self.ColorBick)
        self.ok_button.clicked.connect(self.OkEvent)

    # retranslateUi
    def UpdateFigure(self):
        self.figure_name_textbox.setText(self.figure.name)
        self.function_textbox.setText(self.figure.function)
        self.max_textbox.setText(str(self.figure.max))
        self.min_textbox.setText(str(self.figure.min))
        self.UpdateColorButton(self.figure.color)

    def DeleteEvent(self):
        self.mainWindow.DeleteFigure()
        self.close()

    def ColorBick(self):
        color = QColorDialog.getColor()
        if color.isValid():
            print(color.red(), color.green(), color.blue())
            self.figure.color = (color.red(), color.green(), color.blue())
            self.UpdateColorButton(self.figure.color)

    def UpdateColorButton(self, color):
        self.color_button.setStyleSheet(f"background-color: rgb({color[0]},{color[1]},{color[2]});")

    def OkEvent(self):
        errorMessage = self.isValid()
        if len(errorMessage) > 0:
            self.errorDialog = QErrorMessage()
            self.errorDialog.showMessage(errorMessage)
        else:
            self.figure = Figure(
                self.figure_name_textbox.toPlainText().strip(),
                self.function_textbox.toPlainText().strip(),
                int(self.max_textbox.toPlainText().strip()),
                int(self.min_textbox.toPlainText().strip()),
                self.figure.color,
                self.figure.interpreter
            )
            self.mainWindow.UpdateFigure()
            self.close()

    def isValid(self):
        valid = True
        currentMax = int(self.max_textbox.toPlainText())
        currentMin = int(self.min_textbox.toPlainText())
        currentName = self.figure_name_textbox.toPlainText()
        currentFunction = self.function_textbox.toPlainText()
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
