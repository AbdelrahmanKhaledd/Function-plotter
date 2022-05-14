from Tokens import *
from SyntaxTree import *
from Lexer import *
class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        if token.type == Tokens.PLUS:
            self.eat(Tokens.PLUS)
            node = UnaryOp(token, self.factor())
            return node

        elif token.type == Tokens.MINUS:
            self.eat(Tokens.MINUS)
            node = UnaryOp(token, self.factor())
            return node

        elif token.type == Tokens.NUMBER:
            self.eat(Tokens.NUMBER)
            return Num(token)

        elif token.type == Tokens.VAR:
            self.eat(Tokens.VAR)
            return Var(token)

        elif token.type == Tokens.LPAREN:
            self.eat(Tokens.LPAREN)
            node = self.expr()
            self.eat(Tokens.RPAREN)
            return node

    def prim(self):
        node = self.factor()
        while self.current_token.type == Tokens.EXP:
            token = self.current_token
            self.eat(Tokens.EXP)
            node = BinOp(left=node, op=token, right=self.factor())
        return node

    def term(self):
        node = self.prim()

        while self.current_token.type in (Tokens.MUL, Tokens.DIV):
            token = self.current_token
            if token.type == Tokens.MUL:
                self.eat(Tokens.MUL)
            elif token.type == Tokens.DIV:
                self.eat(Tokens.DIV)

            node = BinOp(left=node, op=token, right=self.prim())
        return node

    def expr(self):
        node = self.term()
        while self.current_token.type in (Tokens.PLUS, Tokens.MINUS):
            token = self.current_token
            if token.type == Tokens.PLUS:
                self.eat(Tokens.PLUS)
            elif token.type == Tokens.MINUS:
                self.eat(Tokens.MINUS)
            node = BinOp(left=node, op=token, right=self.term())

        return node

    def parse(self):
        return self.expr()

