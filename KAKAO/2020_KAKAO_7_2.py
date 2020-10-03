from collections import deque, defaultdict

OFFSET = [[-1, 0], [0, 1], [1, 0], [0, -1]]
ROTATE = [1, -1]
EMPTY = 0
WALL = 1
UNVISITED = 0

def is_overflow(x, y, M, N):
    return x < 0 or x >= M or y < 0 or y >= M

tuple_sorted = lambda x : tuple(sorted(x))

class Current:
    def __init__(self, is_horizontal=True, position=((1, 1), (1, 2)), distance=0):
        super().__init__()
        self.is_horizontal = is_horizontal
        self.position = position
        self.distance = distance

def solution(board):
    answer = -1
    M, N = len(board), len(board[0])
    queue = deque([Current()])
    visited = defaultdict(bool)
    
    new_board = [[WALL for j in range(N + 2)] for i in range(M + 2)]
    
    for i in range(1, M+1):
        new_board[i][1:N+1] = board[i-1]

    for i in range(M+2):
        for j in range(N+2):
            print("{:3}".format(new_board[i][j]), end=" ")

        print()
    
    print()
    board = new_board

    while queue:
        current = queue.popleft()
        left, right = current.position

        if visited[(left, right)]:
            continue

        visited[(left, right)] = True
        
        #print(left, right)
        #print()
        #print("CURRENT", current, current.position, current.distance)

        if (left[0] == M and left[1] == N) or \
            (right[0] == M and right[1] == N):
            return current.distance

        for _dir in range(len(OFFSET)):
            
            new_left_x, new_left_y = \
                left[0] + OFFSET[_dir][0], left[1] + OFFSET[_dir][1]
            new_right_x, new_right_y = \
                right[0] + OFFSET[_dir][0], right[1] + OFFSET[_dir][1]
            
            if board[new_left_x][new_left_y] == WALL or \
                board[new_right_x][new_right_y] == WALL:
                continue
        
                #print("NEW", (new_left_x, new_left_y), (new_right_x, new_right_y))

            queue.append(Current(is_horizontal=current.is_horizontal,
                position=tuple_sorted(((new_left_x, new_left_y), (new_right_x, new_right_y))),
                distance=current.distance+1))
            
        #print(current, current.position)
        

        if current.is_horizontal:
            
            for r in ROTATE:
                
                if board[left[0]+r][left[1]] == EMPTY and board[right[0]+r][right[1]] == EMPTY:
                    
                    queue.append(Current(is_horizontal=False,
                        position=tuple_sorted(((left[0]+r, left[1]), (left[0], left[1]))),
                        distance=current.distance+1))
                    queue.append(Current(is_horizontal=False,
                        position=(tuple_sorted(((right[0], right[1]), (right[0]+r, right[1])))),
                        distance=current.distance+1))
                        
        else:
            for r in ROTATE:
                
                if board[left[0]][left[1]+r] == EMPTY and board[right[0]][right[1]+r] == EMPTY:
                    queue.append(Current(is_horizontal=True,
                        position=tuple_sorted(((left[0], left[1]), (left[0], left[1]+r))),
                        distance=current.distance+1))
                    queue.append(Current(is_horizontal=True,
                        position=(tuple_sorted(((right[0], right[1]+r), (right[0], right[1])))),
                        distance=current.distance+1))
                    
                    
    
              
    return answer


if __name__ == "__main__":
    
    board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
    print(solution(board))