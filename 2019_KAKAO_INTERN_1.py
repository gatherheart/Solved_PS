
def print_arr(_arr, N, M):
    for i in range(N):
        for j in range(M):
            print(_arr[i][j], end=" ")
        print()

def solution(board, moves):
    answer = 0
    queues = [[]]
    stack = []
    M, N = len(board), len(board[0])
    for j in range(N):
        queue = []
        for i in range(M):
            if board[i][j] == 0:
                continue
            
            queue.append(board[i][j])
         
        queue.append(None)   
        queues.append(queue)
        
    for move in moves:
        current = queues[move].pop(0)
        if not current:
            queues[move].append(None)
            continue
        
        if stack and stack[-1] == current:
            stack.pop()
            answer += 2
        else:
            stack.append(current)
    
    #print(queues)
    
    return answer

if __name__ == "__main__":

    test = 1
    
    if test == 1:
        board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
        moves = [1,5,3,5,1,2,1,4]
        
    print_arr(board, len(board), len(board[0]))
    print(solution(board, moves))