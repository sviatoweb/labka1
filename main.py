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


def parse_field(field):
    rows = []
    columns = []
    colors = []

    for row in field:
        append_row = []
        for el in row:
            if el != '*':
                append_row.append(el)
        rows.append(append_row)
    
    return rows
            


print(parse_field(board))