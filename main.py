from Lexer import lexer
from Parser import Parser
from Interpreter import Interpreter
import sys

args = sys.argv

strInput = "z = 100\nprint z+1\n"

with open(args[1]) as f:
    strInput = f.read()

parse = Parser(lexer(strInput))
Interpreter(parse.parse())
