"""Tea Party Planner"""

__author__ = "730571325"


def main_planner(guests: int) -> None:
    """Planning out our wonderful tea party"""

    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))


def tea_bags(people: int) -> int:
    """Determines number of tea bags that we need"""
    return people * 2


def treats(people: int) -> int:
    """determines how many treats that we need"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Cost Function"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guest are attending your tea party?")))
