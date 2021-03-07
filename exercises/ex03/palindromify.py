"""EX03 - palindromify function."""

__author__: str = "730309878"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("race", False))
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromigy("live on time", False))


def palindromify(x: str, y: bool) -> str:
    """Creates palindrome out of given string."""
    i: int = 0
    while i < len(x):
        if len(x) % 2 == 0:

        else:
    return x   


if __name__ == "__main__":
    main()