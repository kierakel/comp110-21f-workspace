"""Finding duplicate letters in a word."""

__author__ = "730350912"

word: str = input("Enter a word: ")
duplicate: bool = False
i: int = 0
while i < len(word):
    character = word[i]
    j: int = i + 1
    while j < len(word):
        second = word[j]
        j += 1
        if character != second:
            duplicate
        else:
            duplicate: bool = True
    i += 1
print("Found duplicate: " + str(duplicate))