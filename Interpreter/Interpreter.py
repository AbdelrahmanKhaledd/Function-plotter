from Interpreter.Parser import *
from Interpreter.Lexer import *


class Interpreter():
    def __init__(self, text:str):
        self.text = text
        self.lexer = Lexer(self.text)
        self.syntaxTree = Parser(self.lexer).parse()
        self.syntaxTree.PrintTree()
        self.syntaxTree.Optimaizing()
        self.syntaxTree.PrintTree()

    def Interpret(self, x):
        return self.syntaxTree.Calc(self.syntaxTree.root, x)

