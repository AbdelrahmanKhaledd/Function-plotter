from Tokens import *
class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.currentChar = self.text[self.pos]

    def advance(self):
        self.pos += 1
        if self.pos == len(self.text):
            self.currentChar = None  # Indicates end of input
        else:
            self.currentChar = self.text[self.pos]

    def whitespace(self):
        while self.currentChar is not None and self.currentChar.isspace():
            self.advance()

    def number(self):
        result = ''
        while self.currentChar is not None and self.currentChar.isdigit():
            result += self.currentChar
            self.advance()
        return int(result)

    def variable(self):
        """Return a variable symbol like:x """
        result = ''
        while self.currentChar != None and self.currentChar.isalpha():
            result += self.currentChar
            self.advance()
        return result

    def get_next_token(self):
        while self.currentChar != None:
            if self.currentChar.isspace():
                self.whitespace()
                continue
            if self.currentChar.isdigit():
                return Token(Tokens.NUMBER, self.number())

            if self.currentChar.isalpha():
                return Token(Tokens.VAR, self.variable())

            if self.currentChar == '+':
                self.advance()
                return Token(Tokens.PLUS, '+')

            if self.currentChar == '-':
                self.advance()
                return Token(Tokens.MINUS, '-')

            if self.currentChar == '*':
                self.advance()
                return Token(Tokens.MUL, '*')

            if self.currentChar == '/':
                self.advance()
                return Token(Tokens.DIV, '/')

            if self.currentChar == '^':
                self.advance()
                return Token(Tokens.EXP, '^')

            if self.currentChar == '(':
                self.advance()
                return Token(Tokens.LPAREN, '(')

            if self.currentChar == ')':
                self.advance()
                return Token(Tokens.RPAREN, ')')

            raise Exception('Invalid character')

        return Token(Tokens.EOF, None)

