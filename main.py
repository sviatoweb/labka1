board = [
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     95  ",
 " 6  83  *",
 "3   1  **",
 "  8  2***",
 "  22 ****"
]


def parse_field(field):
    """return colored area in a list"""
    rows = []
    columns = []
    colors = []

    for row in field:
        append_row = []
        for el in row:
            append_row.append(el)
        rows.append(append_row)

    for j in range(len(rows)):
        new_col = []
        for row in rows:
            new_col.append(row[j])
        columns.append(new_col)

    rows_ = rows[::-1]
    for i in range(5):
        r_ = rows_[i][i:i+5]
        c_ = columns[i][4-i:9-i]
        color = r_+c_
        colors.append(color)
    return colors


def check_if_false(colors):
    """This function checking board colored ared.
    Check: if all numbers are from 1 to 9 and all numbers appears only once."""
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

