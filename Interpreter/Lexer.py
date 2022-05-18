from Interpreter.Tokens import *

class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.currentChar = self.text[self.pos]

    def Advance(self):
        """increasing index by one"""
        self.pos += 1
        if self.pos == len(self.text):
            self.currentChar = None  # Indicates end of input
        else:
            self.currentChar = self.text[self.pos]

    def Whitespace(self):
        """jumping spaces"""
        while self.currentChar is not None and self.currentChar.isspace():
            self.Advance()

    def Number(self):
        """Return numbers in equations like :121"""
        result = ''
        while self.currentChar is not None and self.currentChar.isdigit():
            result += self.currentChar
            self.Advance()
        return int(result)

    def Variable(self):
        """Return a variable symbol like:x """
        result = ''
        while self.currentChar != None and self.currentChar.isalpha():
            result += self.currentChar
            self.Advance()
        return result

    def GetNextToken(self):
        while self.currentChar != None:
            if self.currentChar.isspace():
                self.Whitespace()
                continue
            if self.currentChar.isdigit():
                return Token(Tokens.NUMBER, self.Number())

            if self.currentChar.isalpha():
                return Token(Tokens.VAR, self.Variable())

            if self.currentChar == '+':
                self.Advance()
                return Token(Tokens.PLUS, '+')

            if self.currentChar == '-':
                self.Advance()
                return Token(Tokens.MINUS, '-')

            if self.currentChar == '*':
                self.Advance()
                return Token(Tokens.MUL, '*')

            if self.currentChar == '/':
                self.Advance()
                return Token(Tokens.DIV, '/')

            if self.currentChar == '^':
                self.Advance()
                return Token(Tokens.EXP, '^')

            if self.currentChar == '(':
                self.Advance()
                return Token(Tokens.LPAREN, '(')

            if self.currentChar == ')':
                self.Advance()
                return Token(Tokens.RPAREN, ')')

            raise Exception(f'Invalid character{self.currentChar}')

        return Token(Tokens.EOF, None)

