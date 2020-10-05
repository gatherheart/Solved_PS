import sys 

'''CONSTANTS'''

'''VARIABLES'''
N = 0
index = 0
left, right = 1, 0
'''UTILS'''

def count_smaller(mid, N):
    ret = 0
    for i in range(1, N+1):
        ret += min(mid // i, N)
    return ret
'''INPUT'''

N = int(sys.stdin.readline())
index = int(sys.stdin.readline())
right = N * N

'''COMPUTE'''
answer = 1

while left <= right:
    mid = (left + right) // 2
    
    count = count_smaller(mid, N)
    if count < index:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1
        
print(answer)