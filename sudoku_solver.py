"""Sudoku puzzle solver using back-tracking """

board = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 3, 6, 0, 0, 0, 0, 0],
         [0, 7, 0, 0, 9, 0, 2, 0, 0],
         [0, 5, 0, 0, 0, 7, 0, 0, 0],
         [0, 0, 0, 0, 4, 5, 7, 0, 0],
         [0, 0 ,0 ,1 ,0 ,0 ,0 ,3 ,0],
         [0, 0, 1, 0, 0, 0, 0, 6, 8],
         [0, 0, 8, 5, 0, 0, 0, 1, 0],
         [0, 9, 0, 0, 0, 0, 4, 0, 0]]

def print_board(brd):
    for i, row in enumerate(brd):
        if i % 3 == 0 and i != 0:
            print('_ _ _ _ _ _ _ _ _ _ _ ')

        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                print('| ', end = '')
            if j == 8:
                print(f'{val}')
            else:
                print(f'{val} ', end = '')


def get_empty_pos(brd):
    for i, row in enumerate(brd):
        for j, val in enumerate(row):
            if val == 0:
                return i, j
    return False

def valid(val, pos, brd):
    i, j = pos
    # check row
    for num in brd[i]:
        if num == val:
            return False
    # check col
    for row in brd:
        if row[j] == val:
            return False
    # check box
    box_r, box_c = i // 3, j // 3
    for a in range(3):
        for b in range(3):
            if board[a+(box_r*3)][b+(box_c*3)] == val:
                return False
    return True

def solve(brd):
    if get_empty_pos(brd):  # if board is not solved
        i, j = get_empty_pos(brd)  # get empty position

        for num in range(0,10): # try numbers 1-9
            if valid(num, (i,j), brd):  # try if number is valid else continue
                brd[i][j] = num

                if solve(brd): #is board solved?
                    print_board(brd)
                    exit()
                else: # try next number
                    continue

        brd[i][j] = 0
        return False  # only return False if there is no numbers are valid
    return True  # this initiates the return up the call stack

solve(board)
























