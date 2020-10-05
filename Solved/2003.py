import sys 
from collections import deque

'''CONSTANTS'''

'''VARIABLES'''

N, M = 0, 0
numbers = []
_sum = 0
count = 0
window = deque()

'''UTILS'''

'''INPUT'''

N, M = list(map(int, sys.stdin.readline().split()))
numbers = deque(map(int, sys.stdin.readline().split()))

'''COMPUTE'''

while True:

    if numbers and _sum <= M:
        num = numbers.popleft()
        window.append(num)
        _sum += num
    elif _sum > M:
        _sum -= window.popleft()
    else:
        break
        
    if _sum == M:
        count += 1
        
'''OUTPUT'''

print(count)