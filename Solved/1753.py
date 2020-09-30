import heapq 
import sys 

'''MACRO'''
INF = 0xFFFFFFFF
NO_EDGE_WEIGHT = 0
HASH_MAX_SIZE = 300000

'''VARIABLES'''
#  (1≤V≤20,000, 1≤E≤300,000) 
# 4 Bytes * 20000 * 20000 = 1,600,000,000 Bytes = 1600 MB - Full Vertex Array Size
# 4 Bytes * 300,000 = 1,200,000 = 1.2 MB  - Edge Array Size
# # of Vertex, # of Edge, Starting vertice
V, E, K = 0, 0, 0

'''UTILS'''

def print_arr(_arr, N, M):
    for i in range(N):
        for j in range(M):
            print(_arr[i][j], end=" ")
        print()

def dijkstra_sp(K, arr):

    _V = len(arr) - 1
    # dist = (weight, vertex_index)
    dist = [(INF, i) for i in range(_V+1)]
    
    dist[K] = (0, K)
    heap = [dist[K]]
    heapq.heapify(heap)

    while heap:
        weight, curr = heapq.heappop(heap)
        
        for _next in arr[curr].keys():
            
            # Relaxation
            _next_weight = dist[_next][0]
            
            if _next_weight > weight + arr[curr][_next]:
                dist[_next] = (weight + arr[curr][_next], _next)
                heapq.heappush(heap, dist[_next])

    return dist


'''INPUT'''

line = sys.stdin.readline().split(" ")
V, E = int(line[0]), int(line[1])
K = int(sys.stdin.readline())
arr = [{} for _ in range(V+1)]

for i in range(E):
    line = sys.stdin.readline().split(" ")
    # (u, v, w)
    u, v, w = list(map(int, line))
    arr[u][v] = w if v not in arr[u] or w < arr[u][v] else arr[u][v]

'''COMPUTE'''

ret = dijkstra_sp(K, arr)

'''OUTPUT'''

for curr in ret[1:]:
    weight, _ = curr
    weight = weight if weight != INF else 'INF'

    print(weight)