from PySide2.QtWidgets import QListWidgetItem


class Figure:
    def __init__(self, name=None, function=None, max=None, min=None, color=None):
        self.name = name
        self.function = function
        self.max = max
        self.min = min
        self.color = color

    def __repr__(self):
        return f"{self.name}, {self.function}, {self.max}, {self.min}"

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