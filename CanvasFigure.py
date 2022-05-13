import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg, NavigationToolbar2QT)
import FunctionFigure
from pylab import *
from matplotlib import figure as figure

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self):
        self.fig = figure.Figure()
        self.fig.add_axes((0,0,1,1))
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)

    def Reset(self):
        self.fig.axes.clear()
        self.draw()

    def UpdateFigureList(self ,figureList):
        self.figure.clear()
        self.axes = self.figure.add_subplot(111)
        for figure in figureList:
            x = linspace(figure.min, figure.max)
            y = eval(figure.function)
            self.axes.plot(x, y ,c='r' )
        self.axes.grid()
        self.draw()
