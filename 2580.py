import sys 

'''CONSTANTS'''
BLANK = 0
SUDOKU_SIZE = 9
ROW, COL, SQR = 0, 1, 2
SUDOKU_MAX_NUM = 9
SUDOKU_MIN_NUM = 1
'''VARIABLES'''
arr = []
blank_positions = []
'''UTILS'''

def print_arr(_arr, N, M):
    for i in range(N):
        for j in range(M):
            print(_arr[i][j], end=" ")
        print()

def sum(curr, arr, axis=0):
    # axis = 0 row, axis = 1 col, axis = 2 square
    _sum = 0
    x, y = curr
    if axis == ROW:
        for i in range(SUDOKU_SIZE):
            _sum += arr[x][i]
    elif axis == COL:
        for i in range(SUDOKU_SIZE):
            _sum += arr[i][y]
    elif axis == SQR:
        start_x, start_y = x // 3 * 3, y // 3 * 3
        for i in range(SUDOKU_SIZE // 3):
            for j in range(SUDOKU_SIZE // 3):
                _sum += arr[start_x + i][start_y + j]
    return _sum

def is_improper_position(curr, arr):

    x, y = curr

    for i in range(SUDOKU_SIZE):
        if y != i and arr[x][y] == arr[x][i]:
            return True
    
    for i in range(SUDOKU_SIZE):
        if x != i and arr[x][y] == arr[i][y]:
            return True
    
    start_x, start_y = x // 3 * 3, y // 3 * 3
    for i in range(SUDOKU_SIZE // 3):
        for j in range(SUDOKU_SIZE // 3):
            if x != start_x + i and y != start_y + j \
                and arr[x][y] == arr[start_x + i][start_y + j]:
                return True
    
    return False


def solve_sudoku(blank_positions, index, arr):

    if index >= len(blank_positions):
        return True

    x, y = blank_positions[index]

    for i in range(SUDOKU_MIN_NUM, SUDOKU_MAX_NUM+1):
        arr[x][y] = i
        if is_improper_position((x, y), arr) or not solve_sudoku(blank_positions, index + 1, arr):
            arr[x][y] = BLANK
        else:
            return True

    return False

'''INPUT'''

for i in range(SUDOKU_SIZE):
    arr.append(list(map(int, sys.stdin.readline().split())))
    blanks = [i for i, e in enumerate(arr[i]) if e == BLANK]
    for b in blanks:
        blank_positions.append((i, b))

'''COMPUTE'''

solve_sudoku(blank_positions, 0, arr)

'''OUTPUT'''

print_arr(arr, SUDOKU_SIZE, SUDOKU_SIZE)

'''
CASE 1. Easiest

1 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 0

CASE 2. 

0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0


'''