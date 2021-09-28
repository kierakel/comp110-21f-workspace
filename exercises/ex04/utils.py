"""List utility functions."""

__author__ = "123456789"


# TODO: Implement your functions here.


def all(x: list[int], y: int) -> bool:
    """Return True if int is found in list, return False if otherwise."""
    i: int = 0
    while i < len(x):
        if y != x[i]:
            return False
        i += 1
    return True
    

def is_equal(x: list[int], y: list[int]):
    """Return True if lists x and y are identical, return False if otherwise."""
    i: int = 0
    while i < len(x) and len(y):
        if x[i] != y[i]:
            return False
        i += 1
    return True


def max(x: list[int]):
    """Return the largest number in the list."""
    if len(x) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    while i < len(x):
        if x[i] > x[i + 1]:
            return x[i]
        i += 1