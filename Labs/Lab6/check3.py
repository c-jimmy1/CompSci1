import lab06_util

def ok_to_add(row, column, value, bd):
    for x in range(0,9):
        if value == bd[row][x]:
            return False
        
    for y in range(0,9):
        if value == bd[y][column]:
            return False

    newrow = row // 3
    newcolumn = column // 3
    
    for x in range(0,3):
        for y in range(0,3):
            if value == bd[newrow * 3 + x][newcolumn * 3 + y]:
                return False

    return True


def verify_board(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                return False

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            board[r][c] = '.'
            if not ok_to_add(r, c, val, board):
                board[r][c] = val
                return False
            board[r][c] = val

    return True


def print_board(bd):
    line = ''
    for x in range(9):
        if x % 3 == 0:
            line += '\n-------------------------'
        line += '\n'
        for y in range(9):
            if y % 3 == 0:
                line += '| '
            line += bd[x][y] + ' '
            if y == 8:
                line += '|'
    line += '\n-------------------------'
    print(line)



fname = input("Enter a file name: ")
board = lab06_util.read_sudoku(fname)

while not verify_board(board):
    print_board(board)
    

    row = int(input("Enter a row (0-8): "))
    column = int(input("Enter a column (0-8): "))
    value = input("Enter the value (1-9): ")
    
    if ok_to_add(row, column, value, board):
        board[row][column] = value
    else:
        print(f"Cannot place {value} at row {row}, column {column} (invalid move).")

print_board(board)
