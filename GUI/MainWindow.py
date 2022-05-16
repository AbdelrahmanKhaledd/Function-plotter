from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from GUI.CanvasFigure import MplCanvas
from GUI.AddFigureDialog import AddFigureDialog
from GUI.Figure import Figure, FigureList
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from GUI.EditFigureDialog import EditFigureDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.selectedItemIndex = 0
        self.figureList = FigureList()
        self.canv = MplCanvas()
        self.navigationBar = NavigationToolbar2QT(self.canv , None, True)
        self.setupUi()

    def setupUi(self):
        self.resize(1040, 648)
        self.action_open_state = QAction(self)
        self.action_open_state.setObjectName(u"action_open_state")
        self.action_save_State_As = QAction(self)
        self.action_save_State_As.setObjectName(u"action_save_State_As")

        self.actionPan = QAction(self)
        self.actionPan.setObjectName(u"actionPan")
        icon = QIcon()
        icon.addFile(u"./assets/pan.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPan.setIcon(icon)

        self.actionZoom = QAction(self)
        self.actionZoom.setObjectName(u"actionZoom")
        icon1 = QIcon()
        icon1.addFile(u"./assets/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionZoom.setIcon(icon1)

        self.actionScreenshot = QAction(self)
        self.actionScreenshot.setObjectName(u"actionScreenshot")
        icon2 = QIcon()
        icon2.addFile(u"./assets/index.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionScreenshot.setIcon(icon2)

        self.actionReset = QAction(self)
        self.actionReset.setObjectName(u"actionReset")
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

        self.figure_list = QListWidget(self.layoutWidget)
        self.verticalLayout.addWidget(self.figure_list)
        self.figure_list.setMinimumSize(QSize(240, 0))
        self.figure_list.setMaximumSize(QSize(250, 16777215))
        self.figure_list.setStyleSheet(
            "QListWidget::item:selected {background-color: white; border-left: 2px solid red;}");
        self.horizontalLayout = QHBoxLayout()
        self.add_push_button = QPushButton(self.layoutWidget)
        self.horizontalLayout.addWidget(self.add_push_button)
        self.reset_push_button = QPushButton(self.layoutWidget)
        self.horizontalLayout.addWidget(self.reset_push_button)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.splitter.addWidget(self.layoutWidget)
        self.drawing_area = QWidget(self.splitter)
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
        self.toolBar = QToolBar(self)
        self.toolBar.setObjectName(u"toolBar")
        font = QFont()
        font.setBold(False)
        self.toolBar.setFont(font)
        self.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.action_open_state)
        self.menuFile.addAction(self.action_save_State_As)
        self.toolBar.addAction(self.actionPan)
        self.toolBar.addAction(self.actionZoom)
        self.toolBar.addAction(self.actionScreenshot)
        self.toolBar.addAction(self.actionReset)
        self.vBox = QVBoxLayout()
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
        self.actionPan.setText(QCoreApplication.translate("main_window", u"Pan", None))
        self.actionZoom.setText(QCoreApplication.translate("main_window", u"Zoom", None))
        self.actionScreenshot.setText(QCoreApplication.translate("main_window", u"Screenshot", None))
        self.actionReset.setText(QCoreApplication.translate("main_window", u"Reset", None))
        self.add_push_button.setText(QCoreApplication.translate("main_window", u"Add", None))
        self.reset_push_button.setText(QCoreApplication.translate("main_window", u"Reset", None))
        self.menuFile.setTitle(QCoreApplication.translate("main_window", u"File", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("main_window", u"toolBar", None))
        self.add_push_button.clicked.connect(self.ShowAddFigureEvent)
        self.reset_push_button.clicked.connect(self.resetAll)
        self.figure_list.itemDoubleClicked.connect(self.EditEvent)
        self.actionPan.triggered.connect(self.navigationBar.pan)
        self.actionZoom.triggered.connect(self.navigationBar.zoom)
        self.actionScreenshot.triggered.connect(self.navigationBar.save_figure)
        self.actionReset.triggered.connect(self.navigationBar.home)

    # retranslateUi

    def test(self):
        print("s")

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


