import enum
class Tokens(enum.Enum):
    NUMBER, VAR, PLUS, MINUS, MUL, DIV, EXP,LPAREN, RPAREN, EOF = (
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    )
class Token(object):
    """ Tokens types
    """
    def __init__(self, type, value):
        self.type:Tokens = type
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
            Token(MUL, '*')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

