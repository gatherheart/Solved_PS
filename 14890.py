import sys

'''CONSTANTS'''
STAIR = 1
FLOOR = 0

'''VARIABLES'''
N, L = 0, 0
count = 0
board = []
board_list = []

'''UTILS'''

def print_arr(arr, M, N):
    
    for i in range(M):
        for j in range(N):
            print("{:3}".format(arr[i][j]), end=" ")
        print()
        
def rotate_90_right(M, N, board):
    new_board = [[0 for j in range(N)] for i in range(M)]
    for i in range(M):
        for j in range(N):
            new_board[j][N-i-1] = board[i][j]
    
    return new_board 


def check_horizontal(N, L, board):
    stack = [(board[1], FLOOR)]
    i = 2
    while i < N+1:
        
        top, _type = stack[-1]
        #print(top, _type, board[i], stack)
        # Higher than right before
        if top < board[i] and board[i] - top == 1:
            count = 0
            while stack:
                prev, prev_type = stack.pop()
                
                if top == prev and prev_type == FLOOR:
                    count += 1
                    if count >= L:
                        stack.clear()
                        stack.append((board[i], FLOOR))
                        i += 1
                        break
                else:
                    #print("Higher than right before")
                    return False
            
            if count < L:
                return False
            
        # Lower than right before
        elif top > board[i] and top - board[i] == 1:
            for j in range(i, i+L):
                if not board[i] == board[j]:
                    #print("Lower than right before")
                    return False
                
            stack.clear()
            stack.append((board[j], STAIR))
            i = j + 1
        
        # Same with before
        elif top == board[i]:
            stack.append((board[i], FLOOR))
            i += 1
        
        else:
            #print("Diff >= D")
            return False
        
    return True

'''INPUT'''

N, L = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
    
new_board = [[0 for j in range(N+2)] for i in range(N+2)]

for i in range(N):
    new_board[i+1][1:N+1] = board[i]

board = new_board
rotated_board = rotate_90_right(N+2, N+2, board)

for line in board[1:N+1]:
    board_list.append(line)
    
for line in rotated_board[1:N+1]:
    board_list.append(line)

for line in board_list:
    if check_horizontal(N, L, line):
        count += 1

print(count)

'''COMPUTE'''


'''OUTPUT'''


'''
CASE 1 Normal

6 2
3 3 3 3 3 3
2 3 3 3 3 3
2 2 2 3 2 3
1 1 1 2 2 2
1 1 1 3 3 1
1 1 2 3 3 2

6 2
3 3 2 2 3 3
2 3 3 3 3 3
2 2 2 3 2 3
1 1 1 2 2 2
1 1 1 3 3 1
1 1 2 3 3 2

6 2
3 2 1 1 2 3
3 2 2 1 2 3
3 2 2 2 3 3
3 3 3 3 3 3
3 3 3 3 2 2
3 3 3 3 2 2

CASE 2

'''