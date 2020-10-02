
class SegmentTree:
    
    def __init__(self, arr) -> None:
        self.N = len(arr)
        self.arr = arr
        self.tree = [0] * (2 * self.N)
        self.build()
        
    def build(self):
        
        for i in range(self.N):
            self.tree[self.N+i] = self.arr[i]

        for i in range(self.N-1, 0, -1):
            self.tree[i] = self.tree[i*2] + self.tree[i*2+1]

    def update(self, index, value):
        
        index = self.N + index
        self.tree[index] = value

        while index > 1:
            self.tree[index // 2] = self.tree[index] + self.tree[index^1]
            index = index // 2
    
    # sum of [_from, _to)
    def get_sum(self, _from, _to):
        _from = self.N + _from
        _to = self.N + _to
        ret = 0
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
    
# Driver Code 
if __name__ == "__main__":
  
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];  
    
    # n is global  
    n = len(a);  
    
    segTree = SegmentTree(a)
    print(segTree)
    # print the sum in range(1,2) index-based  
    print(segTree.get_sum(0, n));  
      
    # modify element at 2nd index  
    segTree.update(2, 1);  
    print(segTree)

    # print the sum in range(1,2) index-based  
    print(segTree.get_sum(0, n));  
      
# This code is contributed by AnkitRai01 