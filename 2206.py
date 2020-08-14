import sys 

'''MACROS'''
INF = 0xFFFFFFFF
OFFSET = [[-1, 0], [0, 1], [1, 0], [0, -1]]
PASSED = -1
BLANK = 0
WALL = 1
CHANCE_USED = 1
CHANCE_UNUSED = 0

'''VARIABLES'''
# N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)
N, M = 0, 0
arr = []
queue = []
break_count = 0
START_POSITION = (0, 0)

'''UTILS'''

def print_arr(_arr, N, M):
    for i in range(N):
        for j in range(M):
            print(_arr[i][j], end=" ")
        print()

def print_arr2(_arr, N, M, used):
    for i in range(N):
        for j in range(M):
            print(_arr[i][j][used], end=" ")
        print()

def is_overflow(x, y, N, M):
    return x < 0 or x >= N or y < 0 or y >=M 

def is_wall(x, y, arr):
    return arr[x][y] == WALL

def is_passed(x, y, visited, used):
    return visited[x][y][used] < 0

def is_blank(x, y, arr):
    return arr[x][y] == BLANK

def BFS(start, N, M, arr):
    visited = [[[0] * 2 for i in range(M)] for _ in range(N)]
    # Not yet used chance = 0 
    # Already used chance = 1
    visited[start[0]][start[1]][0] = -1
    queue.append([*start, CHANCE_UNUSED])

    while queue:
        # chance used -> false: 0, true: 1
        x, y, used = queue.pop(0)

        for dir in range(len(OFFSET)):
            new_x = x + OFFSET[dir][0]
            new_y = y + OFFSET[dir][1]

            if is_overflow(new_x, new_y, N, M) \
                or (used == CHANCE_USED and is_wall(new_x, new_y, visited)) \
                or is_passed(new_x, new_y, visited, used):
                continue
            
            if used == CHANCE_UNUSED and is_wall(new_x, new_y, arr):
                visited[new_x][new_y][CHANCE_USED] = visited[x][y][CHANCE_UNUSED] - 1
                queue.append((new_x, new_y, CHANCE_USED))
            elif is_blank(new_x, new_y, arr):
                visited[new_x][new_y][used] = visited[x][y][used] - 1
                queue.append((new_x, new_y, used))

    return visited

'''INPUT'''

N, M = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    line = list(sys.stdin.readline().strip())
    arr.append(list(map(int, line)))

'''COMPUTE'''

ret = BFS(START_POSITION, N, M, arr)

# Penalty if not reached
ret[N-1][M-1][CHANCE_UNUSED] = -INF if ret[N-1][M-1][CHANCE_UNUSED] == 0 else ret[N-1][M-1][CHANCE_UNUSED]
ret[N-1][M-1][CHANCE_USED] = -INF if ret[N-1][M-1][CHANCE_USED] == 0 else ret[N-1][M-1][CHANCE_USED]

result = -max(ret[N-1][M-1][CHANCE_UNUSED], ret[N-1][M-1][CHANCE_USED])
result = -1 if result == INF else result

'''OUTPUT'''
print(result)

'''

CASE 1. CANNOT Move -> Use break-chance

6 4
0100
1110
1000
0000
0111
0000

CASE 2. CAN MOVE, but fast

6 4
0000
1110
1000
0000
0111
0000

ANS = 9 


6 4
0000
1110
1101
0001
0111
0000
ANS = 13

6 4
0000
1110    
0000
0000
1110
0000

6 4
0100
0000
1000
0001
0111
0000

CASE 3. No Path

4 4
0111
1111
1111
1110

CASE 4. Separate passed route

8 8
01000100
01010100
01010100
01010100
01010100
01010100
01010100
00010100 

ANS = 29
'''