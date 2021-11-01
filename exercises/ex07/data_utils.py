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


def head(column_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """This function produces a new column-bsaed table with a select number of rows."""
    empty_dict: dict[str, list[str]] = {}
    i: int = 0
    for columns in column_table:
        empty_list: list[str] = []
        while i <= rows:
            empty_list.append(columns[i])
        empty_dict[columns] = empty_list
    return empty_dict


def select(column_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """This function produces a new table with a only a select number of columns."""
    empty_dict: dict[str, list[str]] = {}
    for key in empty_dict:
        empty_dict[key] = names
    return empty_dict
   

def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """This function produces a new table by combining two different tables."""
    empty_dict: dict[str, list[str]] = {}
    for column in table_1:
        empty_dict[column] = table_1[column]
    for column in table_2:
        empty_dict[column] = table_2[column]
    return empty_dict


def count(list: list[str]) -> dict[str, int]:
    """This function counts how many times a value appears in a list."""
    empty_dict: dict[str, int] = {}
    i: int = 0
    value: int = 0
    for item in empty_dict:
        item = list[i]
        if item in empty_dict:
            item = item[i]
            value += 1
        else:
            value = 1
        i += 1
    return empty_dict