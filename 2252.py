import sys 
from collections import deque

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

def topological_sort(indegree, dag):

    queue = deque()
    ordered = []

    # Find 0 indegree nodes
    for i, _in in enumerate(indegree):
        if _in == 0:
            queue.append(i)

    # BFS for 0 indegree nodes first
    while queue:
        curr = queue.popleft()
        ordered.append(curr)

        for _next in dag[curr]:
            indegree[_next] -= 1
            if indegree[_next] == 0:
                queue.append(_next)

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