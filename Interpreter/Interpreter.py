from Tokens import *
from SyntaxTree import *
from Lexer import *
from Parser import *
class Interpreter():
    def __init__(self, parser):
        self.parser = parser

    def visit(self, node, x):
        if node.type == NodeTypes.BINARY:
            if node.op.type == Tokens.PLUS:
                return self.visit(node.left, x) + self.visit(node.right, x)
            elif node.op.type == Tokens.MINUS:
                return self.visit(node.left, x) - self.visit(node.right, x)
            elif node.op.type == Tokens.MUL:
                return self.visit(node.left, x) * self.visit(node.right, x)
            elif node.op.type == Tokens.DIV:
                return self.visit(node.left, x) / self.visit(node.right, x)
            elif node.op.type == Tokens.EXP:
                return self.visit(node.left, x) ** self.visit(node.right ,x)

        elif node.type == NodeTypes.UNARY:
            op = node.op.type
            if op == Tokens.PLUS:
                return +self.visit(node.expr, x)
            elif op == Tokens.MINUS:
                return -self.visit(node.expr, x)

        elif node.type == NodeTypes.NUM:
            return node.value
        else:
            return int(x)

    def interpret(self, x ):
        tree = self.parser.parse()
        return self.visit(tree, x )


if __name__ == '__main__':
    while True:
        text = input('eq ')
        lexer = Lexer(text)
        parser = Parser(lexer)
        x = input('x =')
        interpreter = Interpreter(parser)

        result = interpreter.interpret(x)
        print(result)

