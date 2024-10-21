"""Mutating functions."""

__author__ = "730467229"


def manual_append(listx: list[int], intx: int) -> None:
    listx.append(intx)


def double(listy: list[int]) -> None:
    index: int = 0
    while index < len(listy):
        listy[index] = listy[index] * 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
