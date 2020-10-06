INF = 0xFFFFFFFF




def floydWarshall(V, graph):
    
    dist = [g[:] for g in graph]
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    
    print(dist)


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

# Print the solution 
floydWarshall(V, graph); 