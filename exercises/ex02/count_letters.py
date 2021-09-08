"""Counting letters in a string."""

__author__ = "730350912"


letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
i: int = 0
c = ""
while i == 0:
    if word != letter:
        print("Count: 0")
    i = i + 1