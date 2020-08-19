import sys 

'''CONSTANTS'''

LEFTMOST = 0
MIDDLE = 1
RIGHTMOST = 2
MAX_CACHE_VALUE = sys.maxsize
MIN_CACHE_VALUE = -MAX_CACHE_VALUE

'''VARIABLES'''
# N(1 ≤ N ≤ 100,000)
N, M = 0, 3
min_score, max_score = 0, 0
arr = []
cache = []

'''UTILS'''

def print_arr(_arr, N, M):
    for i in range(N):
        for j in range(M):
            print(_arr[i][j], end=" ")
        print()

def BFS(start, N, M, cache, arr):
    
    # Initialize Cache at the start position
    cache[start[0]][start[1]][0] = arr[start[0]][start[1]]
    cache[start[0]][start[1]][1] = arr[start[0]][start[1]]

    queue = [start]

    while queue:

        x, y = queue.pop(0)
        if x == N - 1:
            continue

        possible_new_y = [y]

        if y == LEFTMOST:    
            possible_new_y.append(y+1)
        elif y == MIDDLE:
            possible_new_y.append(y-1)
            possible_new_y.append(y+1)
        elif y == RIGHTMOST:
            possible_new_y.append(y-1)

        for new_y in possible_new_y:
            # Update Min at new position
            cache[x+1][new_y][0] = min(cache[x+1][new_y][0], cache[x][y][0] + arr[x+1][new_y])
            cache[x+1][new_y][1] = max(cache[x+1][new_y][1], cache[x][y][1] + arr[x+1][new_y])
            queue.append((x+1, new_y))

    return

'''INPUT'''
N = int(sys.stdin.readline())

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

# (Min, Max)
cache = [[[MAX_CACHE_VALUE, MIN_CACHE_VALUE] for j in range(M)] for i in range(N)]

'''COMPUTE'''

for i in range(M):
    BFS((0, i), N, M, cache, arr)

min_score = cache[-1][0][0]
max_score = cache[-1][0][1]


for score in cache[-1]:
    if min_score > score[0]:
        min_score = score[0]
    
    if max_score < score[1]:
        max_score = score[1]


'''OUTPUT'''

print(max_score, min_score)

'''
CASE 1.

3
1 2 3
4 5 6
4 9 0

CASE 2.

5
1 2 3
4 5 6
4 9 0
1 2 3
4 5 6

'''