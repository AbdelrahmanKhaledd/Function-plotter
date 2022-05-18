from Interpreter.SyntaxTree import *
from Interpreter.Lexer import *

class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.currentToken = self.lexer.GetNextToken()

    def Take(self, tokenType):
        if self.currentToken.type == tokenType :
            self.currentToken = self.lexer.GetNextToken()
        else:
            raise Exception(f'Invalid syntax in {self.lexer.currentChar}')

    def Factor(self):
        token = self.currentToken
        if token.type == Tokens.PLUS:
            self.Take(Tokens.PLUS)
            node = UnaryOp(token, self.Factor())
            return node

        elif token.type == Tokens.MINUS:
            self.Take(Tokens.MINUS)
            node = UnaryOp(token, self.Factor())
            return node

        elif token.type == Tokens.NUMBER:
            self.Take(Tokens.NUMBER)
            node =Num(token)
            return node

        elif token.type == Tokens.VAR:
            self.Take(Tokens.VAR)
            node = Var(token)
            return node

        elif token.type == Tokens.LPAREN:
            self.Take(Tokens.LPAREN)
            node = self.expr()
            self.Take(Tokens.RPAREN)
            return node

    def Prim(self):
        node = self.Factor()
        while self.currentToken.type == Tokens.EXP:
            token = self.currentToken
            self.Take(Tokens.EXP)
            left = node
            right = self.Factor()
            if left == None or right == None:
                raise Exception(f'Invalid syntax in {self.lexer.currentChar}')

            node = BinOp(left=left, op=token, right=right)
        return node

    def Term(self):
        node = self.Prim()

        while self.currentToken.type in (Tokens.MUL, Tokens.DIV):
            token = self.currentToken
            if token.type == Tokens.MUL:
                self.Take(Tokens.MUL)
            elif token.type == Tokens.DIV:
                self.Take(Tokens.DIV)
            left = node
            right = self.Prim()
            if left == None or right == None:
                raise Exception(f'Invalid syntax in {self.lexer.currentChar}')
            node = BinOp(left=left, op=token, right=right)
        return node

    def BuildTree(self):
        node = self.Term()
        while self.currentToken.type in (Tokens.PLUS, Tokens.MINUS):
            token = self.currentToken
            if token.type == Tokens.PLUS:
                self.Take(Tokens.PLUS)
            elif token.type == Tokens.MINUS:
                self.Take(Tokens.MINUS)
            left = node
            right = self.Term()
            if left == None or right == None:
                raise Exception(f'Invalid syntax in {self.lexer.currentChar}')

            node = BinOp(left=left, op=token, right=right)
        return node

    def parse(self):
        return SyntaxTree(self.BuildTree())

