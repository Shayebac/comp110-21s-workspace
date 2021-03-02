"""Create your own adventure project."""

__author__ = "730309878"

from random import randint

points: int 
player: str 
welcome = str
guess = int
guesses = int
SAD_FACE: str 
CELEBRATION_EMOJI: str 


def main() -> None: 
    """Entrypoint of Adventure."""
    greet("Welcome to the Number Guessing Game!")
    global points
    points = 0
    choice: str = input("Which would you like to do? A: Hint game, B: Hangman game, C: Quit ")
    if choice == "A":
        (Hint())
    elif choice == "B":
        points = (Hangman(points))
    elif choice == "C":
        print(f"Thank you for playing. You had {points} point(s). Goodbye!")
    
    
def greet(welcome) -> None:
    """Welcome Statement."""
    print(welcome)
    print("You can either guess a number and get hints, or guess a number and play hangman.")
    print("You have five tries in each game.")
    global SAD_FACE
    SAD_FACE = ("\U0001F625")
    print(f"If you do not guess the right number in five tries, you lose {SAD_FACE}.")
    global player
    player = input("What is your name? ")
    print(f"Welcome {player}.")


def Hint() -> None: 
    """Option to play game 1."""
    print(f"{player}, welcome to the hint game!")
    global points
    points = 0
    global CELEBRATION_EMOJI
    CELEBRATION_EMOJI = ("\U0001F389")
    while points < 5:
        guess1: int = (int(input("Guess a number, 1 through 100. ")))
        number = (randint(1, 100))
        if guess1 != number:
            if guess1 < number:
                points += 1
                print("Try guessing a greater number")
            else:
                points += 1
                print("Try guessing a lower number")        
        else:
            points += 1
            print(f"Way to go! You guessed it. Game over! {CELEBRATION_EMOJI}")
    print("You are out of guesses. Game over. Try again some other time.")
    
    
def Hangman(points: int) -> int: 
    """Option to play game 2."""
    print(f"{player}, welcome to hangman.")
    global CELEBRATION_EMOJI
    CELEBRATION_EMOJI = ("\U0001F389")
    guess_one: int = input("Guess a number, 1 through 10. ")
    number = (randint(1, 10))
    points: int = 0
    while points < 5: 
        if guess_one == number:
            points += 1
            print(f"Wow, great job. You win! It took you {points} try.  {CELEBRATION_EMOJI}")
        else:
            points += 1
            guess_two: int = input("Wrong. You now have a head. Guess again. You have four tries left. ")
            if guess_two == number:
                points += 1
                print(f"Wow, great job. You win! It took you {points} tries. {CELEBRATION_EMOJI}")
            else:
                points += 1
                guess_three: int = input("Wrong. You now have a body. Guess again. You have three tries left. ")
                if guess_three == number:
                    points += 1
                    print(f"Wow, great job. You win! It took you {points} tries. {CELEBRATION_EMOJI}")
                else:
                    points += 1
                    guess_four: int = input("Wrong. You now have two arms. Guess again. You have two tries left. ")
                    if guess_four == number:
                        points += 1
                        print(f"Wow, great job. You win! It took you {points} tries. {CELEBRATION_EMOJI}")
                    else:
                        points += 1
                        guess_five: int = input("Wrong. You now have two legs. This is your last guess. ")
                        if guess_five == number:
                            points += 1
                            print(f"There you go. You win! It took you {points} tries. {CELEBRATION_EMOJI}")
                        else:
                            points += 1
                            print("I am sorry you are out of tries. You lose. Try again some other time.")
    return points

                
if __name__ == "__main__":
    main()