board = [
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   1  **",
 "  8  2***",
 "  2  ****"
]

def check_rows(field):
    """
    This function checking board rows.
    First check: if all numbers are from 1 to 9.
    Second check: if all numbers appears only once.
    """
    rows = []
    num = []

    for row in field:
        append_row = []
        for el in row:
            if el != '*':
                append_row.append(el)
        rows.append(append_row)

    for _, val in enumerate(rows):
        for j in range(len(val)):
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
