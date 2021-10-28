"""Practice with dictionaries."""

__author__ = "730350912"


def invert(strings: dict[str, str]) -> dict[str, str]:
    """A function to invert the keys and values of a dictionary."""
    x = {}
    for string in strings:
        key: str = strings[string]
        value: str = string
        if key in x:
            raise KeyError("Cannot have the same key!")
        x[key] = value
    return x


def favorite_color(colors: dict[str, str]) -> str:
    """A function to identify the color appearing in a dictionary the most."""
    favorite: list[str] = []
    fav_color: str = ""
    for key in colors:
        if colors[key] in favorite:
            fav_color = colors[key]
        favorite.append(colors[key])
    if fav_color not in favorite:
        fav_color = favorite[0]
    return fav_color


print(favorite_color({"Marc": "green", "Ezri": "blue", "Kris": "green", "Kiera": "blue"}))


def count(list: list[str]) -> dict[str, int]:
    """A function to count how many times a key appears while iterating through a dictionary."""
    empty = {}
    i: int = 1
    for string in list:
        if string in empty:
            i += 1
        else: 
            i = 1
        empty[string] = i
    return empty