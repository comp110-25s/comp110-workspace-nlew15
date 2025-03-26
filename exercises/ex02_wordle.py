"""Worlde Beginning"""

__author__ = "730571325"


def contains_char(word_search: str, single_char: str) -> bool:
    """Searches for a letter in a word"""
    assert len(single_char) == 1, f"len('{single_char}') is not 1"
    index: int = 0
    while index < len(word_search):
        if word_search[index] == single_char:
            return True
        else:
            index += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Returns a string that notifies the individual if they are correct"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    result: str = ""
    index: int = 0
    """Displays emojiys for if they are correct or not."""
    while index < len(guess):
        if guess[index] == secret[index]:
            result += GREEN_BOX
        elif contains_char(secret, guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1
    """Returns the result of the users answers"""
    return result


def input_guess(expected_length: int) -> str:
    """Lets the person know if they have the right number or not"""
    guess = input(f"Enter a {expected_length} character word: ")
    """Repeats until they are correct"""
    while len(guess) != expected_length:
        print(f"That wasn't {expected_length} chars! Try again.")
        guess = input(f"Enter a {expected_length} character word: ")

    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    """Current turn number"""

    max_turns: int = 6

    has_won: bool = False
    while turns <= max_turns and not has_won:
        """Prints current turn"""
        print(f"=== Turn {turns}/{max_turns} ===")

        """Ask user for a guess"""
        guess: str = input_guess(len(secret))

        """Show the results in the form of green, yellow, and white boxes"""
        result: str = emojified(guess, secret)
        print(result)

        """Checks if the guess is the secret"""
        if guess == secret:
            has_won = True
        else:

            turns += 1

    """3. After the loop ends, determine if the user won or lost:"""
    if has_won:
        """N is replaced with the turn number at which they guessed correctly"""
        print(f"You won in {turns}/{max_turns} turns!")
    else:

        print(f"X/{max_turns} - Sorry, try again tomorrow!")

    return None


if __name__ == "__main__":
    main(secret="codes")
