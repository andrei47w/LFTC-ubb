from FA import *
from Grammar import Grammar
from Parser import ParserConfig, ParserTests





grammar = Grammar()
grammar.readFile("g1.txt")

print(str(grammar))
print(grammar.checkCFG())

parser = ParserConfig(grammar)
parserTest = ParserTests()
parserTest.testAdvance(parser)
parserTest.testExpand(parser)