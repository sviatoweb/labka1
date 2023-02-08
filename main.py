def check_column(board):
    """
    Checks whether columns are correct
    """
    for i in range(9):
        numbers = '123456789'
        for line in board:
            if line[i] != '*' and line[i] != ' ':
                index = numbers.find(line[i])
                if index == -1:
                    return False
                numbers = numbers[:index] + numbers[index + 1:]
    return True
