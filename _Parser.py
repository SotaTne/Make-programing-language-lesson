def parser(tokens):
    current = 0
    parsed = []

    def error(message):
        print(message)
        exit()

    def stmt():
        nonlocal current
        if len(tokens) > current:
            left = expr()
            if (
                current < len(tokens)
                and left["op"] == "IDENTIFY"
                and left["val"] == "print"
            ):
                parsed.append({"type": "STMT", "op": "PRINT", "val": expr()})
                if current < len(tokens) and tokens[current]["type"] == "NEWLINE":
                    current += 1
                else:
                    print(tokens[current]["type"])
                    error("Expected NEWLINE in stmt")
                stmt()
            else:
                parsed.append({"type": "STMT", "op": "", "val": left})
                if current < len(tokens) and tokens[current]["type"] == "NEWLINE":
                    current += 1
                else:
                    print(tokens[current]["type"])
                    error("Expected NEWLINE in stmt")
                stmt()

    def expr():
        nonlocal current
        val = arith_expr()
        if current < len(tokens) and tokens[current]["type"] == "EQUAL":
            current += 1
            right = expr()
            return {"type": "EXPR", "op": "ASSIGNMENT", "left": val, "right": right}
        return val

    def arith_expr():
        nonlocal current
        val = term()
        if current < len(tokens) and (
            tokens[current]["type"] == "ADD" or tokens[current]["type"] == "MINUS"
        ):
            Type = tokens[current]["type"]
            current += 1
            right = arith_expr()
            val = {"type": "EXPR", "op": Type, "left": val, "right": right}
        return val

    def term():
        nonlocal current
        val = primary()
        if current < len(tokens) and (
            tokens[current]["type"] == "STAR" or tokens[current]["type"] == "SLASH"
        ):
            Type = tokens[current]["type"]
            current += 1
            right = term()
            val = {"type": "EXPR", "op": Type, "left": val, "right": right}
        return val

    def primary():
        nonlocal current
        if current < len(tokens) and tokens[current]["type"] == "IDENTIFY":
            val = tokens[current]["val"]
            current += 1
            return {"type": "EXPR", "op": "IDENTIFY", "val": val}
        elif current < len(tokens) and tokens[current]["type"] == "NUMBER":
            val = tokens[current]["val"]
            current += 1
            return {"type": "EXPR", "op": "NUMBER", "val": val}
        else:
            if current < len(tokens):
                print(tokens[current]["type"])
            error("Expected IDENTIFY or NUMBER in primary")

    stmt()
    return parsed


print(
    parser(
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
    )
)
[
    {
        "type": "STMT",
        "op": "PRINT",
        "val": {
            "type": "EXPR",
            "op": "ASSIGNMENT",
            "left": {"type": "EXPR", "op": "IDENTIFY", "val": "a"},
            "right": {
                "type": "EXPR",
                "op": "ADD",
                "left": {
                    "type": "EXPR",
                    "op": "STAR",
                    "left": {"type": "EXPR", "op": "NUMBER", "val": "3"},
                    "right": {"type": "EXPR", "op": "NUMBER", "val": "1"},
                },
                "right": {"type": "EXPR", "op": "NUMBER", "val": "2"},
            },
        },
    }
]
[
    {
        "type": "STMT",
        "op": "PRINT",
        "val": {
            "type": "EXPR",
            "op": "ASSIGNMENT",
            "left": {"type": "EXPR", "op": "IDENTIFY", "val": "a"},
            "right": {
                "type": "EXPR",
                "op": "ADD",
                "left": {
                    "type": "EXPR",
                    "op": "STAR",
                    "left": {"type": "EXPR", "op": "NUMBER", "val": "3"},
                    "right": {"type": "EXPR", "op": "NUMBER", "val": "1"},
                },
                "right": {"type": "EXPR", "op": "NUMBER", "val": "2"},
            },
        },
    }
]
