import json
from PySide2.QtWidgets import *
from GUI.Figure import *
from Interpreter.Interpreter import *
class State:
    def __init__(self, mainWindow):
        self.currentFileName = None
        self.mainWindow = mainWindow

    def GetState(self):
        figuresDict = []
        for figure in self.mainWindow.figureList.list:
            figuresDict.append(figure.ToDict())
        return {'figures':figuresDict}

    def Save(self):
        if  len(self.mainWindow.figureList.list) >0:
            return
        if self.currentFileName == None :
            fileName = self.SaveAs()
            if fileName != None:
                self.currentFileName = fileName
        else:
            file = open(self.currentFileName, 'w')
            file.write(json.dumps(self.GetState()))

    def SaveAs(self):
        fileName = QFileDialog.getSaveFileName(self.mainWindow, 'Save State')

        if fileName == ('', '') or len(self.mainWindow.figureList.list)==0:
            return
        else :
            file = open(fileName[0],'w')
            file.write(json.dumps(self.GetState()))
            file.close()
            return fileName

    def OpenState(self):
        fileName = QFileDialog.getOpenFileName()
        if fileName != ('',''):
            file = open(fileName[0], 'r')
            figures = json.load(file)['figures']
            figuresList = FigureList()
            for figure in figures :
                figuresList.Add(Figure.DictToFigure(figure))
            for figure in figuresList.list:
                figure.interpreter = Interpreter(figure.function)
            self.currentFileName = fileName[0]
            self.mainWindow.figureList = figuresList
            self.mainWindow.figureList.Render(self.mainWindow, self.mainWindow.canv)

    def NewState(self):
        self.Save()
        self.currentFileName = None
        self.mainWindow.figureList.Clear()
        self.mainWindow.figureList.Render(self.mainWindow, self.mainWindow.canv)




