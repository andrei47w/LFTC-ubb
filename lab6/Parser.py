from FA import *
from Grammar import *


class ParserConfig:
    def __init__(self, grammar):
        self.grammar = grammar
        self.s = 'q'
        self.i = 0
        self.alpha = []
        self.beta = []
