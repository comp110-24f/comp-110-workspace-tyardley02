"""Creating a concatenation function"""

__author__ = "730467229"


def concat(str1: str, str2: str) -> str:
    return str1 + str2


if __name__ == "__main__":
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))
