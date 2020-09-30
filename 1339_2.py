import sys 
from collections import defaultdict
from functools import reduce

sys.setrecursionlimit(10000)
'''CONSTANTS'''
DEFAULT_VALUE = -1

'''VARIABLES'''

'''UTILS'''

def parse_words(words):
    classified = defaultdict(list)
    inverted = defaultdict(int)

    for word in words:
        for i, char in enumerate(word):
            classified[len(word)-i-1].append(char)
       
    for item in sorted(classified.items(), key=lambda x: -x[0]):
        key, chars = item
        for char in chars:
            inverted[char] += pow(10, key)
    
    alphabets = list(map(lambda x: x[0], sorted(inverted.items(), key=lambda x: -x[1])))
    return alphabets


def backtracking(words, allocated, alphabets, curr=0):
    
    ret = 0
    if curr >= len(alphabets):
        numbers = []

        for word in words:
            numbers.append(int("".join(list(map(lambda char: str(allocated[char]), word)))))
            
        return sum(numbers)
    
    curr_char = alphabets[curr]
    # Not yet allocated alphabet
    allocated[curr_char] = 10 - curr - 1
    return backtracking(words, allocated, alphabets, curr+1)

'''INPUT'''

N = int(sys.stdin.readline())
words = []
allocated = defaultdict(int)

for i in range(N):
    line = list(sys.stdin.readline().strip())
    words.append(line)


alphabets = parse_words(words)

for char in alphabets:
    allocated[char] = DEFAULT_VALUE
    
'''COMPUTE'''

print(backtracking(words, allocated, alphabets))

'''OUTPUT'''
