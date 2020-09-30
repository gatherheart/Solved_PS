import sys
import heapq

'''CONSTANTS'''

INF = sys.maxsize
NO_PATH = 0

'''VARIABLES'''

# (1¡ÂV¡Â20,000, 1¡ÂE¡Â300,000)
V, E = 0, 0
start = 0
graph = []

'''UTILS'''

def dijkstra(start, vertices, graph):

    cost = [INF for _ in range(len(graph))]
    cost[start] = 0
    heap = [(cost[start], start)]
    heapq.heapify(heap)

    while heap:
        curr_weight, curr = heapq.heappop(heap)
        
        for _next in graph[curr]:
            _weight = graph[curr][_next]
            if _weight == NO_PATH:
                continue
          
            # Relaxation
            if cost[_next] > _weight + curr_weight:
                cost[_next] = _weight + curr_weight
                heapq.heappush(heap, (cost[_next], _next))

    return cost

'''INPUT'''

V, E = list(map(int, sys.stdin.readline().split()))
start = int(sys.stdin.readline())

graph = [{} for i in range(V+1)]
vetices = [v for v in range(V+1)]

for e in range(E):
    vertex1, vertex2, weight = list(map(int, sys.stdin.readline().split()))
    graph[vertex1][vertex2] = weight if not vertex2 in graph[vertex1] \
        or weight < graph[vertex1][vertex2] else graph[vertex1][vertex2]

'''COMPUTE'''

costs = dijkstra(start, vetices, graph)

'''OUTPUT'''

for cost in costs[1:]:
    print(cost if cost != INF else "INF")

'''
CASE 1. 

5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6


'''