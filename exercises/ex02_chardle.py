"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730467229"


def input_word() -> str:
    user_word: str = str(
        input("Enter a 5-character word: ")
    )  # Asks the user to input a 5-character word
    if (
        len(user_word) == 5
    ):  # If the length of the word given is in fact 5, the program returns the word.
        return user_word
    else:  # Otherwise, the program prints the error message below before exiting.
        print("Error: Word must contain 5 characters.")
        exit()
        return user_word


def input_letter() -> str:
    user_letter: str = str(
        input("Enter a single character:")
    )  # Asks the user to input a single character
    if (
        len(user_letter) == 1
    ):  # If the character is in fact a single character, the program returns it.
        return user_letter
    else:  # Otherwise, the program prints the error message below before exiting.
        print("Error: Character must be a single character.")
        exit()
        return user_letter


def contains_char(word: str, letter: str) -> None:
    count: int = (
        0  # This establishes a variable that keeps track of the number of instances of
        # the letter in the word.
    )
    print(
        "Searching for " + letter + " in " + word
    )  # This line prints back to the user the letter it is searching for in the word.
    if (
        word[0] == letter
    ):  # This checks index 0 to see if the letter matches. Each following if below
        # checks each consecutive index and the program prints back to the reader each
        # index the letter is found at in its own line.
        print(letter + " found at index 0")
        count += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1
    if count == 0:  # If the letter doesn't match any of the indexes,
        # the program returns the below message.
        print("No instances of " + letter + " found in " + word)
    if count > 0:  # If the letter does match some of the indexes, the program prints
        # the variable count as a string as part of the below message to the user.
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:  # This function streamlines the program by calling each function
    # and gathering the user's inputs to perform each opreation.
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":  # This enables us to run the program as a module
    main()
