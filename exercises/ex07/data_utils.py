"""Utility functions."""

__author__ = "730350912"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """This function reads the CSV rows and puts them in a table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """This function takes a table and returns a list of just the column values."""
    empty: list[str] = []
    for row in table:
        key: str = row[column]
        empty.append(key)
    return empty


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """This function takes a row-oriented table and changes it to a column-oriented table."""
    empty: dict[str, list[str]] = {}
    row_1: dict[str, str] = table[0]
    for column in row_1:
        empty[column] = column_values(table, column)
    return empty
