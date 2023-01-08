from FA import *
from Grammar import *
from Parser import ParserConfig, ParserTests

grammar = Grammar()
grammar.readFile("g1.txt")

print(str(grammar))
print(grammar.checkCFG())

print('\n\n\n')
parser = ParserConfig(grammar)
with open('seq.txt') as file:
    for line in file:
        seq = line.split()
file.close()
parser.parse(seq)
prod = parser.alpha
print(prod)
tree = parser.get_tree(prod)
print(tree)
file = open('g1.out', 'w')
for item in tree:
    file.write(str(item) + "\n")
file.close()


