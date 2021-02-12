"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730309878"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def fortune_cookie() -> str:
    """Single, random fortune string."""
    fortune = (randint(1, 100))

    if fortune <= 50:
        if fortune <= 25: 
            return ("You will receieve good news very soon.")
        else:
            return ("Luck is coming your way.")
    else:
        if fortune <= 75:
            return ("Your biggest dream will soon come true.")
        else: 
            return ("Your hard work will soon pay off.")

# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
