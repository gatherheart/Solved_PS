import sys 

'''CONSTANTS'''

WATER = 0
OFFSET = [[-1, 0], [0, 1], [1, 0], [0, -1]]
NO_ICE = None

'''VARIABLES'''
# N과 M은 3 이상 300 이하
N, M = 0, 0
arr = []
start = None
year = 0

'''UTILS'''

def is_overflow(x, y, N, M):
    return x < 0 or x >= N or y < 0 or y >= M

def get_ice_position(N, M, arr):

    for i in range(N):
        for j in range(M):
            if arr[i][j] != WATER:
                return (i, j)

    return None

def get_num_of_water(x, y, arr):
    
    count = 0

    for _dir in range(len(OFFSET)):
        new_x = x + OFFSET[_dir][0]
        new_y = y + OFFSET[_dir][1]
        
        if is_overflow(new_x, new_y, N, M):
            continue
        
        if arr[new_x][new_y] == WATER:
            count += 1

    return count

def melt_ice(N, M, arr):
    
    start = get_ice_position(N, M, arr)
    original_arr = [row[:] for row in arr]
    visited = [[False for j in range(M)] for i in range(N)]

    if start == NO_ICE:
        return 0

    stack = [start]
    count = 0

    while stack:
        x, y = stack.pop()
        if visited[x][y]:
            continue
        
        visited[x][y] = True

        num_of_water = get_num_of_water(x, y, original_arr)
        arr[x][y] = max(arr[x][y] - num_of_water, 0)

        if arr[x][y] != WATER:
            count += 1

        for _dir in range(len(OFFSET)):
            new_x = x + OFFSET[_dir][0]
            new_y = y + OFFSET[_dir][1]

            if is_overflow(new_x, new_y, N, M) \
                or arr[new_x][new_y] == WATER \
                or visited[new_x][new_y]:
                continue

            stack.append((new_x, new_y))

    return count

def is_divided(start, num_of_ice, N, M, arr):

    stack = [start]
    count = 0
    visited = [[False for j in range(M)] for i in range(N)]

    while stack:
        x, y = stack.pop()

        if visited[x][y]:
            continue

        visited[x][y] = True
        count += 1

        for _dir in range(len(OFFSET)):
            new_x = x + OFFSET[_dir][0]
            new_y = y + OFFSET[_dir][1]

            if is_overflow(new_x, new_y, N, M) \
                or arr[new_x][new_y] == WATER \
                or visited[new_x][new_y]:
                continue

            stack.append((new_x, new_y))

    return count != num_of_ice


'''INPUT'''

N, M = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    arr.append(line)

'''COMPUTE'''

while True:

    num_of_ice = melt_ice(N, M, arr)
    new_start = get_ice_position(N, M, arr)

    if num_of_ice == 0 or new_start == NO_ICE:
        year = 0
        break

    year += 1

    if is_divided(new_start, num_of_ice, N, M, arr):
        break

'''OUTPUT'''

print(year)

'''

CASE 1. Normal Case - divided

5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0

5 7
0 0 0 0 0 0 0
0 6 4 5 3 0 0
0 6 0 2 6 2 0
0 6 6 2 4 0 0
0 0 0 0 0 0 0

5 7
0 0 0 0 0 0 0
0 4 2 4 1 0 0
0 4 0 1 6 0 0
0 4 5 1 2 0 0
0 0 0 0 0 0 0

5 7
0 0 0 0 0 0 0
0 2 0 4 1 0 0
0 2 0 2 6 0 0
0 2 3 0 2 0 0
0 0 0 0 0 0 0


CASE 2. Not Divided

4 4
0 0 0 0
0 1 1 0
0 1 1 0
0 0 0 0

CASE 3. Already Divided

4 4
0 0 0 0
0 1 0 0
0 0 1 0
0 0 0 0


'''