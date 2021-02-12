"""Tar Heels exercise redux as a structured program."""

__author__ = "730309878"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    # TODO 2: Print the response of calling the tar_heels function here.
    print(tar_heels(choice = int))

def tar_heels(val: int) -> str:
    val = input("Enter an int: ")

    if int(val) % 2 == 0 and int(val) % 7 == 0:
        return ("TAR HEELS")
    elif int(val) % 2 == 0:
        return ("TAR")
    elif int(val) % 7 == 0:
        return ("HEELS")
    else:
        return ("CAROLINA")

if __name__ == "__main__":
    main()
