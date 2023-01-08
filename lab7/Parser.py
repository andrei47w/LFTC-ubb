from FA import *
from Grammar import *


# q = normal state
# b = back state
# f = final state
# e = error state


class ParserConfig:
    def __init__(self, grammar: Grammar, s='q', i=0, alpha=[]):
        self.grammar = grammar
        self.s = s
        self.i = i
        self.alpha = alpha
        self.beta = [grammar.S]

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
        self.i -= 1
        terminal = self.alpha.pop()
        self.beta.append(terminal)

    def expand(self):
        current = self.beta.pop()
        production = self.grammar.getProductionsForNonTerminal(current)
        rules = production[0][1].split()
        if rules != "epsilon":
            self.beta += reversed(rules)
        self.alpha.append(production[0][0] + "#0")

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

        current_production = productions[production_nbr][1].split()
        for production in current_production:
            if production != "epsilon":
                _ = self.beta.pop()

        if production_nbr < len(productions) - 1:
            new_production = productions[production_nbr + 1][1].split()
            if "epsilon" not in new_production:
                self.beta += reversed(new_production)
            self.alpha.append(non_terminal + "#{0}".format(production_nbr + 1))
            self.s = 'q'
            return

        if self.i == 0 and non_terminal == self.grammar.S:
            self.s = 'e'
            return
        self.beta.append(non_terminal)

    def parse(self, word: list) -> list:
        while self.s not in ['f', 'e']:
            if self.s == 'q':
                if self.i == len(word) and len(self.beta) == 0:
                    self.success()
                else:
                    if len(self.beta) > 0 and self.beta[-1] in self.grammar.N:
                        self.expand()
                    else:
                        if self.i < len(word) and len(self.beta) > 0 and \
                                self.beta[-1] == word[self.i]:
                            self.advance()
                        else:
                            self.momentary_insuccess()
            else:
                if self.s == 'b':
                    if len(self.alpha) > 0 and self.alpha[-1] in self.grammar.E:
                        self.back()
                    elif len(self.alpha) > 0:
                        self.another_try()

        if self.s == 'e':
            print('error')
            return None
        print('sequence accepted')
        return self.alpha

    def get_tree(self, production_string):
        if not production_string:
            return []
        result = [(production_string[0].split('#')[0], -1, -1)]
        i = 0
        j = 0
        while j < len(production_string) and i < len(result):
            top = result[i]
            if top[0] not in self.grammar.N:
                i += 1
                continue
            expand_with = None
            while j < len(production_string):
                if '#' not in production_string[j]:
                    j += 1
                    continue
                non_terminal, production_number = production_string[j].split('#')
                if non_terminal == top[0]:
                    expand_with = (non_terminal, production_number)
                    j += 1
                    break
                j += 1
            if j == len(production_string):
                break
            non_terminal, production_number = expand_with
            production_number = int(production_number)
            production = self.grammar.getProductionsForNonTerminal(non_terminal)[production_number][1].split()
            added = 1
            for symbol in production:
                result.insert(i + added, (symbol, i, i + 1 + added))
                added += 1
            result[i + added - 1] = (*result[i + added - 1][:-1], -1)
            i += 1
        return result


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
