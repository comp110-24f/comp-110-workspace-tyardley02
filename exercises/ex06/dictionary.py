"""Practice with dictionary functions"""

__author__ = "730467229"


def invert(one: dict[str, str]) -> dict[str, str]:
    two: dict[str, str] = (
        {}
    )  # This creates an empty dictionary to store the inverted one in.
    for key in one:  # This for loop loops through the keys of the first dictionary.
        if (
            one[key] in two
        ):  # If the value is already found in the second dict it returns an error.
            raise KeyError(
                "Oops! Dictionary one stores the same values for multiple keys."
            )
        two[(one[key])] = (
            key  # Otherwise, it stores the new key/value as the opposite in new dict.
        )
    return two  # The new dictionary is returned.


def favorite_color(colors: dict[str, str]) -> str:
    tracker: dict[str, int] = (
        {}
    )  # the new dictionary is established to track the count of each color.
    for key in colors:  # This loop starts the count of each at zero.
        tracker[colors[key]] = 0
    for key in colors:  # Then it cycles through again and adds one per color.
        tracker[colors[key]] += 1
    max: str = (
        ""  # The starting value for the max is an empty string and
        # it is replaced by the color with the most or the first color to appear.
    )
    tracker[max] = 0
    for key in tracker:
        if (
            tracker[key] > tracker[max]
        ):  # If the count of the key is more than the previous key, the max is updated.
            max = key
    return max  # The color with the most is returned.


def count(values: list[str]) -> dict[str, int]:
    times: dict[str, int] = {}  # An empty dictionary is established.
    for i in values:
        if i in times:
            times[i] += 1  # Adds one for each additional time the value appears.
        else:
            times[i] = 1  # sets equal to one when the first iteration is encountered.
    return times  # the new dictionary is returned.


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    alphabetical: dict[str, list[str]] = {}  # empty dict established.
    for i in words:
        if i[0] in alphabetical:
            alphabetical[i[0].lower()].append(
                i
            )  # if the letter is already a key in the new dictionary,
            # the value is appended
        else:
            alphabetical[i[0].lower()] = (
                []
            )  # if the letter isn't there yet it creates a new key then appends value.
            alphabetical[i[0].lower()].append(i)
    return alphabetical  # the final dictionary is returned.


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    if student not in attendance_log[day]:
        attendance_log[day].append(
            student
        )  # This function simply appends the student at the indicated day.
