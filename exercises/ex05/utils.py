"""EX05 Part 1: Implementing some list utility functions."""

__author__ = "730467229"


def only_evens(input: list[int]) -> list[int]:
    output: list[int] = (
        []
    )  # This creates an empty list to which the evens from the input will be appended.
    for i in input:  # This for loop checks if each number in the input list is even
        # and then appends it to the output list if it is.
        if i % 2 == 0:
            output.append(i)
    return output  # The newly created list, output, is returned.


def sub(input: list[int], start_index: int, end_index: int) -> list[int]:
    output: list[int] = (
        []
    )  # This creates an empty list to which the evens from the input will be appended.
    i: int = start_index
    if (
        start_index < 0
    ):  # If the start index is less than zero, the function just starts
        # at the beginning of the list.
        i = 0
    if end_index + 1 > len(
        input
    ):  # If the end index is too large it is modified to match the length of the input.
        end_index = len(input)
    while i <= (end_index - 1):  # Then, the function cycles through the input list and
        # returns the desired subset as a new list.
        output.append(input[i])
        i += 1
    return output


def add_at_index(input: list[int], element: int, idx: int) -> None:
    if input != []:  # If the list is not an empty list, and...
        if idx >= len(input):  # ...if the index is too large an IndexError is raised.
            raise IndexError("Index is out of bounds for the input list")
    if input == []:  # If the list IS an empty list, and...
        if idx >= 1:  # ... if the index = 1 or greater an IndexError is raised.
            raise IndexError("Index is out of bounds for the input list")
    input.append(1)  # First an arbitrary integer is added to the end of the list.
    for i in range(
        len(input) - 1, idx, -1
    ):  # This for...in range loop cycles from the end of the list to the given index.
        input[i] = input[
            i - 1
        ]  # Within the loop, this moves each int one place to the right,
        # making space for the new element.
    input[idx] = (
        element  # Then the desired index is mutated to equal the desired element.
    )


r: list[int] = []
add_at_index(r, 1, 1)
print(r)
