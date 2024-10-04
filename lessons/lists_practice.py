"""Basic syntax of lists."""

# Create an empty list
my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor
print(my_numbers)


# Adding a value to a list
my_numbers.append(1.5)
my_numbers.append(2.3)
print(my_numbers)


# Creating an already populated list
game_points: list[int] = [102, 86, 94]
print(game_points)

# Subscription Notation/Indexing
print(game_points[2])
# Storing subscription in variable
last_game: int = game_points[2]
print(last_game)


# Modifying by Index
# Lists are mutable.
game_points[1] = 72
print(game_points)

# Printing the length of a list
print(len(game_points))


# Removing an item from a list
game_points.pop(1)
print(game_points)


# Function name: display
# Parameter: list of integers
# RV: None
# Print every element in the input list
# Call display on game_points


def display(int_list: list[int]) -> None:
    index: int = 0

    while index < len(int_list):
        print(int_list[index])
        index += 1


display(game_points)

game_points.append(94)
print(game_points)
