"""CQ07: Part 1 - the list functions"""

__author__ = "730467229"


def find_and_remove_max(a: list[int]) -> int:
    if len(a) == 0:
        return -1
    idx: int = 0
    idx2: int = 0
    max: int = a[0]
    while idx < len(a):
        if a[idx] > max:
            max = a[idx]
        idx += 1
    while idx2 < len(a):
        if a[idx2] == max:
            a.pop(idx2)
        else:
            idx2 += 1
    return max
