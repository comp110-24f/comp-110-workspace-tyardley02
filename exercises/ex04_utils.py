"""Docstring"""

__author__ = "730467229"


def all(num_list: list[int], num1: int) -> bool:
    for elem in num_list:  # This for...in loop cycles through each element in the list
        # and checks if it does not match the given integer.
        if num1 != elem:
            return (
                False  # If any of the numbers don't match the function returns False.
            )
    return True  # Otherwise, the function returns True.


def max(
    num_list: list[int],
) -> int:  # This function returns the maximum value from the list you input
    if len(num_list) == 0:
        raise ValueError(
            "max() arg is an empty list"
        )  # This anticipates a potential error and the message that will be returned.
    idx = num_list[0]  # This is a placeholder that keeps track of the current max
    # up to the point the loop has reached.
    for (
        elem
    ) in (
        num_list
    ):  # This loops through the list and checks if each number is greater than
        # the current max, and updates it if greater.
        if elem >= idx:
            idx = elem
    return idx  # When the function is done running through the list it returns the max.


def is_equal(
    num_list_1: list[int], num_list_2: list[int]
) -> (
    bool
):  # This function checks two lists and sees if they are deeply equal to one another.
    idx: int = (
        0  # This tracks the index of the item that is compared between the lists.
    )
    if len(num_list_1) != len(
        num_list_2
    ):  # If the lists do not have the same length, this immediately returns False.
        return False
    while idx < len(
        num_list_1
    ):  # This while loop cycles through each item in both lists and sees if they are =
        if (
            num_list_1[idx] != num_list_2[idx]
        ):  # If any element does not match, the function returns False.
            return False
        idx += 1
    return True  # If the function passes all of these tests, it returns True.


def extend(
    num_list_1: list[int], num_list_2: list[int]
) -> None:  # This function takes two lists and appends
    # every element of the second list to the first in succession.
    for elem in num_list_2:
        num_list_1.append(elem)
