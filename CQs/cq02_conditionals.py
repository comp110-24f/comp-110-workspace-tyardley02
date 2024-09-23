"""CQ02 Conditionals: Number Guessing Game!"""

__author__ = "730467229"


def guess_a_number() -> None:
    secret: int = (
        7  # This defines the secret number to equal 7
        # by creating the local variable secret.
    )
    x: int = int(
        input("Guess a number: ")
    )  # This stores the value the user inputs as a local variable x.
    print(
        "Your guess was " + str(x) + "."
    )  # This line prints back this sentence to the user and the number they guessed.
    if x == secret:
        print("You got it!")  # prints back "You got it!" if the user guesses correctly
    elif x < secret:
        print(
            "Your guess was too low! The secret number is " + str(secret)
        )  # prints back this string concatenated with the secret number
        # if the guess is too low
    else:
        print(
            "Your guess was too high! The secret number is " + str(secret)
        )  # prints back this string concatenated with the secret number
        # if the guess is too high
    return None


if __name__ == "__main__":
    guess_a_number()  # calls the function
