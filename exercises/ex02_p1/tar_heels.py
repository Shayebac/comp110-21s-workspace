"""Tar Heels exercise redux as a structured program."""

__author__ = "730309878"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))

def tar_heels(choice: int) -> str:
    """Definition of the function."""

    if int(choice) % 2 == 0 and int(choice) % 7 == 0:
        return ("TAR HEELS")
    elif int(choice) % 2 == 0:
        return ("TAR")
    elif int(choice) % 7 == 0:
        return ("HEELS")
    else:
        return ("CAROLINA")

if __name__ == "__main__":
    main()
