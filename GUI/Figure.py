from PySide2.QtWidgets import QListWidgetItem

from GUI.CanvasFigure import MplCanvas
class Figure:
    def __init__(self, name=None, function=None, max=None, min=None, color=None, interpreter=None):
        self.name = name
        self.function = function
        self.max = max
        self.min = min
        self.color = color
        self.interpreter = interpreter

    def __repr__(self):
        return f"{self.name}, {self.function}, {self.max}, {self.min}, {self.color}"

    def ToDict(self):
        return {
            'name':self.name,
            'function':self.function,
            'max':self.max,
            'min':self.min,
            'color':self.color,
        }
    @staticmethod
    def FigureToFigureListItem(figure, item:QListWidgetItem):
        item.setData(4, figure.name)
        item.setData(5, figure.function)
        item.setData(6, figure.max)
        item.setData(7, figure.min)
        item.setData(8, figure.color)

    @staticmethod
    def FigureListItemToFigure(item:QListWidgetItem):
        return Figure(item.data(4), item.data(5), item.data(6), item.data(7), item.data(8))

    @staticmethod
    def DictToFigure(figureDict):
        return Figure(
            figureDict['name'],
            figureDict['function'],
            int(figureDict['max']),
            int(figureDict['min']),
            figureDict['color']
        )




class FigureList:
    def __init__(self):
        self.list = []

    def Add(self, figure:Figure):
        self.list.append(figure)

    def Edit(self, index, figure:Figure):
        self.list[index] = figure

    def Clear(self):
        self.list = []

    def Delete(self, index):
        del self.list[index]

    def Render(self, mainWindow, canvas:MplCanvas):
        mainWindow.figureWidgetList.clear()
        for figure in self.list:
            from GUI.FigureListWidgit import FigureListWidgit
            itemWidget = FigureListWidgit(figure)
            itemList = QListWidgetItem(mainWindow.figureWidgetList)
            itemList.setSizeHint(itemWidget.sizeHint())
            mainWindow.figureWidgetList.addItem(itemList)
            mainWindow.figureWidgetList.setItemWidget(itemList, itemWidget)
        canvas.UpdateFigureList(self.list)
