import sys 
from collections import defaultdict
sys.setrecursionlimit(100000)

'''CONSTANTS'''
MAX_COLOR = 17

'''VARIABLES'''
n = 0
graph = defaultdict(list)
dp = []
visited = defaultdict(bool)
INITIAL_CACHE = 0xFFFFFFFFFFFF

'''UTILS'''

def build_dp(graph, curr, visited, dp):

    visited[curr] = True
    for _next in graph[curr]:
        if visited[_next]:
            continue
        
        build_dp(graph, _next, visited, dp)
    
        for current_color in range(1, MAX_COLOR):
            min_value = INITIAL_CACHE
            for child_color in range(1, MAX_COLOR):
            
                if current_color != child_color:
                    min_value = min(min_value, dp[_next][child_color])
            
            dp[curr][current_color] += min_value
    
    for color in range(1, MAX_COLOR):
        dp[curr][color] += color 
    
    return

'''INPUT'''

n = int(sys.stdin.readline())
for i in range(n-1):
    x, y = list(map(int, sys.stdin.readline().split()))
    graph[x].append(y)
    graph[y].append(x)

dp = [[0] * MAX_COLOR for i in range(n+1)]

'''COMPUTE'''

build_dp(graph, 1, visited, dp)
print(min(dp[1][1:]))