import sys 
import heapq 

'''CONSTANTS'''
INF = sys.maxsize

'''VARIABLES'''
# (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 
N, E = 0, 0
arr = []
v1, v2 = 0, 0

'''UTILS'''

def shortest_path(start, stop, N, arr):

    heap = [(0, start)]
    cache = [INF for _ in range(N + 1)]
    cache[start] = 0

    while heap:
        weight, curr = heapq.heappop(heap)
        if curr == stop:
            break
        
        _nexts = arr[curr].keys()

        for _next in _nexts:
            if weight + arr[curr][_next] < cache[_next]:
                cache[_next] = weight + arr[curr][_next]
                heapq.heappush(heap, (arr[curr][_next] + weight, _next))

    return cache


'''INPUT'''

N, E = list(map(int, sys.stdin.readline().split()))
arr = [{} for i in range(N + 1)]

for i in range(E):
    vertex1, vertex2, weight = list(map(int, sys.stdin.readline().split()))
    arr[vertex1][vertex2] = weight
    arr[vertex2][vertex1] = weight

v1, v2 = list(map(int, sys.stdin.readline().split()))

'''COMPUTE'''

ret1 = shortest_path(1, v1, N, arr)[v1] + shortest_path(v1, v2, N, arr)[v2]\
        + shortest_path(v2, N, N, arr)[N]
ret2 = shortest_path(1, v2, N, arr)[v2] + shortest_path(v2, v1, N, arr)[v1]\
        + shortest_path(v1, N, N, arr)[N]

'''OUTPUT'''

ret = min(ret1, ret2)

if ret >= INF:
    print(-1)
else:
    print(ret)

'''
CASE 1. 
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3


1 -> 2 -> 3 -> 4 
= 3 + 3 + 1 = 7

1 -> 3 -> 2 -> 3 -> 4
= 5 + 3 + 5 = 12 


4 4
1 2 1
2 3 1
1 3 1
1 4 1
2 3


CASE 2. There is already passed path
4 3
1 2 1
2 3 1
1 4 1
2 3

1 -> 2 -> 3 -> 2 -> 1 -> 4
1 + 1 + 1 + 1 + 1 = 5

1 -> 2 -> 3 -> 2 -> 1 -> 4
1 + 1 + 1 + 1 + 1 = 5


CASE 3. different v1 -> v2, v2 -> v1
4 4
1 2 1
2 3 1
1 3 2
3 4 1
2 3

1 -> 2 -> 3 -> 4 
1 + 1 + 1 = 3

1 -> 3 -> 2 -> 3 -> 4
4

4 4
1 3 1
1 2 1
2 4 1
2 3 1
2 3

1 -> 2 -> 3 -> 2 -> 4
4

1 -> 3 -> 2 -> 4
3

CASE 4. There is no Path
4 2
1 2 1
2 4 1
2 3

1 -> 2 -> X
1 -> 3 -> X

'''