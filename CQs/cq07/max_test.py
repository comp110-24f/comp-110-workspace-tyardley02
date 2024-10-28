"""CQ07: Part 2 - the unit tests"""

__author__ = "730467229"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_return_use_case() -> None:
    assert find_and_remove_max([3, 4, 6, 7, 7, 6, 7]) == 7


def test_find_and_remove_max_mutate_use_case() -> None:
    a: list = [12, 14, 15, 15, 11]
    find_and_remove_max(a)
    assert a == [12, 14, 11]


def test_find_and_remove_max_return_edge_case() -> None:
    b: list = []
    assert find_and_remove_max(b) == -1
