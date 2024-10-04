"""EX 03 - Wordle - Creating a program that imitates the game Wordle"""

__author__ = "730467229"


def input_guess(
    secret_word_len: int,
) -> str:  # secret_word_len stores the requested length of the word from the user.
    """This function dictates the correct length of the secret word and checks that
    the user's guess matches that length."""
    guess: str = input(
        f"Enter a {secret_word_len} character word: "
    )  # This prompts the user to enter a word and stores it in the guess variable.""
    while secret_word_len != len(
        guess
    ):  # This starts a loop that runs while the user continues to enter
        # a word of the incorrect length.
        guess = input(
            f"That wasn't {secret_word_len} chars! Try again: "
        )  # This message prints this message and prompts the user for a new input.
    return guess  # If the length is correct then the function returns the guess.


def contains_char(
    secret_word: str, char_guess: str
) -> (
    bool
):  # Given a secret_word and char_guess, this function checks each individual letter
    # to see if char_guess is found in secret_word
    """This function tests each letter to see if it exists in the secret word"""
    assert (
        len(char_guess) == 1
    )  # This assertion does not allow the function to run if len(char_guess) != 1
    index: int = (
        0  # This index allows the while loop to loop through each letter in the word
    )
    while index < len(
        secret_word
    ):  # The while loop runs as long as the index is less than the length of the word
        if (
            secret_word[index] == char_guess
        ):  # This part returns True if the letter is in the word
            return True
        else:  # This part increases the index if the letter is not in the word
            index += 1
    return False  # If the letter is not in the word, the program will return false


# once it has checked each letter


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """This function determines the correctness of letter and position
    for each character in the user guess and returns an emojified representation
    to the user with green, yellow, and white square emojis."""
    assert len(guess) == len(
        secret
    )  # This makes sure the function only operates if the guess is the right length.
    result: str = (
        ""  # This starts an empty string to which each emoji will be concatenated.
    )
    index: int = 0  # This index tracks where the program is in the guess.
    while index < len(
        guess
    ):  # This while loop allows the program to cycle through each letter of the guess
        # and return the appropriate color box emoji.
        if (
            guess[index] == secret[index]
        ):  # If the letter at the same index in both guess and secret matches,
            # it adds a green box.
            result += GREEN_BOX
        elif contains_char(
            secret, guess[index]
        ):  # If not, but contains_char() returns true, it adds a yellow box.
            result += YELLOW_BOX
        else:  # Otherwise, logically, the letter is not in the word at all,
            # and it adds a white box.
            result += WHITE_BOX
        index += (
            1  # Then the program adds 1 to the index to move on to the next letter.
        )
    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 0  # This tracks what turn the user is on.
    while turn < 6:  # This while loop operates until the sixth turn.
        turn += 1  # This advances the turn number.
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(
            len(secret)
        )  # Definining guess keeps track of what the user inputs when prompted
        # so that the program can later check if it matches the secret word.
        # Putting len(secret) as secret_word_len within input_guess() allows the length
        # of the word to be flexible.
        print(
            emojified(guess, secret)
        )  # This prints back the emojified result of the user's guess
        # based on the secret word.
        if guess == secret:  # This checks if the word is correct and if it is,
            # it returns a "You won" message and quits the program.
            print(f"You won in {turn}/6 turns!")
            quit()
    print(
        "x/6 - Sorry, try again tomorrow!"
    )  # If the program makes it this far, the user has lost.
    # It returns this message and then quits the program.
    quit()


if __name__ == "__main__":  # This function allows us to run the module.
    main(secret="codes")
