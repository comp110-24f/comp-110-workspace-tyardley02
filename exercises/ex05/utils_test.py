"""EX05 Part 2: Defining unit tests for utils.py."""

__author__ = "730467229"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_use_case_return() -> None:
    """This tests whether only_evens produces the expected return list."""
    assert only_evens([10, 12, 13, 14, 15]) == [10, 12, 14]


def test_only_evens_use_case_mutate() -> None:
    """This tests if the function does not mutate the original input list."""
    a: list[int] = [1, 2, 3, 4, 5]
    only_evens(a)
    assert a == [1, 2, 3, 4, 5]


def test_only_evens_edge_case() -> None:
    """This tests the edge case where the input list is empty"""
    assert only_evens([]) == []


def test_sub_use_case_return() -> None:
    """This tests whether sub returns the expected subset list of the input list."""
    assert sub([33, 34, 35, 36, 37, 38], 2, 4) == [35, 36]


def test_sub_use_case_mutate() -> None:
    """This tests whether the original input list for sub remains unmutated."""
    a: list[int] = [4, 5, 6]
    sub(a, 1, 2)
    assert a == [4, 5, 6]


def test_sub_edge_case() -> None:
    """Tests that when unexpected indexes are used, the function defaults to
    using the beginning or end of the list."""
    a: list[int] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert sub(a, -5, 50) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    b: list[int] = []
    assert sub(b, 1, 5) == []


def test_add_at_index_use_case_return() -> None:
    """Tests that a is changed to the expected result based on the input."""
    a: list[int] = [4, 4, 4, 4, 4]
    add_at_index(a, 2, 2)
    assert a == [4, 4, 2, 4, 4, 4]


def test_add_at_index_use_case_mutate() -> None:
    """Tests that the original list has been mutated and
    is not the same as initially defined."""
    a: list[int] = [4, 4, 4, 4, 4]
    add_at_index(a, 1, 2)
    assert a != [4, 4, 4, 4, 4]


def test_add_at_index_edge_case() -> None:
    "Tests if the function works for adding values to an empty list"
    a: list[int] = []
    add_at_index(a, 1, 0)
    assert a == [1]


def test_add_at_index_raises_indexerror() -> None:
    """Test that add_at_index raises an IndexError for an invalid index."""
    a: list[int] = [1]
    with pytest.raises(IndexError):
        add_at_index(a, 4, 5)
