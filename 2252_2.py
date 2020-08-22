import sys 
from collections import deque
sys.setrecursionlimit(100000)

'''CONSTANTS'''

INF = sys.maxsize

'''VARIABLES'''
# N(1≤N≤32,000), M(1≤M≤100,000)

N, M = 0, 0

# Directed acyclic graph
dag = []
indegree = []
result = []

'''UTILS'''

def DFS(curr, visited, ordered, dag):

    if visited[curr]:
        return 

    for _next in dag[curr]:
        if not visited[_next]:
            DFS(_next, visited, ordered, dag)
            visited[_next] = True

    ordered.appendleft(curr)
    return 

def topological_sort(indegree, dag):

    visited = [False] * len(dag)
    ordered = deque()
    
    # Find 0 indegree nodes = Start Nodes
    for i, _in in enumerate(indegree):
        if _in == 0:
            DFS(i, visited, ordered, dag)

    return ordered
'''INPUT'''

N, M = list(map(int, sys.stdin.readline().split()))

dag = [[] for i in range(N + 1)]
indegree = [0 for i in range(N + 1)]

for i in range(M):
    small, tall = list(map(int, sys.stdin.readline().split()))
    dag[small].append(tall)
    indegree[tall] += 1

'''COMPUTE'''

indegree[0] = INF

result = topological_sort(indegree, dag)
for i in result:
    print(i, end=" ")

'''OUTPUT'''


'''
CASE 1. 

3 2
1 3
2 3


CASE 2. 

4 2
4 2
3 1

CASE 3. Duplicate parents

3 2
1 3
1 2

'''