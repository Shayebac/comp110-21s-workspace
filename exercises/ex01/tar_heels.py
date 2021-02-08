"""An exercise in remainders and boolean logic."""

__author__ = "730309878"

# Begin your solution here...
val = input("Enter an int: ")
if int(val) % 2 == 0 and int(val) % 7 == 0:
    print("TAR HEELS")
elif  int(val) % 2 == 0:
    print("TAR")
elif int(val) % 7 == 0:
    print("HEELS")
else:
    print("CAROLINA")

