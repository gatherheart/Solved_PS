import sys 

'''CONSTANTS'''

INF = sys.maxsize
BLANK = 0

'''VARIABLES'''
# n(1 ≤ n ≤ 100) m(1 ≤ m ≤ 100,000)
n, m = 0, 0
graph = []

'''UTILS'''

def print_arr(_arr, N, M):
    for i in range(1, N+1):
        for j in range(1, M+1):
            print("{}".format(_arr[i][j] if _arr[i][j] != INF else BLANK), end=" ")
        print()

def floyd_warshall(n, graph):
    
    # Diagonal
    for k in range(1, n+1):
        # Row
        for i in range(1, n+1):
            # Col
            for j in range(1, n+1):
                if i == j  or i == k or j == k: 
                    continue
                graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

    return

'''INPUT'''

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[INF if i != j else BLANK for j in range(n + 1)] for i in range(n + 1)]

for i in range(m):
    vertex1, vertex2, weight = list(map(int, sys.stdin.readline().split()))
    graph[vertex1][vertex2] = min(graph[vertex1][vertex2], weight)

'''COMPUTE'''

floyd_warshall(n, graph)

'''OUTPUT'''

print_arr(graph, n, n)


'''
CASE 1.
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4

'''