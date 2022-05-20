import enum
from Interpreter.Tokens import *
class NodeTypes(enum.Enum):
    NUM = 0
    VAR = 1
    UNARY = 2
    BINARY = 3

class Node:
    """
    Node of SyntaxTree
    """
    def __init__(self, type):
        self.type:NodeTypes = type

    def Childs(self):
        """
        Get childrens of nodes(left, right,op)
        :return: List of Childerns

        """
        pass

    def __repr__(self):
        pass

class BinOp(Node):
    def __init__(self, left, op, right):
        super().__init__(NodeTypes.BINARY)
        self.left = left
        self.token = self.op = op
        self.right = right
        self.childs = [self.left, self.right]

    def ToNum(self, token):
        self.type = NodeTypes.NUM
        self.token = token
        self.value = token.value
        self.childs = []
        del self.op

    def Childs(self):
        return self.childs

    def __repr__(self):
        return str(self.token)

class UnaryOp(Node):
    def __init__(self, op, expr):
        super().__init__(NodeTypes.UNARY)
        self.token = self.op = op
        self.expr = expr

    def ToNum(self, token):
        self.type = NodeTypes.NUM
        self.token = token
        self.value = token.value
        del self.expr

    def Childs(self):
        return [self.expr]

    def __repr__(self):
        return str(self.token)

class Num(Node):
    def __init__(self, token):
        super().__init__(NodeTypes.NUM)
        self.token = token
        self.value = token.value

    def ToNum(self, token):
        self.type = NodeTypes.NUM
        self.token = token
        self.value = token.value

    def Childs(self):
        return []

    def __repr__(self):
        return str(self.value)

class Var(Node):
    def __init__(self, token):
        super().__init__(NodeTypes.VAR)
        self.token = token
        self.value = token.value

    def Childs(self):
        return []

    def __repr__(self):
        return str(self.value)

class SyntaxTree:
    """
    SyntaxTree containing operations nodes
    """
    def __init__(self, root:Node):
        self.root = root

    def Optimaizing(self):
        """
        Optmaizing sybtaxTree to run faster in calculation
        :return: None
        """
        self._optimaizing(self.root)

    def _optimaizing(self, node):
        #(true ,val)
        res =None
        if node.type == NodeTypes.BINARY:
            left = self._optimaizing(node.left)
            right = self._optimaizing(node.right)
            if node.op.type == Tokens.PLUS:
                res = None if( left ==None or right ==None)  else left + right
            elif node.op.type == Tokens.MINUS:
                res = None if ( left ==None or right ==None) else left - right
            elif node.op.type == Tokens.MUL:
                res = None if ( left ==None or right ==None) else left * right
            elif node.op.type == Tokens.DIV:
                res = None if ( left ==None or right ==None) else left / right
            elif node.op.type == Tokens.EXP:
                res = None if ( left ==None or right ==None) else left ** right

        elif node.type == NodeTypes.UNARY:
            op = node.op.type
            jump = self._optimaizing(node.expr)
            if op == Tokens.PLUS:
                res = None if jump ==None else +jump
            elif op == Tokens.MINUS:
                res = None if jump==None else -jump

        elif node.type == NodeTypes.NUM:
            res = node.value
        else:
            res = None

        if res != None:
            node.ToNum(Token(Tokens.NUMBER, res))
        return res

    def Calc(self, node, x):
        """Return value of equation passsing x (our single variable)"""
        if node.type == NodeTypes.BINARY:
            if node.op.type == Tokens.PLUS:
                return self.Calc(node.left, x) + self.Calc(node.right, x)
            elif node.op.type == Tokens.MINUS:
                return self.Calc(node.left, x) - self.Calc(node.right, x)
            elif node.op.type == Tokens.MUL:
                return self.Calc(node.left, x) * self.Calc(node.right, x)
            elif node.op.type == Tokens.DIV:
                return self.Calc(node.left, x) / self.Calc(node.right, x)
            elif node.op.type == Tokens.EXP:
                return self.Calc(node.left, x) ** self.Calc(node.right ,x)

        elif node.type == NodeTypes.UNARY:
            op = node.op.type
            if op == Tokens.PLUS:
                return +self.Calc(node.expr, x)
            elif op == Tokens.MINUS:
                return -self.Calc(node.expr, x)

        elif node.type == NodeTypes.NUM:
            return node.value
        else:
            return int(x)

    def PrintTree(self):
        """
        print synatxTree.
        Ex:
        ├── Token(Tokens.PLUS, '+')
        │    ├── Token(Tokens.EXP, '^')
        │    │    ├── x
        │    │    └── 2
        │    └── Token(Tokens.MUL, '*')
        │        ├── 3
        │        └── x
        └── 23

        :return:None
        """
        self._printNode(self.root)

    def _printNode(self, node ,indent='',last=True):
        indent_extension = '└── ' if last else '├── '
        print(indent, end='')
        print(indent_extension, end='')
        print(str(node), end='')
        print()
        indent += '    ' if last else '│    '
        childs = node.Childs()
        for i in range(len(childs)):
            self._printNode(childs[i], indent, i == (len(childs)-1))



