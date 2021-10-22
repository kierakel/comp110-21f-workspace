"""Practice with dictionaries."""

__author__ = "123456789"


def invert(strings: dict[str, str]) -> dict[str, str]:
    x = {}
    for string in strings:
        key: str = strings[string]
        value: str = string
        x[key] = value
    return x


def favorite_color(colors: dict[str, str]) -> str:
    fav: str = ""
    for value in colors:
        if value != colors[value]:
            fav = colors[value]
        else:
            fav = value
    return fav


def count(list: list[str]) -> dict[str, int]:
    empty = {}
    i: int = 1
    for string in list:
        if string in empty:
            i += 1
        else: 
            i
    return empty


print(count(["kris", "kaki", "kris"]))