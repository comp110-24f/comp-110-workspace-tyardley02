from lessons.first import get_first, remove_first, remove_and_get_first


def test_get_first() -> None:
    """Testing basic behavior for get_first function."""
    assert get_first([4, 5, 6, 7]) == 4


def test_get_first_edge_case() -> None:
    """Testing get_first on empty list."""
    assert get_first([]) == -1


def test_remove_first_use_case() -> None:
    """Testing remove_first removes first element."""
    a: list[int] = [4, 5, 6, 7]
    remove_first(a)
    assert a == [5, 6, 7]


def test_remove_first_edge_case() -> None:
    """Testing remove_first on empty list. Should not do anything."""
    a: list[int] = []
    remove_first(a)
    assert a == []


def test_remove_and_get_first_use_case() -> None:
    """Testing remove_and_get first returns the first element in a typical input"""
    assert remove_and_get_first([4, 5, 6, 7]) == 4


def test_remove_and_first_mutation_use_case() -> None:
    """Testing remove_and_get_first removes first element in use case"""
    a: list[int] = [4, 5, 6, 7]
    remove_and_get_first(a)
    assert a == [5, 6, 7]
