import re

from SymbolTable import SymbolTable as ST


class Tokens:
    def __init__(self):
        self.reserved_words = []
        self.separators = []
        self.operators = []

    def getTokens(self, file_name):
        with open(file_name, 'r') as f:
            f.readline()
            for i in range(11):
                separator = f.readline().rstrip('\n')
                if separator == "space":
                    separator = ' '
                self.separators.append(separator)
            for i in range(14):
                self.operators.append(f.readline().rstrip('\n'))
            for i in range(12):
                self.reserved_words.append(f.readline().rstrip('\n'))


class PIF:
    def __init__(self):
        self.__content = []

    def add(self, token, pos):
        if token.strip() == "":
            return

        self.__content.append((token, pos))

    def __str__(self):
        output = ""

        for pair in self.__content:
            output += str(pair[1]) + " " * (12 - len(str(pair[1]))) + pair[0] + "\n"

        return output


class Scanner:
    def __init__(self, tokens, str_sep):
        self.tokens = tokens
        self.str_sep = str_sep

    def isIdentifier(self, token):
        return re.match(r'^[a-z]([a-zA-Z]|[0-9])*', token) is not None

    def isConstant(self, token):
        return re.match(
            r'^(0|[+\-]?[1-9][0-9]*)$|^' + self.str_sep + '.' + self.str_sep + '$|^' + self.str_sep + '.*' + self.str_sep + '$',
            token) is not None

    def getString(self, line, index):
        token = ''
        quotes_count = 0
        str_end = index

        for i in range(index, len(line)):
            if quotes_count >= 2:
                break

            if line[i] == self.str_sep:
                quotes_count += 1

            token += line[i]
            str_end = i + 1

        return token, str_end

    def getOperator(self, line, index):
        token = ''
        while index < len(line) and line[index] in "".join(self.tokens.operators):
            token += line[index]
            index += 1

        return token, index

    def scanLine(self, line):
        token = ''
        index = 0
        token_list = []

        while index < len(line):
            # check for operator
            if line[index] in "".join(self.tokens.operators):
                if token:
                    token_list.append(token)

                token, index = self.getOperator(line, index)
                token_list.append(token)
                token = ''

            # check for string constant
            elif line[index] == self.str_sep:
                if token:
                    token_list.append(token)

                token, index = self.getString(line, index)
                token_list.append(token)
                token = ''

            # check for separators
            elif line[index] in self.tokens.separators:
                if token:
                    token_list.append(token)

                token, index = line[index], index + 1
                token_list.append(token)
                token = ''

            # other tokens
            else:
                token += line[index]
                index += 1
        if token:
            token_list.append(token)
        return token_list


def scan(file_name):
    with open(file_name, 'r') as file:
        i = 0

        for line in file:
            i += 1
            for token in scanner.scanLine(line.strip()):
                if token in tokens.reserved_words + tokens.separators + tokens.operators:
                    pif.add(token, (-1, -1))

                elif scanner.isIdentifier(token) or scanner.isConstant(token):
                    if token[0] == scanner.str_sep == token[-1]:
                        id = str_constants_st.add(token)

                    elif token.isnumeric():
                        id = nr_constants_st.add(token)

                    else:
                        id = identifiers_st.add(token)
                    pif.add(token, id)

                else:
                    errors.append('Lexical error: `' + token + '` on line ' + str(i))


if __name__ == '__main__':
    identifiers_st = ST(50)
    str_constants_st = ST(50)
    nr_constants_st = ST(50)

    pif = PIF()
    tokens = Tokens()
    scanner = Scanner(tokens, '"')

    tokens.getTokens('token.in')
    errors = []

    scan("p1err.txt")

    with open('st.out', 'w') as file:
        file.write("Identifiers:\n")
        file.write(str(identifiers_st))

        file.write("\nString Constants:\n")
        file.write(str(str_constants_st))

        file.write("\nNumber Constants:\n")
        file.write(str(nr_constants_st))

    with open('pif.out', 'w') as file:
        file.write(str(pif))

    if not errors:
        print("No errors!")
    else:
        print(*errors, sep="\n")
