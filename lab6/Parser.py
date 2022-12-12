from FA import *
from Grammar import *


class ParserConfig:
    def __init__(self, grammar):
        self.grammar = grammar
        self.s = 'q'
        self.i = 0
        self.alpha = []
        self.beta = []

    def expand(self):
        current = self.beta.pop()
        production = self.grammar.getProductionsForNonTerminal(current)
        rules = production[0][1].split()[0]
        if rules != "epsilon":
            self.beta += reversed(rules)
        self.beta.append(rules + "#0")

    def advance(self):
        self.i += 1
        terminal = self.beta.pop()
        self.alpha.append(terminal)


class ParserTests:
    def testAdvance(self, parser):
        parser.beta.append('a')
        parser.advance()
        assert (len(parser.beta) == 0)
        assert (parser.alpha.pop() == 'a')
        assert (parser.i == 1)
        parser.i -= 1

    def testExpand(self,parser):
        parser.beta.append('S')
        parser.expand()
        assert (parser.beta.pop() == 'aA#0')

