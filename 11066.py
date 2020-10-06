import sys 
from itertools import combinations

'''CONSTANTS'''
DEFAULT_CACHE_VALUE = 0xFFFFFFFF

'''VARIABLES'''
T, K = 0, 0
costs = []

'''UTILS'''

        
'''INPUT'''

T = int(sys.stdin.readline())

'''COMPUTE'''

for _ in range(T):
    K = int(sys.stdin.readline())
    costs = list(map(int, sys.stdin.readline().split()))

    cache = [[0] * K for _ in range(K)]
    summed = [[0] * K for _ in range(K)]
        
    for i in range(K-1):
        summed[i][i+1] = costs[i] + costs[i+1]
        for j in range(i+2, K):
            summed[i][j] = summed[i][j-1] + costs[j]
    
    for gap in range(1, K):
        for start in range(K-gap):
            end = start + gap
            cache[start][end] = DEFAULT_CACHE_VALUE
            
            for mid in range(start, end):
            
                cache[start][end] = min(cache[start][end],
                                        cache[start][mid] + cache[mid+1][end] + 
                                        summed[start][end])
                

    print(cache[0][K-1])    
    
'''OUTPUT'''
'''
1 
4
40 30 30 50
'''