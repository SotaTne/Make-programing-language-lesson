valMap = {}


[
    {
        "op": "",
        "val": {
            "op": "ASSIGNMENT",
            "left": {"op": "IDENTIFY", "val": "z"},
            "right": {"op": "NUMBER", "val": "100"},
        },
    },
    {
        "op": "PRINT",
        "val": {
            "op": "ADD",
            "left": {"op": "IDENTIFY", "val": "z"},
            "right": {"op": "NUMBER", "val": "1"},
        },
    },
]


def Interpreter(parsed):
    for stmt in parsed:
        runStmt(stmt)


def runStmt(stmt):
    if stmt["op"] == "PRINT":
        expr = runExpr(stmt["val"])
        exprPrint()
    else:
        runExpr(expr)


def runExpr(expr):
    if expr["op"] == "ASSIGNMENT":
        left = runExpr(expr["left"])
        right = runExpr(expr["right"])
        Assign(left, right)
        return right
    elif expr["op"] == "ADD":
        return float(runExpr(expr["left"])) + float(runExpr(expr["right"]))
    elif expr["op"] == "MINUS":
        return float(runExpr(expr["left"])) - float(runExpr(expr["right"]))
    elif expr["op"] == "STAR":
        return float(runExpr(expr["left"])) * float(runExpr(expr["right"]))
    elif expr["op"] == "SLASH":
        return float(runExpr(expr["left"])) / float(runExpr(expr["right"]))

    runArithExpr(expr)


def runArithExpr(expr):
    print()


def Assign(left, right):
    if left:
        valMap[str(left)] = right


def runTerm():
    print()


def runPrimary():
    print()


def exprPrint(expr):
    print(expr["val"])


[
    {"type": "IDENTIFY", "val": "print"},
    {"type": "IDENTIFY", "val": "a"},
    {"type": "EQUAL", "val": ""},
    {"type": "NUMBER", "val": "3"},
    {"type": "STAR", "val": ""},
    {"type": "NUMBER", "val": "1"},
    {"type": "ADD", "val": ""},
    {"type": "NUMBER", "val": "2"},
    {"type": "NEWLINE", "val": ""},
]
