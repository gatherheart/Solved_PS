OFFSET  = [[-1, 0], [0, 1], [1, 0], [0, -1]]
REMOVED = ""

def print_arr(_arr, N, M):
    for i in range(N):
        for j in range(M):
            if _arr[i][j] == "":
                print(" ", end=" ")
            else:
                print(_arr[i][j], end=" ")
        print()
        
        
def is_overflow(x, y, m, n):
    return x < 0 or x >= m or y < 0 or y >= n

def is_removable(curr, start_dir, m, n, board):
    x, y = curr
    new_x, new_y = curr
    shape = board[x][y]
    
    for _dir in range(start_dir, start_dir+len(OFFSET)):
        _dir = _dir % len(OFFSET)
        new_x = new_x + OFFSET[_dir][0]
        new_y = new_y + OFFSET[_dir][1]
        if is_overflow(new_x, new_y, m, n):
            return False
        
        if board[new_x][new_y] != shape:
            return False
    
    return True

def remove_block(curr, start_dir, m, n, board):
    x, y = curr
    new_x, new_y = curr
    shape = board[x][y]
    for _dir in range(start_dir, start_dir+len(OFFSET)):
        _dir = _dir % len(OFFSET)
        new_x = new_x + OFFSET[_dir][0]
        new_y = new_y + OFFSET[_dir][1]
        board[new_x][new_y] = REMOVED
        
    return True

def fill_block(m, n, board):
    for j in range(n):
        column = []
        for i in range(m):
            column.append(board[i][j])
        
        #print("".join(column))
        column = list("".join(column))
        #print(column)
        
        i = m - 1
        while column:
            board[i][j] = column.pop()
            i -= 1
        
        #print(i)
        for k in range(i, -1, -1):
            board[k][j] = REMOVED
            #print("REMOVED", board[k][j])
        
        #print_arr(board, m, n)
        #print()
    return 

def solution(m, n, board):
    answer = 0
    #print_arr(new_board, m, n)
    #print()
    while True:
        new_board = list(map(list, board))

        for i in range(m):
            for j in range(n):
                if board[i][j] == REMOVED:
                    continue
                
                if is_removable((i, j), 1, m, n, board):
                    remove_block((i, j), 1, m, n, new_board)
                    #print_arr(new_board, m, n)
                    #print()
                   
        fill_block(m, n, new_board)
        #print_arr(new_board, m, n)

        if board == new_board:
            for i in range(m):
                answer += new_board[i].count("")
            return answer

        board = new_board

if __name__ == "__main__":

    m = 6
    n = 6
    board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
    m, n = 4, 5
    board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]	
    board = ["AAAAA", "AAAAA", "AAABA", "AABAB"]	

    print(solution(m, n, board))
