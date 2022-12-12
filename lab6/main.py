from FA import *


class Grammar:
    def __init__(self, N: list = [], E: list = [], P: list = [], S: str = "") -> None:
        self.N = N  # Non-terminals
        self.E = E  # Terminals
        self.P = P  # Productions
        self.S = S  # Starting point

    def __str__(self):
        return "N = { " + ', '.join(self.N) + " }\n\n" \
            "E = { " + ', '.join(self.E) + " }\n\n" \
            "S = { " + self.S + " }\n\n" \
            "P = { " + str(self.P) + " }\n"

    def setN(self, N):
        self.N = N

    def setE(self, E):
        self.E = E

    def setP(self, P):
        self.P = P

    def setS(self, S):
        self.S = S

    @staticmethod
    def parseLine(line):
        return line.strip().split(' ')[2:]

    def readFile(self, file_name):
        with open(file_name) as file:
            N = Grammar.parseLine(file.readline())
            E = Grammar.parseLine(file.readline())
            S = Grammar.parseLine(file.readline())[0]

            file.readline()
            P = []
            for line in file:
                lhs, rhs = line.split('->')
                lhs = lhs.strip()
                rhs = [value.strip() for value in rhs.split('|')]

                for value in rhs:
                    P.append((lhs, value))

            self.setN(N)
            self.setP(P)
            self.setE(E)
            self.setS(S)

    def checkCFG(self):
        return True


grammar = Grammar()
grammar.readFile("g1.txt")

print(str(grammar))
print(grammar.checkCFG())
