import sys 
import math 
from collections import defaultdict

'''CONSTANTS'''
# 0: x좌표가 증가하는 방향 (→)
# 1: y좌표가 감소하는 방향 (↑)
# 2: x좌표가 감소하는 방향 (←)
# 3: y좌표가 증가하는 방향 (↓)

OFFSET = [[1, 0], [0, -1], [-1, 0], [0, 1]]
MAX = 100

'''VARIABLES'''
#  N (1 ≤ N ≤ 20)

N = 0
dragons = []
cache = {}
arr = [[False for j in range(MAX+1)] for i in range(MAX+1)]
positions = set([])
dr=[[0]]
for _ in range(10):
    dr.append(dr[-1]+[i+1 for i in dr[-1][::-1]])

'''UTILS'''
'''
0 -> 0 
1 -> 0 1
2 -> 0 1 2 1
3 -> 0 1 2 1 2 3 2 1
4 -> 0 1 2 1 2 3 2 1 2 3 0 3 2 3 2 1

'''

def print_arr(_arr, N, M):
    for i in range(N):
        for j in range(M):
            print(_arr[i][j], end=" ")
        print()

def is_overflow(x, y, N, M):
    return x < 0 or x >= N or y < 0 or y >= M

def get_directions(gen):
    
    max_key = max(cache.keys())
    start_cache = gen if gen < max_key else max_key
    _dirs = cache[start_cache]

    for g in range(start_cache + 1, gen + 1):
        _new_dirs = list(map(lambda x: (x + 1), _dirs))
        _dirs = _dirs + _new_dirs[::-1]
        cache[g] = _dirs

    return _dirs


def get_positions(start, first_dir, gen):
    x, y = start
    new_positions = [start]
    _dirs = get_directions(gen)

    for _dir in _dirs:
        x, y = new_positions[-1]
        new_x = x + OFFSET[(first_dir + _dir) % 4][0]
        new_y = y + OFFSET[(first_dir + _dir) % 4][1]

        new_positions.append((new_x, new_y))

    return new_positions


def count_squares(N, M, arr):
    
    count = 0

    def is_square(x, y, arr):
        return arr[x][y] & arr[x + 1][y] & arr[x][y + 1] & arr[x + 1][y + 1]

    for i in range(N):
        for j in range(M):
            if is_square(i, j, arr):
                count += 1
        
    return count

'''INPUT''' 

N = int(sys.stdin.readline())

for i in range(N):
    x, y, d, g = list(map(int, sys.stdin.readline().split()))
    dragons.append((x, y, d, g))

'''COMPUTE'''

cache[0] = [0]

for dragon in dragons:
    x, y, d, g = dragon
    _positions = get_positions((x, y), d, g)

    for position in _positions:
        arr[position[0]][position[1]] = True
        positions.add(position)

positions = list(positions)

'''OUTPUT'''

print(count_squares(MAX, MAX, arr))

'''
CASE 1. Normal

4
50 50 0 10
50 50 1 10
50 50 2 10
50 50 3 10

2
70 70 3 10
10 10 2 5

2
10 50 0 10
0 0 2 10

4
70 70 3 10
10 10 2 5
10 50 0 10
0 0 2 10

4
70 70 3 5
10 10 2 5
10 50 0 5
0 0 2 5


CASE 2. Negative Value

3
0 0 0 1
0 0 0 2
0 0 0 3

CASE 3. Overflow

2
100 100 0 3
0 0 2 3

2
100 100 0 10
0 0 2 10

4
100 100 0 10
0 0 2 10
0 100 3 10
100 0 0 10 


'''