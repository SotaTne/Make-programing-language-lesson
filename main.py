from Lexer import lexer
from Parser import parser

# from Interpreter import Interpreter
import sys

args = sys.argv

strInput = "z = 100\nprint z+1\n"
if len(args) == 2:
    with open(args[1]) as f:
        strInput = f.read()
print(lexer(strInput))
parsed = parser(lexer(strInput))
print(parsed)

# Interpreter(parsed)
