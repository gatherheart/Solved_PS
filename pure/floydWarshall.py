INF = 0xFFFFFFFF

def print_path(path, _from, _to):

    if not path[_from][_to]:
        return
    print_path(path, _from, path[_from][_to])
    print(path[_from][_to])
    print_path(path, path[_from][_to], _to)
        
def floydWarshall(V, graph):
    
    dist = [g[:] for g in graph]
    path = [[None for j in range(V)] for i in range(V)]
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k]+dist[k][j]
                    path[i][j] = k
 
    print(dist)
    print(path)
    print_path(path, 0, 4)

# Driver program to test the above program 
# Let us create the following weighted graph 
""" 
            10 
       (0)<------>(3)-----------5
        |    5    /|\           |
      5 |          |            |
        |        2 | 1          |
       \|/        \|/          \|/
       (1)------->(2)-------->(4)
            3           5
            
"""

V = 5
graph = [[0, 5, INF, 10, INF],
        [INF, 0, 3, INF, INF], 
        [INF, INF, 0, 1, 5], 
        [5, INF, 2, 0, 5],
        [INF, INF, INF, INF, 0]]


graph = [[0, 5, 1, 10, INF],
        [INF, 0, INF, INF, 3], 
        [INF, 2, 0, INF, 6], 
        [INF, INF, INF, INF, 20],
        [INF, INF, INF, INF, 0]]

# Print the solution 
floydWarshall(V, graph); 