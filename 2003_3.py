import sys 
from collections import deque

'''CONSTANTS'''

'''VARIABLES'''

N, M = 0, 0
numbers = []
left, right = 0, 0
count = 0

'''UTILS'''

class SegmentTree:
    def __init__(self, arr) -> None:
        self.n = len(arr)
        self.tree = [0] * self.n * 2
        self.build(arr)
        
    def build(self, arr):
        
        for i in range(self.n, self.n*2):
            self.tree[i] = arr[i-self.n]
        
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def update(self, index, value):
        
        index += self.n
        
        while index > 1:
            self.tree[index // 2] = self.tree[index] + self.tree[index^1]
            index //= 2
    
    def query(self, _from, _to):
        
        ret = 0
        _from += self.n
        _to += self.n
        
        while _from < _to:
            
            if _from % 2:
                ret += self.tree[_from]
                _from += 1
               
            if _to % 2:
                _to -= 1
                ret += self.tree[_to]
            
            _from >>= 1
            _to >>= 1
            
        return ret
    
    def __str__(self) -> str:
        return "{}".format(self.tree)
            
             

'''INPUT'''

N, M = list(map(int, sys.stdin.readline().split()))
numbers = list(map(int, sys.stdin.readline().split()))

'''COMPUTE'''

tree = SegmentTree(numbers)

while left <= right:
    
    _sum = tree.query(left, right)

    if right < N and _sum <= M:
        right += 1
    else:
        left += 1
    
    if _sum == M:
        count += 1 

'''OUTPUT'''

print(count)