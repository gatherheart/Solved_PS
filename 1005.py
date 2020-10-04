from heapq import heapify
import sys
from collections import defaultdict, deque

'''CONSTANTS'''

'''VARIABLES'''
T, N, K = 0, 0, 0
costs = []
graph = defaultdict(list)
indegree = defaultdict(int)

'''UTILS'''

def topological_sort(graph, indegree, costs):
    
    starts = list(map(lambda x: x[0], filter(lambda x: x[1] == 0, indegree.items())))
    queue = deque([*starts])
    accumulated = costs[:]
    accumulated[queue[0]] = costs[queue[0]]
    
    while queue:
        curr = queue.popleft()
        
        for _next in graph[curr]:
            indegree[_next] -= 1
            accumulated[_next] = max(accumulated[_next], 
                                 accumulated[curr] + costs[_next])
            if indegree[_next] == 0:
                queue.append(_next)
                
        
    return accumulated
    

'''INPUT'''

T = int(sys.stdin.readline())
answer = []

for _ in range(T):
    N, K = list(map(int, sys.stdin.readline().split()))
    costs = [0, *list(map(int, sys.stdin.readline().split()))]
    
    for i in range(K):
        x, y = list(map(int, sys.stdin.readline().split()))
        graph[x].append(y)
        indegree[x] = indegree[x]
        indegree[y] += 1
    
    w = int(sys.stdin.readline())
    
    accumulated = topological_sort(graph, indegree, costs)
    answer.append(accumulated[w])
    graph.clear()
    indegree.clear()             

'''COMPUTE'''

for a in answer:
    print(a)

'''OUTPUT'''