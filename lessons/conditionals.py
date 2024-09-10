"""Practicing my conditionals."""


def less_than_10(num: int) -> None:
    """Tell us if num < 10."""
    if num < 10:  # check if this is true
        print("Small number!")
    else:
        print("Big number!")
    print("Hope that helps!")


less_than_10(num=2)


def wake_up(alarm: bool) -> str:
    """return a message based on if alarm is going off."""
    if alarm is True:
        return "Wake up! Go to Comp 110!"
    else:
        return "Keep sleeping. You deserve it. :)"


print(wake_up(alarm=False))


def check_first_letter(word: str, letter: str) -> str:
    """returns 'match!' if the first character of word is letter"""
    if word[0] == letter:
        return "match!"
    else:
        return "try again..."


print(check_first_letter(word="eagle", letter="e"))


def check_first_letter2(word: str, letter: str) -> None:
    """returns 'match!' if the first character of word is letter"""
    if word[0] == letter:
        print("match!")
    else:
        print("try again...")


check_first_letter2(word="eagle", letter="e")
