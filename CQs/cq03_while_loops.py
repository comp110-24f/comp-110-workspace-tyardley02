"""CQ03: Practice with while loops"""

__author__ = "730467229"


def num_instances(phrase: str, search_char: str) -> None:
    count: int = 0  # keeps track of the number of times search_char occurs
    index: int = 0  # keeps track of where you are in phrase
    while index < len(
        phrase
    ):  # while loop that runs while index < length of the phrase
        if (
            phrase[index] == search_char
        ):  # if the indexed character equals search_char it increases count by 1
            count += 1
        else:  # otherwise count remains the same
            count = count
        index += 1  # then the index is increased by 1

    print(count)  # the function prints the final count
