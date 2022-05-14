import enum
class NodeTypes(enum.Enum):
    NUM = 0
    VAR = 1
    UNARY = 2
    BINARY = 3

class Node:
    def __init__(self, type):
        self.type:NodeTypes = type

class BinOp(Node):
    def __init__(self, left, op, right):
        super().__init__(NodeTypes.BINARY)
        self.left = left
        self.token = self.op = op
        self.right = right

class UnaryOp(Node):
    def __init__(self, op, expr):
        super().__init__(NodeTypes.UNARY)
        self.token = self.op = op
        self.expr = expr

class Num(Node):
    def __init__(self, token):
        super().__init__(NodeTypes.NUM)
        self.token = token
        self.value = token.value

class Var(Node):
    def __init__(self, token):
        super().__init__(NodeTypes.VAR)
        self.token = token
        self.value = token.value
        


