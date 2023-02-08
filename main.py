"""Puzzle module"""

from typing import List

def parse_field(field: List[str]) -> List[List]:
    """
    return colored area in a list
    >>> parse_field(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
 "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    [[' ', ' ', '2', ' ', ' ', ' ', ' ', '3', ' '],\
 [' ', '8', ' ', ' ', '2', ' ', ' ', '6', ' '],\
 [' ', ' ', '1', ' ', ' ', ' ', '4', ' ', ' '],\
 [' ', '8', '3', ' ', ' ', '1', ' ', ' ', ' '],\
 [' ', '9', ' ', '5', ' ', ' ', ' ', '3', '1']]
    """
    rows = []
    columns = []
    colors = []

    for row in field:
        append_row = []
        for element in row:
            append_row.append(element)
        rows.append(append_row)

    for j in range(len(rows)):
        new_col = []
        for row in rows:
            new_col.append(row[j])
        columns.append(new_col)

    rows = rows[::-1]
    for i in range(5):
        sliced_rows = rows[i][i:i+5]
        sliced_columns = columns[i][4-i:8-i]
        color = sliced_rows+sliced_columns
        colors.append(color)
    return colors


def check_colors(colors: List[List]) -> bool:
    """
    This function checking board colored ared.
    Check: if all numbers are from 1 to 9 and all numbers appears only once.
    >>> check_colors(parse_field(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
 "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"]))
    True
    >>> check_colors(parse_field(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
 "     9 5 ", " 6  83  *", "3   1  **", "3 8  2***", "  2  ****"]))
    False
    """
    for i in colors:
        dct = {}
        for j in i:
            if j in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if j in dct:
                    return False
                dct[j] = 1
            else:
                if j not in ['*', ' ']:
                    return False
    return True


def check_rows(field: List[str]) -> bool:
    """
    This function checking board rows.
    First check: if all numbers are from 1 to 9.
    Second check: if all numbers appears only once.
    >>> check_rows(["**** ****", "***1 ****","**  3****","* 4 1****",\
    "     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"])
    True
    >>> check_rows(["**** ****", "***1 ****","**  3****","* 4 1****",\
    "     9 5 "," 6  83 3*","3   1  **","  8  2***","  2  ****"])
    False
    """
    rows = []
    num = []

    for row in field:
        append_row = []
        for element in row:
            if element != '*':
                append_row.append(element)
        rows.append(append_row)

    for _, val in enumerate(rows):
        number = len(val)
        for j in range(number):
            if val[j] != " ":
                if 1 <= int(val[j]) <= 9:
                    if  int(val[j]) not in num:
                        num.append(int(val[j]))
                    else:
                        return False
                else:
                    return False
        num = []
    return True


def check_column(board):
    for i in range(9):
        numbers = '123456789'
        for line in board:
            if line[i] != '*' and line[i] != ' ':
                index = numbers.find(line[i])
                if index == -1:
                    return False
                numbers = numbers[:index] + numbers[index + 1:]
    return True


def validate_board(board: List[str]) -> bool:
    """Checks wether board is valid"""
    return all((check_colors(parse_field(board)), check_columns(board), check_rows(board)))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
