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

    def another_try(self):
        symbl = self.alpha.pop()
        non_terminal, production_nbr = symbl.split("#")
        production_nbr = int(production_nbr)
        productions = self.grammar.getProductionsForNonTerminal(
            non_terminal)

        current_production = productions[production_nbr]
        for el in current_production:
            el = self.beta.pop()

        if production_nbr < len(productions) - 1:
            new_production = productions[production_nbr + 1]
            if new_production != "epsilon":
                self.beta += reversed(new_production)
            self.beta.append(non_terminal + "#{0}".format(production_nbr + 1))
            self.s = 'q'
            return

        if self.i == 0 and non_terminal == self.grammar.S:
            self.s = 'e'
            return
        self.beta.append(non_terminal)


class ParserTests:
    def testAdvance(self, parser):
        parser.beta.append('a')
        parser.advance()
        assert (len(parser.beta) == 0)
        assert (parser.alpha.pop() == 'a')
        assert (parser.i == 1)
        parser.i -= 1

    def testExpand(self, parser):
        parser.beta.append('S')
        parser.expand()
        assert (parser.beta.pop() == 'aA#0')
