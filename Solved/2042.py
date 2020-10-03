import sys 

'''CONSTANTS'''

UPDATE = 1
READ = 2

'''VARIABLES'''
N, M, K = 0, 0, 0
arr = []
commands = []

'''UTILS'''

class SegmentTree:
    def __init__(self, arr) -> None:
        self.n = len(arr)
        self.tree = [0] * self.n * 2
        self.build(arr)
        
    def build(self, arr) -> None:
        for i in range(self.n, self.n*2):
            self.tree[i] = arr[i-self.n]

        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[i*2] + self.tree[i*2+1]
    
    def update(self, index, value) -> None:
        
        index = self.n + index
        self.tree[index] = value
        
        while 1 < index:
            self.tree[index // 2] = self.tree[index] + self.tree[index^1]
            index //= 2
        
    def query(self, _from, _to) -> int:
        
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

N, M, K = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    arr.append(int(sys.stdin.readline()))
    
for i in range(M + K):
    commands.append(list(map(int, sys.stdin.readline().split())))    

'''COMPUTE'''
tree = SegmentTree(arr)
for comd in commands:
    a, b, c = comd
    if a == UPDATE:
        tree.update(b-1, c)
    elif a == READ:
        print(tree.query(b-1, c))


'''
12 2 2
1
2
3
4
5
6
7
8
9
10
11
12
2 1 8
1 3 1
2 1 8
1 3 1

'''

