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