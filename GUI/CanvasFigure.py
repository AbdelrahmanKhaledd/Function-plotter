import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from pylab import *
from matplotlib import figure as figure
import multiprocessing

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
            thread_pool = multiprocessing.Pool(multiprocessing.cpu_count() - 1)
            y = thread_pool.map(figure.interpreter.Interpret, x)
            self.axes.plot(x, y ,c=(float(figure.color[0])/255, float(figure.color[1])/255, float(figure.color[2])/255))
        self.axes.grid()
        self.draw()
