from lessons.first import get_first, remove_first, remove_and_get_first


def test_get_first() -> None:
    """Testing basic behavior for get_first function."""
    assert get_first([4, 5, 6, 7]) == 4


def test_remove_first_use_case() -> None:
    """Testing remove_first removes first element."""
    a: list[int] = [4, 5, 6, 7]
    remove_first(a)
    assert a == [5, 6, 7]


def test_remove_and_get_first_use_case() -> None:
    """Testing remove_and_get first returns the fi"""
    assert remove_and_get_first([4, 5, 6, 7]) == 4
