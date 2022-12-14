from FA import *
from Grammar import *
from Parser import ParserConfig, ParserTests

grammar = Grammar()
grammar.readFile("g1.txt")

print(str(grammar))
print(grammar.checkCFG())


print('\n\n\n')
parser = ParserConfig(grammar)

parser.momentary_insuccess()
parser.success()

print(parser.back())
print(str(parser))

parser = ParserConfig(grammar)
parserTest = ParserTests()
parserTest.testAdvance(parser)
parserTest.testExpand(parser)
