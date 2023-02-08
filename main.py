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
