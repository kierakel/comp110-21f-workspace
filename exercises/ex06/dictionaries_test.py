"""Unit tests for dictionary functions."""

from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730350912"


def test_invert_correctly_inverted() -> None:
    """A test of whether the function invert correctly inverts a dictionary's keys and values."""
    xs = {'apple': 'cat'}
    assert invert(xs) == {'cat': 'apple'}


def test_invert_key_error() -> None:
    """A test of whether the function invert correctly raises a KeyError when more than one of the same key is encountered."""
    xs = {'kris': 'jordan', 'michael': 'jordan'}
    assert invert(xs) == KeyError


def test_invert_multiple_keys() -> None:
    """A test of whether the function invert correctly inverts when there is more than one key-value pair in the dictionary."""
    xs = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(xs) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_favorite_color_tie() -> None:
    """A test of whether the function favorite_colors breaks a tie by claiming the first color to appear more than once as the favorite."""
    xs = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Kaki": "yellow"}
    assert favorite_color(xs) == "yellow"


def test_favorite_color_most_frequent() -> None:
    """A test of whether the function favorite_colors correctly identifies the color that appears most frequently in a dictionary."""
    xs = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(xs) == "blue"


def test_favorite_color_no_winner() -> None:
    """A test of whether the function favorite_colors correctly identifies when there is no color that appears most frequently."""
    xs = {"Marc": "yellow", "Ezri": "green", "Kris": "blue"}
    assert favorite_color(xs) == "no winner found"


def test_count_found() -> None:
    """A test of whether the function count increases the value associated by a key by 1 when it is found more than once."""
    xs = ["Marc", "Marc"]
    assert count(xs) == {"Marc": "2"}


def test_count_not_found() -> None:
    """A test of whether the function count keeps the value associated by a key at 1 when it is not found more than once."""
    xs = ["Ezri", "Kris"]
    assert count(xs) == {"Ezri": "1", "Kris": "1"}


def test_count_return_dictionary() -> None:
    """A test of whether the function count correctly returns a dictionary with keys relating to strings and values relating to how many times they appeared in a list."""
    xs = ["Marc", "Ezri", "Kris", "Marc"]
    assert count(xs) == {"Marc": "2", "Ezri": "1", "Kris": "1"}