"""Create your own adventure project."""

__author__ = "730309878"

from random import randint

points: int
player: str 
SAD_FACE: str 
CELEBRATION_EMOJI: str 

def main() -> None: 
    """Entrypoint of Adventure."""
    print(greet(welcome=str))
    global points
    points = 0
    choice: int = input("Which would you like to do? A: Hint game, B: Hangman game, C: Quit ")
    if choice == "A":
        print(Hint(guess=int)) 
    elif choice == "B":
        print(Hangman(points))
    elif choice =="C":
        print(f"Thank you for playing. You had {points} point(s). Goodbye!")
    

def greet(welcome: str) -> None:
    """Welcome Statement."""
    print("Welcome to the Number Guessing Game!")
    print("You can either guess a number and get hints, or guess a number and play hangman. You have five tries in each game.")
    global SAD_FACE
    SAD_FACE = ("\U0001F625")
    print(f"If you do not guess the right number in five tries, you lose {SAD_FACE}.")
    global player
    player = input("What is your name? ")
    print(f"Welcome {player}.")
    return greet


def Hint(guess: int) -> None: 
    """Option to play game 1."""
    print(f"{player}, welcome to the hint game!")
    global points
    points = 0
    global CELEBRATION_EMOJI
    CELEBRATION_EMOJI = ("\U0001F389")
    while points < 5:
        guess: int = (int(input("Guess a number, 1 through 100. ")))
        number = (randint(1,100))
        if guess != number:
            if guess < number:
                points += 1
                print("Try guessing a greater number")
            else:
                points += 1
                print("Try guessing a lower number")        
        else:
            points += 1
            print(f"Way to go! You guessed it. Game over! {CELEBRATION_EMOJI}")
    print("You are out of guesses. Game over. Try again some other time.")
    return Hint 
    

def Hangman(guesses: int) -> int: 
    """Option to play game 2."""
    print(f"{player}, welcome to hangman.")
    global CELEBRATION_EMOJI
    CELEBRATION_EMOJI = ("\U0001F389")
    guess_one: str = input("Guess a number, 1 through 10 ")
    number = (randint(1,10))
    points: int = 0
    while points < 5: 
        if guess_one == number:
            points += 1
            print(f"Wow, great job. You win! It took you {points} try.  {CELEBRATION_EMOJI}")
        else:
            points += 1
            guess_two: str = input("Wrong. You now have a head. Guess again. You have four tries left. ")
            if guess_two == number:
                    points += 1
                    print(f"Wow, great job. You win! It took you {points} tries. {CELEBRATION_EMOJI}")
            else:
                    points += 1
                    guess_three: str = input("Wrong. You now have a body. Guess again. You have three tries left. ")
                    if guess_three == number:
                        points += 1
                        print(f"Wow, great job. You win! It took you {points} tries. {CELEBRATION_EMOJI}")
                    else:
                        points += 1
                        guess_four: str = input("Wrong. You now have two arms. Guess again. You have two tries left. ")
                        if guess_four == number:
                            points =+ 1
                            print(f"Wow, great job. You win! It took you {points} tries. {CELEBRATION_EMOJI}")
                        else:
                            points += 1
                            guess_five: str = input("Wrong. You now have two legs. This is your last guess. Guess again. ")
                            if guess_five == number:
                                    points =+ 1
                                    print(f"There you go. You win! It took you {points} tries. {CELEBRATION_EMOJI}")
                            else:
                                    points += 1
                                    print("I am sorry you are out of tries. You lose. Try again some other time.")
    return Hangman

                
if __name__ == "__main__":
    main()