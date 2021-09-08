"""Repeating a beat in a loop."""

__author__ = "730350912"

beat: str = input("What beat do you want to repeat? ")
repeat: int = int(input("How many times do you want to repeat it? "))
b = ""
i: int = 0
if repeat <= 0:
    print("No beat...")
while i < repeat:
    if repeat <= 0:
        print("No beat...")
    else: 
        if i == repeat - 1:
            b = b + beat
        else:
            b = b + beat + " "
    i = i + 1
print(b)