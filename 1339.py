import sys 
from collections import defaultdict
from functools import reduce

sys.setrecursionlimit(10000)
'''CONSTANTS'''
DEFAULT_VALUE = -1

'''VARIABLES'''

'''UTILS'''
def backtracking(words, allocated, selected, alphabets, curr=0):
    
    ret = 0
    if curr >= len(alphabets):
        numbers = []

        for word in words:
            numbers.append(int("".join(list(map(lambda char: str(allocated[char]), word)))))
        return sum(numbers)
    
    for i in range(10):
        curr_char = alphabets[curr]
        # Not yet allocated alphabet
        if not selected[i]:
            selected[i] = True
            allocated[curr_char] = i
            ret = max(ret, backtracking(words, allocated, selected, alphabets, curr+1))
            selected[i] = False
            allocated[curr_char] = DEFAULT_VALUE
    
    return ret

'''INPUT'''

N = int(sys.stdin.readline())
words = []
alphabets = set()
allocated = defaultdict(int)
selected = defaultdict(bool)

for i in range(N):
    line = list(sys.stdin.readline().strip())
    words.append(line)
    for char in line:
        alphabets.add(char)
        
for char in alphabets:
    allocated[char] = DEFAULT_VALUE
    
'''COMPUTE'''

print(list(alphabets))

print(backtracking(words, allocated, selected, sorted(list(alphabets))))

'''OUTPUT'''
