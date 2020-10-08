import sys 
import math
from itertools import combinations_with_replacement

'''CONSTANTS'''
BREAK_SIGNAL = 0
MAX_RANGE = 2**15
'''VARIABLES'''

dp = [[0] * 5 for _ in range(MAX_RANGE+1)]

'''UTILS'''

'''INPUT'''
dp[0][0] = 1

for i in range(1, int(math.sqrt(MAX_RANGE)+1)):
    for j in range(4):
        for k in range(MAX_RANGE-i*i):
            dp[k+i*i][j+1] += dp[k][j]
            
while True:
    
    N = int(sys.stdin.readline())
    if N == BREAK_SIGNAL:
        break
    
    print(sum(dp[N]))
    
'''COMPUTE'''

'''OUTPUT'''