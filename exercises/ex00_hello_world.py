"""My first exercise in COMP110!"""

__author__ = "730571325"

print("Hello, world!")


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello," + name + "!"


if __name__ == "main":
    print(greet(name=input("What is your name")))
