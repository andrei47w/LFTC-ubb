from FA import *
from Grammar import *
from Parser import ParserConfig, ParserTests

grammar = Grammar()
grammar.readFile("g1.txt")

print(str(grammar))
print(grammar.checkCFG())


print('\n\n\n')
parser = ParserConfig(grammar)
parser.parse(('a','b','a'))
print(parser.alpha)

# parser.momentary_insuccess()
# parser.success()

# print(parser.back())
# print(str(parser))

# testParset = ParserConfig(Grammar())
# parserTest = ParserTests()
# parserTest.testAdvance(testParset)
# parserTest.testExpand(testParset)
