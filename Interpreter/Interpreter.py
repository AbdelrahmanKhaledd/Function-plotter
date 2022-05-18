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


# if __name__ == '__main__':
#     while True:
#         text = input('eq ')
#         interpreter = Interpreter(text)
#         interpreter.syntaxTree.PrintNode(interpreter.syntaxTree.root)
#         interpreter.syntaxTree.Optimaizing(interpreter.syntaxTree.root)
#         interpreter.syntaxTree.PrintNode(interpreter.syntaxTree.root)
#
#         x = input('x =')
#
#         result = interpreter.interpret(x)
#         print(result)
#
