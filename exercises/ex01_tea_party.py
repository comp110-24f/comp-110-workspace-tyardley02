"""This program helps you plan supplies for a tea party based on the # of people."""

__author__ = "730467229"


def main_planner(guests: int) -> None:
    """Given the number of guests attending the party,
    this function takes the results produced by
    tea_bags(), treats(), and cost() and prints them in a specific format"""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # This concatenates these strings with the # of guests, converted to a string.
    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # This concatenates "Tea Bags: " with
    # the result of tea_bags(), converted to a string.
    print("Treats: " + str(treats(people=guests)))  # This concatenates "Treats: " with
    # the result of treats(), converted to a string.
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )  # This concatenates "Cost: $" with
        # the result of cost(), converted to a string.
    )


def tea_bags(people: int) -> int:
    """Defines a function 'tea_bags' that takes an integer 'people' as input
    and produces the # of teabags necessary"""
    return people * 2  # The return value is 'people * 2'
    # where 'people' is the value held by the local variable.


def treats(people: int) -> int:
    """Defines a function 'treats' that takes an integer 'people'as input
    and produces the # of treats necessary"""
    return int(
        (tea_bags(people=people) * 1.5)
    )  # The return value is the result of calling tea_bags() and returning
    # the result * 1.5 converted to an int. we set the value of 'people'
    # held by treats() equal to the value of 'people' held by tea_bags()


def cost(tea_count: int, treat_count: int) -> float:
    """Defines a function 'cost' that determines the cost of the tea party
    based on the number of tea bags and treats needed"""
    return (tea_count * 0.50) + (treat_count * 0.75)  # This calculates the cost
    # by multiplying the # of teas by $0.50 and the number of treats by $0.75.


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
# These lines make the program runnable.
