from Parser import parseTypes
from Lexer import typesMap

valMap = {}


def Interpreter(Parsed):
    for i in Parsed:
        stmt(i)


def expr(n):
    if isinstance(n, dict):
        if n["op"] == typesMap["+"] and n["type"] == parseTypes["expr"]:
            return float(term(n["left"])) + float(expr(n["right"]))
        elif n["op"] == typesMap["-"] and n["type"] == parseTypes["expr"]:
            return float(term(n["left"])) - float(expr(n["right"]))
        else:
            return term(n)
    else:
        return factor(n)


def term(n):
    if isinstance(n, dict):
        if n["type"] == parseTypes["expr"]:
            if n["op"] == typesMap["*"] and n["type"] == parseTypes["expr"]:
                return factor(n["left"]) * expr(n["right"])
            elif n["op"] == typesMap["/"] and n["type"] == parseTypes["expr"]:
                return factor(n["left"]) / expr(n["right"])
            else:
                return factor(n)
    else:
        return factor(n)


def factor(n):
    if isinstance(n, float):
        return n
    if isinstance(n, int):
        return n
    elif isinstance(n, str) and n.isalpha():
        return valMap[n]
    else:
        callErr("has no factor")


def Print(n):
    print(n)


def stmt(n):
    if n["type"] == parseTypes["assignment"]:
        valMap[n["name"]] = expr(n["val"])
    elif n["type"] == parseTypes["print"]:
        Print(str(expr(n["val"])))
    else:
        callErr("InterpretError")


def callErr(error):
    print(error)
    exit()
