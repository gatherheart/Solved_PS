import sys 
sys.setrecursionlimit(10*6)

'''CONSTANTS'''
DEFAULT_CACHE_VALUE = 0XFFFFFFFF

'''VARIABLES'''

'''UTILS'''

def palindrome(numbers, dp, left, right):

    if left >= right:
        return 0
    
    if dp[left][right] != DEFAULT_CACHE_VALUE:
        return dp[left][right]
    
    left_val, right_val = numbers[left], numbers[right]

    if left_val != right_val:
        dp[left][right] = min(palindrome(numbers, dp, left+1, right),
                              palindrome(numbers, dp, left, right-1)) + 1
    else:
        dp[left][right] = palindrome(numbers, dp, left+1, right-1)

    return dp[left][right]
'''INPUT'''

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
dp = [[DEFAULT_CACHE_VALUE] * N for _ in range(N)]

'''COMPUTE'''

print(palindrome(numbers, dp, 0, N-1))

'''OUTPUT'''
