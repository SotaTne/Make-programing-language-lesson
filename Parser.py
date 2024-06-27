def parser(tokens):
    parsed = []

    def error(message):
        # エラーメッセージを表示し、プログラムを終了する
        print(message)
        exit()

    def stmt(current):
        # トークンリストの末尾に達していない場合
        if len(tokens) > current:
            # 式を解析し、結果を left として取得
            current, left = expr(current)
            # "print" 文の場合
            if (
                current < len(tokens)
                and left["op"] == "IDENTIFY"
                and left["val"] == "print"
            ):
                # "print" 文の引数を解析
                current, val = expr(current)
                # 解析結果を文としてパース済リストに追加
                parsed.append({"op": "PRINT", "val": val})
            else:
                # その他の文の場合
                parsed.append({"op": "", "val": left})

            # 改行トークンのチェック、または最後のトークンでない場合
            if (current < len(tokens) and tokens[current]["type"] == "NEWLINE") or (
                current == len(tokens) - 1 and tokens[current]["type"] != "NEWLINE"
            ):
                current += 1
            elif current < len(tokens):
                # 改行がないまたは、最後のトークンでない場合はエラーを報告
                print(tokens[current]["type"])
                error("Expected NEWLINE in stmt")

            # 再帰的に次の文を解析
            stmt(current)
        return current

    def expr(current):
        # 算術式を解析し、結果を取得
        current, val = arith_expr(current)
        # 代入演算子 "=" のチェック
        if current < len(tokens) and tokens[current]["type"] == "EQUAL":
            current += 1
            # 右辺の式を再帰的に解析
            current, right = expr(current)
            return current, {
                "op": "ASSIGNMENT",
                "left": val,
                "right": right,
            }
        return current, val

    def arith_expr(current):
        # 項を解析し、結果を取得
        current, val = term(current)
        # 加算または減算演算子のチェック
        while current < len(tokens) and (
            tokens[current]["type"] == "ADD" or tokens[current]["type"] == "MINUS"
        ):
            Type = tokens[current]["type"]
            current += 1
            # 右辺の項を再帰的に解析
            current, right = term(current)
            val = {"op": Type, "left": val, "right": right}
        return current, val

    def term(current):
        # プライマリを解析し、結果を取得
        current, val = primary(current)
        # 乗算または除算演算子のチェック
        while current < len(tokens) and (
            tokens[current]["type"] == "STAR" or tokens[current]["type"] == "SLASH"
        ):
            Type = tokens[current]["type"]
            current += 1
            # 右辺のプライマリを再帰的に解析
            current, right = primary(current)
            val = {"op": Type, "left": val, "right": right}
        return current, val

    def primary(current):
        # 識別子トークンのチェック
        if current < len(tokens) and tokens[current]["type"] == "IDENTIFY":
            val = tokens[current]["val"]
            current += 1
            return current, {"op": "IDENTIFY", "val": val}
        # 数値トークンのチェック
        elif current < len(tokens) and tokens[current]["type"] == "NUMBER":
            val = tokens[current]["val"]
            current += 1
            return current, {"op": "NUMBER", "val": val}
        else:
            if current < len(tokens):
                print(tokens[current]["type"])
            error("Expected IDENTIFY or NUMBER in primary")

    stmt(0)  # トークンリストの先頭から解析を開始
    return parsed
