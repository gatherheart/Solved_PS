from enum import Enum
EMPTY = 0
CASE_A = 'A'
CASE_B = 'B'
CASE_C = 'C'
CASE_D = 'D'
CASE_E = 'E'

def column_check(x, y, board):
    for i in range(0, x+1):
        if not board[i][y] == EMPTY:
            return False
    return True

def which_case(x, y, board):
    
    block_id = board[x][y]

    if block_id == EMPTY:
        return '', [], []
    
    if block_id == board[x+1][y] == board[x+1][y+1] == board[x+1][y+2]:
        return CASE_A, [(x, y+1), (x, y+2)], [(x, y), (x+1, y), (x+1, y+1), (x+1, y+2)]
    elif y >= 1 and block_id == board[x+1][y] == board[x+2][y] == board[x+2][y-1]:
        return CASE_B, [(x+1, y-1)], [(x, y), (x+1, y), (x+2, y), (x+2, y-1)]
    elif block_id == board[x+1][y] == board[x+2][y] == board[x+2][y+1]:
        return CASE_C, [(x+1, y+1)], [(x, y), (x+1, y), (x+2, y), (x+2, y+1)]
    elif y >= 2 and block_id == board[x+1][y] == board[x+1][y-1] == board[x+1][y-2]:
        return CASE_D, [(x, y-1), (x, y-2)], [(x, y), (x+1, y), (x+1, y-1), (x+1, y-2)]
    elif y >= 1 and block_id == board[x+1][y] == board[x+1][y-1] == board[x+1][y+1]:
        return CASE_E, [(x, y-1), (x, y+1)], [(x, y), (x+1, y), (x+1, y-1), (x+1, y+1)]
    
    return '', [], []

def solution(board):
    answer = 0
    found = True
    M, N = len(board), len(board[0])
    padded_board = [[0 for j in range(N + 2)] for i in range(M + 2)]
    for i in range(M):
        padded_board[i][:-2] = board[i]
    
    while found:
        found = False
        for i in range(M):
            for j in range(N):
                case, checks, removals = which_case(i, j, padded_board)
                if case:
                    impossible = False
                    for check in checks:
                        if not column_check(*check, padded_board):
                            impossible = True
                    if not impossible:
                        answer += 1
                        found = True
                        for removal in removals:
                            x, y = removal
                            padded_board[x][y] = EMPTY
                    
    return answer

if __name__ == "__main__":

    test = 1
    
    if test == 1:
        board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0], [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]

    print(solution(board))