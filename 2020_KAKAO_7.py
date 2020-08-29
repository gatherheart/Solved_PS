from collections import deque, defaultdict
LEFT = 0
RIGHT = 1
VISITED = 1
NOT_VISITED = 0
WALL = 1
EMPTY = 0
OFFSET = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def is_overflow(x, y, N, M):
    return x < 0 or x >= N or y < 0 or y >= M

def is_rotate_safe(pos, axis, clockwise, N, arr):

    left, right = pos
    left_x, left_y = left
    right_x, right_y = right
                
    if axis == LEFT:
        if clockwise:
            if left_x == right_x and left_y < right_y:
                new_right_x = right_x + 1
                new_right_y = right_y
            elif left_x < right_x and left_y == right_y:
                new_right_x = right_x
                new_right_y = right_y - 1
            elif left_x == right_x and left_y > right_y:
                new_right_x = right_x - 1
                new_right_y = right_y
            elif left_x > right_x and left_y == right_y:
                new_right_x = right_x
                new_right_y = right_y + 1
        else:
            if left_x == right_x and left_y < right_y:
                new_right_x = right_x - 1
                new_right_y = right_y
            elif left_x > right_x and left_y == right_y:
                new_right_x = right_x
                new_right_y = right_y - 1
            elif left_x == right_x and left_y > right_y:
                new_right_x = right_x + 1
                new_right_y = right_y
            elif left_x < right_x and left_y == right_y:
                new_right_x = right_x
                new_right_y = right_y + 1       

        return not is_overflow(new_right_x, new_right_y, N, N) and \
            arr[new_right_x][new_right_y] == EMPTY

    elif axis == RIGHT:
        if clockwise:
            if left_x == right_x and left_y < right_y:
                new_left_x = left_x - 1
                new_left_y = left_y
            elif left_x < right_x and left_y == right_y:
                new_left_x = left_x
                new_left_y = left_y + 1
            elif left_x == right_x and left_y > right_y:
                new_left_x = left_x + 1
                new_left_y = left_y
            elif left_x > right_x and left_y == right_y:
                new_left_x = left_x
                new_left_y = left_y - 1
        else:
            if left_x == right_x and left_y < right_y:
                new_left_x = left_x + 1
                new_left_y = left_y
            elif left_x > right_x and left_y == right_y:
                new_left_x = left_x
                new_left_y = left_y + 1
            elif left_x == right_x and left_y > right_y:
                new_left_x = left_x - 1
                new_left_y = left_y
            elif left_x < right_x and left_y == right_y:
                new_left_x = left_x
                new_left_y = left_y - 1
        
        return not is_overflow(new_left_x, new_left_y, N, N) and \
            arr[new_left_x][new_left_y] == EMPTY


def rotate(pos, axis, clockwise):
    left, right = pos
    left_x, left_y = left
    right_x, right_y = right
    new_left_x, new_left_y = left_x, left_y
    new_right_x, new_right_y = right_x, right_y

    if axis == LEFT:
        if clockwise:
            if left_x == right_x and left_y < right_y:
                new_right_x = right_x + 1
                new_right_y = right_y - 1
            elif left_x < right_x and left_y == right_y:
                new_right_x = right_x - 1
                new_right_y = right_y - 1
            elif left_x == right_x and left_y > right_y:
                new_right_x = right_x - 1
                new_right_y = right_y + 1
            elif left_x > right_x and left_y == right_y:
                new_right_x = right_x + 1
                new_right_y = right_y + 1
        else:
            if left_x == right_x and left_y < right_y:
                new_right_x = right_x - 1
                new_right_y = right_y - 1
            elif left_x > right_x and left_y == right_y:
                new_right_x = right_x + 1
                new_right_y = right_y - 1
            elif left_x == right_x and left_y > right_y:
                new_right_x = right_x + 1
                new_right_y = right_y + 1
            elif left_x < right_x and left_y == right_y:
                new_right_x = right_x - 1
                new_right_y = right_y + 1       

    elif axis == RIGHT:
        if clockwise:
            if left_x == right_x and left_y < right_y:
                new_left_x = left_x - 1
                new_left_y = left_y + 1
            elif left_x < right_x and left_y == right_y:
                new_left_x = left_x + 1
                new_left_y = left_y + 1
            elif left_x == right_x and left_y > right_y:
                new_left_x = left_x + 1
                new_left_y = left_y - 1
            elif left_x > right_x and left_y == right_y:
                new_left_x = left_x - 1
                new_left_y = left_y - 1
        else:
            if left_x == right_x and left_y < right_y:
                new_left_x = left_x + 1
                new_left_y = left_y + 1
            elif left_x > right_x and left_y == right_y:
                new_left_x = left_x - 1
                new_left_y = left_y + 1
            elif left_x == right_x and left_y > right_y:
                new_left_x = left_x - 1
                new_left_y = left_y - 1
            elif left_x < right_x and left_y == right_y:
                new_left_x = left_x + 1
                new_left_y = left_y - 1
    
    new_pos = ((new_left_x, new_left_y), (new_right_x, new_right_y))
    
    return new_pos

def BFS(board):
    start = (((0, 0), (0, 1)), 0)
    N = len(board)
    print(N)
    queue = deque([start])
    time = -1
    visited = defaultdict(int)
    visited[start] = VISITED

    while queue:
        pos, time = queue.popleft()
        #print(pos, time)
        left, right = pos
        left_x, left_y = left
        right_x, right_y = right

        if left_x == N - 1 and left_y == N - 1:
            return time
        elif right_x == N - 1 and right_y == N - 1:
            return time

        for _dir in range(len(OFFSET)):
            new_left_x = left_x + OFFSET[_dir][0]
            new_left_y = left_y + OFFSET[_dir][1]
            new_right_x = right_x + OFFSET[_dir][0]
            new_right_y = right_y + OFFSET[_dir][1]
            new_pos = ((new_left_x, new_left_y), (new_right_x, new_right_y))
            new_left, new_right = new_pos
            
            if is_overflow(*new_left, N, N) or \
                is_overflow(*new_right, N, N) or \
                board[new_left[0]][new_left[1]] == WALL or \
                board[new_right[0]][new_right[1]] == WALL:
                    continue

            if not visited[new_pos]:
                queue.append((new_pos, time + 1))
                visited[new_pos] = VISITED
        
        for axis in range(2):
            for clockwise in range(2):
                if is_rotate_safe(pos, axis, clockwise==0, N, board):
                    new_pos = rotate(pos, axis, clockwise==0)
                    new_left, new_right = new_pos
                    #print(new_pos)
                    #print("ratate", axis, clockwise==0, new_left, new_right)

                    if is_overflow(*new_left, N, N) or \
                        is_overflow(*new_right, N, N) or \
                        board[new_left[0]][new_left[1]] == WALL or \
                        board[new_right[0]][new_right[1]] == WALL:
                        continue
                    
                    if not visited[new_pos]:
                        #print("Rotate", new_pos)
                        queue.append((new_pos, time + 1))
                        visited[new_pos] = VISITED

    return -1

def DFS(pos, time, N, visited, board):

    #print(pos, time)
    _time = 0xFFFF
    left, right = pos
    left_x, left_y = left
    right_x, right_y = right

    if left_x == N - 1 and left_y == N - 1:
        return time
    elif right_x == N - 1 and right_y == N - 1:
        return time

    for _dir in range(len(OFFSET)):
        new_left_x = left_x + OFFSET[_dir][0]
        new_left_y = left_y + OFFSET[_dir][1]
        new_right_x = right_x + OFFSET[_dir][0]
        new_right_y = right_y + OFFSET[_dir][1]
        new_pos = ((new_left_x, new_left_y), (new_right_x, new_right_y))
        new_left, new_right = new_pos
        
        if is_overflow(*new_left, N, N) or \
            is_overflow(*new_right, N, N) or \
            board[new_left[0]][new_left[1]] == WALL or \
            board[new_right[0]][new_right[1]] == WALL:
                continue

        if not visited[new_pos]:
            visited[new_pos] = VISITED
            _time = min(_time, DFS(new_pos, time + 1, N, visited, board))
            visited[new_pos] = NOT_VISITED

    for axis in range(2):
        for clockwise in range(2):
            if is_rotate_safe(pos, axis, clockwise==0, N, board):
                new_pos = rotate(pos, axis, clockwise==0)
                new_left, new_right = new_pos

                if is_overflow(*new_left, N, N) or \
                    is_overflow(*new_right, N, N) or \
                    board[new_left[0]][new_left[1]] == WALL or \
                    board[new_right[0]][new_right[1]] == WALL:
                    continue
                
                if not visited[new_pos]:
                    visited[new_pos] = VISITED
                    _time = min(_time, DFS(new_pos, time + 1, N, visited, board))
                    visited[new_pos] = NOT_VISITED

    return _time

def solution(board):
    answer = solution_dfs(board)
    return answer


def solution_dfs(board):
    visited = defaultdict(int)
    start = ((0, 0), (0, 1))
    visited[start] = VISITED
    N = len(board)

    return DFS(start, 0, N, visited, board)


if __name__ == "__main__":
    board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]	
    print(solution(board))