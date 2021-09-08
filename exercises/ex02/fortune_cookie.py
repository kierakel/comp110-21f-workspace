"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730350912"

from random import randint

print("Your fortune cookie says...")

x = (randint(1, 50))
FORTUNE: int = 25

if x == FORTUNE:
    print("You will fall into great riches soon.")
else:
    if x > 40:
        print("You will meet the love of your life soon.")
    else: 
        if x < FORTUNE:
            print("Everything you dream of will be yours.")
        else:
            print("You are exactly where you need to be.")

print("Now, go spread positive vibes!")