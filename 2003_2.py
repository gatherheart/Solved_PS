import sys 
from collections import deque

'''CONSTANTS'''

'''VARIABLES'''

N, M = 0, 0
numbers = []
_sum = 0
count = 0
left, right = 0, 0

'''UTILS'''

'''INPUT'''

N, M = list(map(int, sys.stdin.readline().split()))
numbers = list(map(int, sys.stdin.readline().split()))

'''COMPUTE'''

while left < N:

    if right <= N - 1 and _sum <= M:
        _sum += numbers[right]
        right += 1
    else:
        _sum -= numbers[left]
        left += 1
    
    if _sum == M:
        count += 1
        
'''OUTPUT'''

print(count)