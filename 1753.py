import heapq 

'''MACRO'''
INF = 0xFFFFFFFF
NO_EDGE_WEIGHT = 0
'''VARIABLES'''
#  (1≤V≤20,000, 1≤E≤300,000) 
# # of Vertex, # of Edge, Starting vertice
V, E, K = 0, 0, 0

'''UTILS'''

def print_arr(_arr, N, M):
    for i in range(N):
        for j in range(M):
            print(_arr[i][j], end=" ")
        print()

def dijkstra_sp(K, arr):

    _V = len(arr[0]) - 1
    # dist = (weight, vertex_index)
    dist = [(INF, i) for i in range(V+1)]
    
    dist[K] = (0, K)
    heap = [dist[K]]
    heapq.heapify(heap)

    while heap:
        weight, curr = heapq.heappop(heap)
        
        for _next in range(1, _V+1):
            if arr[curr][_next] == NO_EDGE_WEIGHT:
                continue
            
            # Relaxation
            _next_weight = dist[_next][0]
            
            if _next_weight > weight + arr[curr][_next]:
                dist[_next] = (weight + arr[curr][_next], _next)
                heapq.heappush(heap, dist[_next])

    return dist


'''INPUT'''

line = input().split(" ")
V, E = int(line[0]), int(line[1])
K = int(input())
arr = [[0 for _ in range(V+1)] for _ in range(V+1)]

for i in range(E):
    line = input().split(" ")
    # (u, v, w)
    u, v, w = list(map(int, line))
    arr[u][v] = w

'''COMPUTE'''

ret = dijkstra_sp(K, arr)

'''OUTPUT'''

for curr in ret[1:]:
    weight, _ = curr
    weight = weight if weight != INF else 'INF'

    print(weight)