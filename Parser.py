from Lexer import typesMap

parseTypes = {
    "assignment": "ASSIGNMENT",
    "print": "PRINT",
    "expr": "EXPR",
}


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        result = self.program()
        if self.current < len(self.tokens):
            self.callErr("Unexpected token")
        return result

    def program(self):
        result = []
        while self.current < len(self.tokens):
            result.append(self.statement())
        return result

    def statement(self):
        if self.tokens[self.current]["val"] == "print":
            return self.print_stmt()
        elif self.tokens[self.current]["type"] == typesMap["IDENTIFY"]:
            return self.assignment()
        else:
            self.callErr(f"Unexpected token: {self.tokens[self.current]['val']}")

    def assignment(self):
        name = self.match(typesMap["IDENTIFY"])
        self.match(typesMap["="])
        expr = self.expression()
        self.match(typesMap["\n"])
        return {
            "type": parseTypes["assignment"],
            "name": name,
            "val": expr,
        }

    def print_stmt(self):
        if self.match(typesMap["IDENTIFY"]) == "print":
            expr = self.expression()
            self.match(typesMap["\n"])
            return {
                "type": parseTypes["print"],
                "val": expr,
            }

    def expression(self):
        result = self.term()
        while self.current < len(self.tokens) and self.tokens[self.current]["type"] in (
            typesMap["+"],
            typesMap["-"],
        ):
            op = self.tokens[self.current]["type"]
            self.match(op)
            right = self.term()
            result = {
                "type": parseTypes["expr"],
                "op": op,
                "left": result,
                "right": right,
            }
        return result

    def term(self):
        result = self.factor()
        while self.current < len(self.tokens) and self.tokens[self.current]["type"] in (
            typesMap["*"],
            typesMap["/"],
        ):
            op = self.tokens[self.current]["type"]
            self.match(op)
            right = self.factor()
            result = {
                "type": parseTypes["expr"],
                "op": op,
                "left": result,
                "right": right,
            }
        return result

    def factor(self):
        token = self.tokens[self.current]
        if token["type"] == typesMap["IDENTIFY"]:
            return self.match(typesMap["IDENTIFY"])
        elif token["type"] == typesMap["NUMBER"]:
            return self.match(typesMap["NUMBER"])
        else:
            self.callErr(f"Unexpected token: {token['val']}")

    def match(self, expected_type):
        if self.tokens[self.current]["type"] == expected_type:
            value = self.tokens[self.current]["val"]
            self.current += 1
            return value
        else:
            self.callErr(
                f"Expected {expected_type}, got {self.tokens[self.current]['type']}"
            )

    def callErr(self, error):
        print("haveError")
        print(error)
        print(self.tokens[self.current]["val"])  # エラートークンを出力
        exit()
