import sys 
from collections import deque
import math
'''CONSTANTS'''

OFFSET = [[1, 0], [0, -1], [-1, 0], [0, 1]]

TILT_UP = 1
TILT_DOWN = -1
TILT_RIGHT = -1
TILT_LEFT = 1

TILTS = [TILT_UP, TILT_RIGHT, TILT_DOWN, TILT_LEFT]

EMPTY = 0
MAX_DEPTH = 5

'''VARIABLES'''
N = 0
board = []

'''UTILS'''

def print_arr(arr, N, M):
    for i in range(N):
        for j in range(M):
            print("{:3}".format(arr[i][j]), end=" ")
        print()
        

def is_overflow(x, y, N, M):
    return x < 0 or x >= N or y < 0 or y >= M

# direction -> tilt right = -1, tilt left = 1 
def tilt_horizontal(direction, N, board):
    new_board = [board[i][:] for i in range(N)]
    board = new_board
    start, end = 1, N
    new_max = 0
    
    if direction == TILT_RIGHT:
        start = N - 2
        end = -1
    
    initial_col = start - direction
    
    for row in range(N):
        prev_block_position = (row, initial_col)
        prev_block = (board[row][initial_col], prev_block_position)
        
        for col in range(start, end, direction):
            prev_block_val, prev_pos = prev_block
            
            if prev_block_val == EMPTY:
                board[prev_pos[0]][prev_pos[1]] = board[row][col]
                board[row][col] = EMPTY
                prev_block = (board[prev_pos[0]][prev_pos[1]], prev_pos)
            
            elif board[row][col] == prev_block_val:
                board[prev_pos[0]][prev_pos[1]] *= 2
                board[row][col] = EMPTY
                prev_block = (board[prev_pos[0]][prev_pos[1]+direction], 
                              (prev_pos[0], prev_pos[1]+direction))
    
            elif board[row][col] != EMPTY:
                board[row][col], board[prev_pos[0]][prev_pos[1]+direction] = \
                    EMPTY, board[row][col]
                prev_block = (board[prev_pos[0]][prev_pos[1]+direction], 
                    (prev_pos[0], prev_pos[1]+direction))
    
            if new_max < board[prev_pos[0]][prev_pos[1]]:
                new_max = board[prev_pos[0]][prev_pos[1]]
    
            if new_max < board[prev_pos[0]][prev_pos[1]+direction]:
                new_max = board[prev_pos[0]][prev_pos[1]+direction]
    
    return new_max, board

# direction -> tilt down = -1, tilt up = 1 
def tilt_vertical(direction, N, board):
    new_board = [board[i][:] for i in range(N)]
    board = new_board
    start, end = 1, N
    new_max = 0
    if direction == TILT_DOWN:
        start = N - 2
        end = -1
    
    initial_row = start - direction
    
    for col in range(N):
        prev_block_position = (initial_row, col)
        prev_block = (board[initial_row][col], prev_block_position)
        
        for row in range(start, end, direction):
            prev_block_val, prev_pos = prev_block
            
            if prev_block_val == EMPTY:
                board[prev_pos[0]][prev_pos[1]] = board[row][col]
                board[row][col] = EMPTY
                prev_block = (board[prev_pos[0]][prev_pos[1]], prev_pos)
            
            elif board[row][col] == prev_block_val:
                board[prev_pos[0]][prev_pos[1]] *= 2
                board[row][col] = EMPTY
                prev_block = (board[prev_pos[0]+direction][prev_pos[1]], 
                              (prev_pos[0]+direction, prev_pos[1]))
    
            elif board[row][col] != EMPTY:
                board[row][col], board[prev_pos[0]+direction][prev_pos[1]] = \
                    EMPTY, board[row][col]
                prev_block = (board[prev_pos[0]+direction][prev_pos[1]], 
                    (prev_pos[0]+direction, prev_pos[1]))

            if new_max < board[prev_pos[0]][prev_pos[1]]:
                new_max = board[prev_pos[0]][prev_pos[1]]
                
            if new_max < board[prev_pos[0]+direction][prev_pos[1]]:
                new_max = board[prev_pos[0]+direction][prev_pos[1]]

    return new_max, new_board

def backtracking(depth, N, board, MAX_DEPTH=5):
    answer = board[0][0]
    if depth == MAX_DEPTH:
        return answer
    
    for _dir in range(4):
        if _dir % 2:
            new_max, new_board = tilt_vertical(TILTS[_dir], N, board)
            answer = max(answer, new_max, backtracking(depth+1, N, new_board, MAX_DEPTH))
        else:
            new_max, new_board = tilt_horizontal(TILTS[_dir], N, board)        
            answer = max(answer, new_max, backtracking(depth+1, N, new_board, MAX_DEPTH))

    return answer

'''INPUT'''

N = int(sys.stdin.readline())

for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    board.append(line)
    
'''COMPUTE'''

print(backtracking(0, N, board, MAX_DEPTH))

'''OUTPUT'''


'''
CASE 
3
2 2 2
4 4 4
8 8 8

3
2 2 2
2 2 2
8 8 8

3
1 1 1
1 1 1
1 1 1

3
0 0 0
1 1 1
1 1 1

3
1 1 1
1 1 1
0 0 0

4
1 0 0 4
1 0 0 0
1 0 0 0
1 0 0 2

4
2 2 2 32
0 2 2 0
0 2 2 2
32 2 2 2


8
8 0 1 0 0 1 1 1
4 1 0 1 0 1 1 1
2 0 0 1 0 1 1 1
1 1 1 0 0 1 1 1
1 0 0 0 0 1 1 1 
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1


16
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
'''