typesMap = {
    "+": "ADD",
    "-": "MINUS",
    "*": "STAR",
    "/": "SLASH",
    "=": "EQUAL",
    "\n": "NEWLINE",
    "NUMBER": "NUMBER",
    "IDENTIFY": "IDENTIFY",
}


def lexer(input_str):
    tokens = []
    current = 0

    while current < len(input_str):
        # 数字のトークン化
        if input_str[current].isdigit():
            start = current
            while current < len(input_str) and input_str[current].isdigit():
                current += 1
            tokens.append(
                {"type": typesMap["NUMBER"], "val": int(input_str[start:current])}
            )

        # 識別子のトークン化
        elif input_str[current].isalpha() or input_str[current] == "_":
            start = current
            while current < len(input_str) and (
                input_str[current].isalnum() or input_str[current] == "_"
            ):
                current += 1
            tokens.append(
                {"type": typesMap["IDENTIFY"], "val": input_str[start:current]}
            )

        # 演算子のトークン化
        elif input_str[current] in typesMap:
            tokens.append({"type": typesMap[input_str[current]], "val": None})
            current += 1

        # 空白文字をスキップ
        elif input_str[current].isspace():
            current += 1

        # エラー処理
        else:
            print("Lexer Error: Invalid character")
            exit()

    return tokens
