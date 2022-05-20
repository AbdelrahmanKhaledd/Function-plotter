from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from GUI.CanvasFigure import MplCanvas
from GUI.FigureDialog import AddFigureDialog
from GUI.Figure import Figure, FigureList
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from GUI.FigureDialog import EditFigureDialog
from GUI.State import *
class MainWindow(QMainWindow):
    """Main window widget"""
    def __init__(self):
        super().__init__()
        self.selectedItemIndex = 0
        self.figureList = FigureList()
        self.canv = MplCanvas()
        self.navigationBar = NavigationToolbar2QT(self.canv , None, True)
        self.SetupUi()
        self.state = State(self)
        self.Connect()

    def SetupUi(self):
        self.resize(1040, 648)
        self.actionNewState = QAction(self)
        self.actionOpenState = QAction(self)
        self.actionSaveState = QAction(self)
        self.actionSvaeStateAs = QAction(self)

        self.actionPan = QAction(self)
        icon = QIcon()
        icon.addFile(u"./assets/pan.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPan.setIcon(icon)

        self.actionZoom = QAction(self)
        icon1 = QIcon()
        icon1.addFile(u"./assets/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionZoom.setIcon(icon1)

        self.actionScreenshot = QAction(self)
        icon2 = QIcon()
        icon2.addFile(u"./assets/index.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionScreenshot.setIcon(icon2)

        self.actionReset = QAction(self)
        icon3 = QIcon()
        icon3.addFile(u"./assets/reset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionReset.setIcon(icon3)

        self.centralwidget = QWidget(self)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setGeometry(QRect(5, 5, 1031, 561))

        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.figureWidgetList = QListWidget(self.layoutWidget)
        self.verticalLayout.addWidget(self.figureWidgetList)
        self.figureWidgetList.setMinimumSize(QSize(240, 0))
        self.figureWidgetList.setMaximumSize(QSize(250, 16777215))
        self.figureWidgetList.setStyleSheet(
            "QListWidget::item:selected {background-color: white; border-left: 2px solid red;}")
        self.horizontalLayout = QHBoxLayout()
        self.addPushButton = QPushButton(self.layoutWidget)
        self.resetPushButton = QPushButton(self.layoutWidget)
        self.horizontalLayout.addWidget(self.resetPushButton)
        self.horizontalLayout.addWidget(self.addPushButton)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.splitter.addWidget(self.layoutWidget)
        self.drawingArea = QWidget(self.splitter)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drawingArea.sizePolicy().hasHeightForWidth())
        self.drawingArea.setSizePolicy(sizePolicy)
        self.drawingArea.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.splitter.addWidget(self.drawingArea)
        self.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 1037, 19))
        self.menuFile = QMenu(self.menubar)
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(self)
        font = QFont()
        font.setBold(False)
        self.toolBar.setFont(font)
        self.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionNewState)
        self.menuFile.addAction(self.actionOpenState)
        self.menuFile.addAction(self.actionSaveState)
        self.menuFile.addAction(self.actionSvaeStateAs)
        self.toolBar.addAction(self.actionPan)
        self.toolBar.addAction(self.actionZoom)
        self.toolBar.addAction(self.actionScreenshot)
        self.toolBar.addAction(self.actionReset)
        self.vBox = QVBoxLayout()
        self.canv.setParent(self.drawingArea)
        self.canv.setFocusPolicy(Qt.StrongFocus)
        self.vBox.addWidget(self.canv)
        self.drawingArea.setLayout(self.vBox)
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    # SetupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("main_window", u"Plotter", None))
        self.actionNewState.setText(QCoreApplication.translate("main_window", u"New state", None))
        self.actionOpenState.setText(QCoreApplication.translate("main_window", u"Open state", None))
        self.actionSaveState.setText(QCoreApplication.translate("main_window", u"Save state", None))
        self.actionSvaeStateAs.setText(QCoreApplication.translate("main_window", u"Save state as", None))
        self.actionPan.setText(QCoreApplication.translate("main_window", u"Pan", None))
        self.actionZoom.setText(QCoreApplication.translate("main_window", u"Zoom", None))
        self.actionScreenshot.setText(QCoreApplication.translate("main_window", u"Screenshot", None))
        self.actionReset.setText(QCoreApplication.translate("main_window", u"Reset", None))
        self.addPushButton.setText(QCoreApplication.translate("main_window", u"Add", None))
        self.resetPushButton.setText(QCoreApplication.translate("main_window", u"Reset", None))
        self.menuFile.setTitle(QCoreApplication.translate("main_window", u"File", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("main_window", u"toolBar", None))

    # retranslateUi

    def Connect(self):
        self.addPushButton.clicked.connect(self.ShowAddFigureEvent)
        self.resetPushButton.clicked.connect(self.ResetAll)
        self.figureWidgetList.itemDoubleClicked.connect(self.EditEvent)
        self.actionPan.triggered.connect(self.navigationBar.pan)
        self.actionZoom.triggered.connect(self.navigationBar.zoom)
        self.actionScreenshot.triggered.connect(self.navigationBar.save_figure)
        self.actionReset.triggered.connect(self.navigationBar.home)
        self.actionOpenState.triggered.connect(self.state.OpenState)
        self.actionSaveState.triggered.connect(self.state.Save)
        self.actionSvaeStateAs.triggered.connect(self.state.SaveAs)
        self.actionNewState.triggered.connect(self.state.NewState)


    def EditEvent(self, item : QListWidgetItem):
        self.selectedItemIndex = self.figureWidgetList.row(item)
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

    def ResetAll(self):
       self.figureList.Clear()
       self.figureList.Render(self, self.canv)




