import sys
import heapq

'''CONSTANTS'''

INF = sys.maxsize

'''VARIABLES'''
# N(1 ≤ N ≤ 32,000)
# M(1 ≤ M ≤ 100,000)
N, M = 0, 0
problems = []
indegree = []

'''UTILS'''

def topological_sort(indegree, dag):

    heap = []
    result = []

    for i, _in in enumerate(indegree):
        if _in == 0:
            heapq.heappush(heap, i)

    while heap:
        curr = heapq.heappop(heap)
        result.append(curr)
        for _next in dag[curr]:
            indegree[_next] -= 1
            if indegree[_next] == 0:
                heapq.heappush(heap, _next)

    return result

'''INPUT'''
N, M = list(map(int, sys.stdin.readline().split()))
problems = [[] for _ in range(N + 1)]
indegree = [0 for i in range(N + 1)]
indegree[0] = INF

# A should be solved earier than B
for i in range(M):
    A, B = list(map(int, sys.stdin.readline().split()))
    problems[A].append(B)
    indegree[B] += 1

'''COMPUTE'''

ret = topological_sort(indegree, problems)

'''OUTPUT'''

for i in ret:
    print(i, end=" ")

'''
CASE 1.
4 2
4 2
3 1

CASE 2.
4 3
1 2
3 2
3 4


'''