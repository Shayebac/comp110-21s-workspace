"""EX03 - prime functions."""

__author__: str = "730309878"


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(5))
    print(list_primes(3, 7))


def is_prime(x: int) -> bool:
    """Check prime number."""
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                return False
        else:
            return True 
    else:
        return False


def list_primes(x: int, y: int) -> list[int]:
    """Find the prime numbers between bounds."""
    new_list: list[int] = []
    num: int = x
    while num < y-1:
        for num in range(x, y-1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    new_list.append(num)
                    num += 1
            else:
                num += 1
    return new_list


if __name__ == "__main__":
    main()