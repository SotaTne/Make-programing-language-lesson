from Lexer import lexer
from Parser import Parser
from Interpreter import Interpreter
import sys

args = sys.argv

strInput = "z = 100\nprint z+1\n"
if len(args) == 2:
    with open(args[1]) as f:
        strInput = f.read()
print(lexer(strInput))
parse = Parser(lexer(strInput))

parsed = parse.parse()
print(parsed)
Interpreter(parsed)
[
    {
        "type": "ASSIGNMENT",
        "name": "a",
        "val": {
            "type": "EXPR",
            "op": "ADD",
            "left": "100",
            "right": {"type": "EXPR", "op": "STAR", "left": "2", "right": "3"},
        },
    },
    {"type": "PRINT", "val": "a"},
]
[
    [
        [
            [
                {
                    "val": {
                        "type": "EXPR",
                        "op": "ADD",
                        "left": "1",
                        "right": {
                            "type": "EXPR",
                            "op": "STAR",
                            "left": "2",
                            "right": "3",
                        },
                    },
                }
            ]
        ]
    ]
]
