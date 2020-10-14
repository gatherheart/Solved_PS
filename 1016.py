import sys 
import math
'''CONSTANTS'''

'''VARIABLES'''

'''UTILS'''

'''INPUT'''

MIN, MAX = list(map(int, sys.stdin.readline().split()))

'''COMPUTE'''

sieve = [True] * (MAX - MIN + 1)
count = 0

for number in range(2, int(math.sqrt(MAX)+1)):
    index = number * number
    
    for i in range(math.ceil(MIN / index), MAX // index + 1):
        test = index * i - MIN
        if sieve[index * i - MIN]:
            sieve[index * i - MIN] = False
            count += 1

print(MAX - MIN + 1 - count)

'''OUTPUT'''