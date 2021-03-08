"""EX03 - palindromify function."""

__author__: str = "730309878"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("race", False))
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromify("live on time", False))


def palindromify(word: str, even_odd: bool) -> str:
    """Creates palindrome out of given string."""
    i: int = 0
    new_word: str = ""
    while i < len(word):
        if len(word) % 2 == 0:
            new_word = (word + word[-1::-1])
            i += 1
        else: 
            new_word = (word + (word[::-1]))
            i += 1
    return new_word
   

if __name__ == "__main__":
    main()