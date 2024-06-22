from Parser import parseTypes
from Lexer import typesMap

valMap = {}


def Interpreter(parsed):
    for stmt in parsed:
        process_stmt(stmt)


def expr(node):
    if isinstance(node, dict):
        left = term(node["left"])
        right = expr(node["right"])

        if node["op"] == typesMap["+"]:
            return float(left) + float(right)
        elif node["op"] == typesMap["-"]:
            return float(left) - float(right)
        else:
            return term(node)
    return factor(node)


def term(node):
    if isinstance(node, dict) and node["type"] == parseTypes["expr"]:
        left = factor(node["left"])
        right = expr(node["right"])

        if node["op"] == typesMap["*"]:
            return left * right
        elif node["op"] == typesMap["/"]:
            return left / right
    return factor(node)


def factor(node):
    if isinstance(node, str):
        if node.isalpha():
            return float(valMap[node])
        elif node.isdigit():
            return int(node)
    print(node)
    callErr("has no factor")


def process_stmt(node):
    if node["type"] == parseTypes["assignment"]:
        valMap[node["name"]] = expr(node["val"])
    elif node["type"] == parseTypes["print"]:
        Print(expr(node["val"]))
    else:
        print(node)
        callErr("InterpretError")


def Print(value):
    print(value)


def callErr(error):
    print(error)
    exit()
