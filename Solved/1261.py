import sys 
import heapq 

'''CONSTANTS'''

BLANK = 0
WALL = 1
OFFSET = [[-1, 0], [0, 1], [1, 0], [0, -1]]
START_POSITION = (0, 0)
INF = sys.maxsize
CACHE_DEFAULT_VALUE = INF

'''VARIABLES'''
# 가로 크기 M, 세로 크기 N (1 ≤ N, M ≤ 100)
N, M = 0, 0
arr = []

'''UTILS'''

def print_arr(N, M, arr):
    for i in range(N):
        for j in range(M):
            print("{:3}".format(arr[i][j] if arr[i][j] != INF else "INF"), end=" ")
        print()


def is_overflow(x, y, N, M):
    return x < 0 or x >= N or y < 0 or y >= M

def is_wall(x, y, arr):
    return arr[x][y] == WALL

def BFS(start, N, M, arr):
    heap = [(0, start)]
    cache = [[CACHE_DEFAULT_VALUE]*M for i in range(N)]
    ret = INF

    while heap:
        broken_wall, curr = heapq.heappop(heap)
        x, y = curr
        
        # if the position is end point
        if x == N - 1 and y == M - 1:
            return min(cache[N-1][M-1], broken_wall)

        for _dir in range(len(OFFSET)):
            new_x = x + OFFSET[_dir][0]
            new_y = y + OFFSET[_dir][1]

            if is_overflow(new_x, new_y, N, M):
                continue

            if is_wall(new_x, new_y, arr) and broken_wall + 1 < cache[new_x][new_y]:
                cache[new_x][new_y] = broken_wall + 1
                heapq.heappush(heap, (broken_wall + 1, (new_x, new_y)))

            elif not is_wall(new_x, new_y, arr) and broken_wall < cache[new_x][new_y]:
                cache[new_x][new_y] = broken_wall
                heapq.heappush(heap, (broken_wall, (new_x, new_y)))

                
    return cache

'''INPUT'''

N, M = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    arr.append(list(map(int, list(sys.stdin.readline().strip()))))

'''COMPUTE'''

result = BFS(START_POSITION, M, N, arr)

'''OUTPUT'''

print(result)

'''
CASE 1.
3 3
011
111
110

-> 3

CASE 2.

4 2
0001
1000

6 4
000000
000000
000000
000000

-> 0

6 4
000000
000000
000001
000010

6 4
011111
111110
110111
111010

CASE 3.

6 6
001111
010000
001111
110001
011010
100010

-> 2


0 0 1 1 1 1
0 1 0 0 0 0
0 0 1 1 1 1
1 1 0 0 0 1
0 1 1 0 1 0
1 0 0 0 1 0


6 6
001111
010011
011111
111001
111010
111010

CASE 4.

4 4
0111
1111
1110

'''