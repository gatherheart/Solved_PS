EMPTY = 0
VERTICAL_COLUMN_SIZE = 2
VERTICAL_ROW_SIZE = 3
HORIZONTAL_COLUMN_SIZE = 3
HORIZONTAL_ROW_SIZE = 2

def print_arr(_arr, N, M):
    for i in range(N):
        for j in range(M):
            print(_arr[i][j], end=" ")
        print()

def is_empty_column(_from, _to, col, board):
    for i in range(_from, _to + 1):
        if board[i][col] != EMPTY:
            return False
        
    return True

def vertical_check(topleft, board):
    blockid = None
    block_count = 0
    empty_spaces = []
    x, y = topleft
    for i in range(VERTICAL_ROW_SIZE):
        for j in range(VERTICAL_COLUMN_SIZE):
            new_x, new_y = x + i, y + j 
            if not blockid and board[new_x][new_y] != EMPTY:
                blockid = board[new_x][new_y]
                block_count += 1
            elif blockid and board[new_x][new_y] != EMPTY and board[new_x][new_y] != blockid:
                return False
            elif blockid and board[new_x][new_y] == blockid:
                block_count += 1
            elif board[new_x][new_y] == EMPTY:
                if not is_empty_column(0, new_x - 1, new_y, board):
                    return False
           
    if not block_count == 4:
        return False
     
    for i in range(VERTICAL_ROW_SIZE):
        for j in range(VERTICAL_COLUMN_SIZE):
            new_x, new_y = x + i, y + j 
            if board[new_x][new_y] == blockid:
                board[new_x][new_y] = EMPTY
            
    return True

def horizontal_check(topleft, board):
    blockid = None
    block_count = 0
    empty_spaces = []
    x, y = topleft
    for i in range(HORIZONTAL_ROW_SIZE):
        for j in range(HORIZONTAL_COLUMN_SIZE):
            new_x, new_y = x + i, y + j 
            if not blockid and board[new_x][new_y] != EMPTY:
                blockid = board[new_x][new_y]
                block_count += 1
            elif blockid and board[new_x][new_y] != EMPTY and board[new_x][new_y] != blockid:
                return False
            elif blockid and board[new_x][new_y] == blockid:
                block_count += 1
            elif board[new_x][new_y] == EMPTY:
                if not is_empty_column(0, new_x - 1, new_y, board):
                    return False
           
    if not block_count == 4:
        return False
     
    for i in range(HORIZONTAL_ROW_SIZE):
        for j in range(HORIZONTAL_COLUMN_SIZE):
            new_x, new_y = x + i, y + j 
            if board[new_x][new_y] == blockid:
                board[new_x][new_y] = EMPTY
            
    return True


def solution(board):
    answer = 0
    M, N = len(board), len(board[0])
    start = (0, 0)    
    found = True
    for i in range(M):
        for j in range(N):
            if board[i][j] != EMPTY:
                start = (i, j)
                break
        if not start == (0, 0):
            break
    
    #print(start)
    while found:
        found = False
        for i in range(M):
            for j in range(M):
                if i + VERTICAL_ROW_SIZE <= M and \
                    j + VERTICAL_COLUMN_SIZE <= N and \
                    vertical_check((i, j), board):
                    answer += 1
                    #print("FOUND VERTICAL", (i, j))
                    found = True
                    #print_arr(board, M, N)
                    #print()
                    
                elif i + HORIZONTAL_ROW_SIZE <= M and \
                    j + HORIZONTAL_COLUMN_SIZE <= N and \
                    horizontal_check((i, j), board):
                    answer += 1
                    #print("FOUND HORIZONTAL", (i, j))
                    found = True

                    #print_arr(board, M, N)
                    #print()
    return answer

if __name__ == "__main__":

    test = 1
    
    if test == 1:
        board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0], [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]

    print(solution(board))