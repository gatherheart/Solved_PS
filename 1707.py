import sys 
from collections import defaultdict

'''CONSTANTS'''

BLACK = -1
WHITE = 1
UNVISITED = 0
RET_TRUE = "YES"
RET_FALSE = "NO"

'''VARIABLES'''
# K(2≤K≤5) V(1≤V≤20,000) E(1≤E≤200,000)

K = 0 
graphs = defaultdict(list)
results = []

'''UTILS'''

'''
bipartite = when one edge is removed, two disjoint set are made

@params
curr = current position
graph
color_map
color = color that should be

'''
def DFS(start, graph, color_map, _color):
    
    ret = True
    stack = []
    
    stack.append((start, _color))
    
    while stack:
        curr, color = stack.pop()
        
        if color_map[curr] == UNVISITED:
            color_map[curr] = color
    
        for vertex2 in graph[curr]:
            if color_map[vertex2] == color:
                return False
            
            if color_map[vertex2] != UNVISITED:
                continue
            
            stack.append((vertex2, -color))

    return ret

def is_bipartite(vertices, edges):

    graph = defaultdict(list)
    color_map = [UNVISITED for _ in range(len(vertices)+1)]
    ret = True
    for e in edges:
        vertex1, vertex2 = e
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)

    for v in vertices:
        if color_map[v] != UNVISITED:
            continue

        ret = ret & DFS(v, graph, color_map, BLACK)

    return ret

'''INPUT'''
'''COMPUTE'''

K = int(sys.stdin.readline())

for k in range(K):
    V, E = list(map(int, sys.stdin.readline().split()))
    for e in range(E):
        graphs[(V, E)].append(tuple(map(int, sys.stdin.readline().split())))
    
    vertices = [v for v in range(1, V+1)]
    results.append(RET_TRUE if is_bipartite(vertices, graphs[(V, E)]) else RET_FALSE)
    graphs[(V, E)] = []

'''OUTPUT'''

for result in results:
    print(result)

'''
CASE 1. Normal Case

2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2


1
4 4
1 2
1 3
2 4
3 4

CASE 2. Disconnected Graph

1
5 3
1 2
1 3
4 5


CASE 3. Disconnected Graph and the second graph is not-bipartite

1
6 5
1 2
1 3
4 5
5 6
4 6

1
5 4
1 2
3 4
3 5
4 5


3
4 3
1 2
4 3
2 3
4 4
2 3
1 4
3 4
1 2
4 3
1 2
2 3
3 4

11
3 1
2 3

3 2
1 3
2 3

4 4
1 2
2 3
3 4
4 2

3 2
2 1
3 2

4 4
2 1
3 2
4 3
4 1

5 2
1 5
1 2

5 2
1 2
2 5

4 3
1 2
4 3
2 3

4 4
2 3
1 4
3 4
1 2

3 3
1 2
2 3
3 1

2 1
1 2

'''