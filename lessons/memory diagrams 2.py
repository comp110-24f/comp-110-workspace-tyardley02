def speak(sound: str, repeat: int) -> None:
    print(sound * repeat)


speak(sound="woof", repeat=3)
speak(sound="meow", repeat=2)

print(speak(sound="woof", repeat=3))
# This line of code prints the result and then "None" because the return value is none.
