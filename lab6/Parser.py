from FA import *
from Grammar import *

# q = normal state
# b = back state
# f = final state
# e = error state


class ParserConfig:
    def __init__(self, grammar: Grammar, s='q', i=0, alpha=[], beta=[]):
        self.grammar = grammar
        self.s = s
        self.i = i
        self.alpha = alpha
        self.beta = beta

    def __str__(self) -> str:
        return "Grammar: \n" + str(self.get_grammar()) + "\n\n" + \
            "S = " + self.s + "\n" + \
            "I = " + str(self.i) + "\n" + \
            "Alpha = " + str(self.alpha) + "\n" + \
            "Beta = " + str(self.beta) + "\n"

    def get_grammar(self) -> Grammar:
        return self.grammar

    def momentary_insuccess(self):
        self.s = 'b'  # back state

    def success(self):
        self.s = 'f'  # final state

    def back(self):
        if len(self.beta):
            self.i -= 1
            terminal = self.beta.pop()
            self.alpha.append(terminal)

            return True
        return False
