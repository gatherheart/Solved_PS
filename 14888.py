import sys 
from collections import defaultdict, deque
from itertools import permutations
'''CONSTANTS'''

ADD = 0
SUB = 1
MUL = 2
DIV = 3

CACHE_MISS = 0

'''VARIABLES'''
N = 0
numbers = []
operators = {}

'''UTILS'''

def find_min_max(N, numbers, ops):
    op_comb = [*[ADD]*ops[ADD], *[SUB]*ops[SUB], *[MUL]*ops[MUL], *[DIV]*ops[DIV]]

    min_res, max_res = sys.maxsize, -sys.maxsize
    cache = defaultdict(bool)
    for perm in permutations(op_comb, N-1):
        if cache[perm]:
            continue
        
        _nums = deque(numbers[:])
        
        for op in perm:
            res = 0
            lhs = _nums.popleft()
            rhs = _nums.popleft()
            
            if op == ADD:
                res = lhs + rhs
            elif op == SUB:
                res = lhs - rhs
            elif op == MUL:
                res = lhs * rhs
            elif op == DIV:
                res = int(lhs/rhs)
            
            _nums.appendleft(res)
            
        cache[perm] = True  
        
        result = _nums[0]
        
        min_res = min(min_res, result)
        max_res = max(max_res, result)
    
    return max_res, min_res

'''INPUT'''

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))

'''COMPUTE'''

for res in find_min_max(N, numbers, operators):
    print(res)

'''OUTPUT'''
