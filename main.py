OUT_PATH = "./5.txt"


def qualified(five: str, word_set: dict) -> bool:
    """
    word_set 是一个包含了每位字母和状态的字典

    状态位:
        g. 字母位置正确
        y. 字母位置不正确
        b. 字母不正确
    """
    keys = [word_set[i][0] for i in range(5)]
    values = [word_set[i][1] for i in range(5)]

    # 排除含不正确字母的单词
    for none_key in [keys[i] for i in range(5) if values[i] == "b"]:
        for i in range(5):
            if five[i] == none_key and values[i] != "g":
                return False

    # 排除不含可能字母的单词
    for position_correct_key in [keys[i] for i in range(5) if values[i] == "y"]:
        if position_correct_key not in five:
            return False

    # 排除不含正确字母的单词 和 可能字母位置不正确的单词
    for i in range(5):
        try:
            not_include_right: bool = values[i] == "g" and list(five)[i] != keys[i]
            not_position_right: bool = values[i] == "y" and list(five)[i] == keys[i]
        except IndexError:
            print(i, word_set)
            exit(0)

        if not_include_right or not_position_right:
            # if not_include_right:
            return False

    return True


def main() -> None:
    """
    main function
    """
    with open(OUT_PATH, mode="r", encoding="utf-8") as dict:

        word_list = dict.readlines()

        while True:

            guessed = list(input("Guessed: "))
            result = list(input("Result: "))

            if result == "ggggg" or len(word_list) == 1:

                print(word_list[0])
                print("This is the correct answer.")
                word_list = dict.readlines()
                continue

            elif len(word_list) == 0:

                print("Something went wrong, please start again.")
                word_list = dict.readlines()
                continue

            length_flag: bool = (len(guessed) == 5) and (len(result) == 5)
            letter_flag: bool = set(result) == {"g", "y", "b"}

            if not (length_flag and letter_flag):

                print("Invalid input!")
                print(length_flag, letter_flag)
                continue

            word_set = [[guessed[i], result[i]] for i in range(5)]
            word_list = [five for five in word_list if qualified(five, word_set)]

            for i in range(len(word_list)):
                print(word_list[i].replace("\n", " "), end="")
                if (i + 1) & 3 == 0:
                    print("\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSee you next time!")

"""
TODO: 已经输入的单词的记忆问题，从而实现自动解答 √
    TODO: 当存在相同字母且状态不同时的处理 √
TODO: 更好看的命令行输出
TODO: 实现游戏+自动解答
TODO: 多字母单词支持
TODO: 更多的猜测次数
"""
