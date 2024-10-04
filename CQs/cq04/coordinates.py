"""Creating a coordinates function"""

__author__ = "730467229"


def get_coords(xs: str, ys: str) -> None:
    index1: int = 0
    index2: int = 0
    while index1 < len(xs):
        while index2 < len(ys):
            print("(" + xs[index1] + "," + ys[index2] + ")")
            index2 += 1
        index1 += 1
        index2 = 0
