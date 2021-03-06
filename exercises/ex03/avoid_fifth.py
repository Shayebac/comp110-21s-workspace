"""EX03 - avoid_fifth function."""

__author__: str = "730309878"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("hello"))
    print(avoid_fifth("The sentence we have here possesses E's galore!"))
   

def avoid_fifth(words: str) -> str:
    """Removes e and E from all strings."""
    i: int = 0
    new_words: str = ""
    while i < len(words):
        if words[i] == "e":
            i += 1
        elif words[i] == "E": 
            i += 1 
        else:
            new_words += words[i]
            i += 1
    return new_words

        
if __name__ == "__main__":
    main()