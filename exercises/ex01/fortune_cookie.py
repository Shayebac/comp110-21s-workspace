"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730309878"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
fortune = (randint(1, 100))

print("Your fortune cookie says...")

if fortune <= 50:
    if fortune <= 25:
        print("You will receieve good news very soon.")
    else:
            print("Luck is coming your way.")
else:
    if fortune <= 75:
        print("Your biggest dream will soon come true.")
    else: 
            print("Your hard work will soon pay off.")

print("Now, go spread positive vibes!")                   