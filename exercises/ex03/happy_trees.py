"""Drawing forests in a loop."""

__author__ = "730350912"

TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
a = ""
i: int = 0
while i < depth:
    if depth <= 0:
        print("")
    else: 
        if i <= depth:
            a = a + TREE
            print(a)
    i = i + 1