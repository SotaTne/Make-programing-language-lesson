typesMap = {
    "+": "ADD",  # + の時ADDを返す
    "-": "MINUS",  # - の時MINUSを返す
    "*": "STAR",  # * の時STARを返す
    "/": "SLASH",  # / の時SLASHを返す
    "=": "EQUAL",  # = の時EQUALを返す
    "\n": "NEWLINE",  # \nの時NEWLINEを返す
    "NUMBER": "NUMBER",  # 数値の時NUMBERを返す
    "IDENTIFY": "IDENTIFY",  # 変数や関数の名前に当てはまる時、IDENTIFYを返す
}
# 今回返却するTypeのまとまり


def lexer(input_str):
    tokens = []  # 返すTokenのList
    current = 0  # 現在地について

    while current < len(input_str):
        # 数字のトークン化
        if "1" <= input_str[current] <= "9":  # 1~9の時
            START = current  # STARTを現在の文字が何番目かに保存
            END = current
            while True:
                current += 1
                if (
                    current >= len(input_str) - 1 or not input_str[current].isdigit()
                ):  # 最後の文字、または0~9じゃない時
                    END = current  # ENDを現在の文字が何番目かに保存
                    break
            # Pythonの[A:B]はA~B-1までのindex番号の要素をとってくるもの
            tokens.append({"type": typesMap["NUMBER"], "val": (input_str[START:END])})

        # 識別子(変数名など)のトークン化
        elif (
            input_str[current].isalpha() or input_str[current] == "_"
        ):  # アルファベットかアンダーバー(_)の時
            START = current
            END = current
            while True:
                current += 1  # １つ次の文字へ移動
                if (
                    current >= len(input_str) - 1
                    or (
                        not input_str[current].isalnum()
                        and not input_str[current] == "_"
                        and not input_str[current].isdigit()
                    )
                ):  # 最後の文字でなくて、アルファベットでもアンダーバー(_)でも数字でものないとき
                    END = current
                    break
            # Pythonの[A:B]はA~B-1までのindex番号の要素をとってくるもの
            tokens.append({"type": typesMap["IDENTIFY"], "val": input_str[START:END]})

        # 演算子のトークン化
        elif (
            input_str[current] in typesMap
        ):  # typesMapの中に、当てはまる文字があるかどうか
            tokens.append({"type": typesMap[input_str[current]], "val": ""})
            current += 1

        # 空白文字をスキップ
        elif input_str[current].isspace():
            current += 1

        # 全て当てはまらない時エラーを出力する
        else:
            print("Lexer Error: Invalid character")
            exit()

    return tokens
