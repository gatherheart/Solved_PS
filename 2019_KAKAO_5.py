import heapq
import sys
from collections import defaultdict

sys.setrecursionlimit(10000)

INF = 0xFFFFFFFF

class Node: 
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.left = None
        self.right = None
    
class Tree:
    
    def __init__(self):
        super().__init__()
        self.root = None
        
    def getNode(self, data):
        return Node(data)
    
    def insert(self, data):
        
        #print("*"*10)
        prev_pointer = None
        pointer = self.root
        
        if not pointer:
            self.root = self.getNode(data)
            return 
        
        x, y, index = data
        
        while pointer:
            #print("Curr:", pointer.data)
            if x < pointer.data[0]:
                prev_pointer = pointer
                pointer = pointer.left
                
            elif x > pointer.data[0]:
                prev_pointer = pointer
                pointer = pointer.right
                
        if x < prev_pointer.data[0]:
            prev_pointer.left = self.getNode(data)
            #print("Insert Left", data)
            
        elif x > prev_pointer.data[0]:
            prev_pointer.right = self.getNode(data)
            #print("Insert Right", data)

    def preorder(self, curr=None, ret=[]):
        if not curr:
            curr = self.root
        
        ret.append(curr.data[-1])
            
        if curr.left:
            self.preorder(curr.left, ret)
        
        if curr.right:
            self.preorder(curr.right, ret)

        return ret

    def postorder(self, curr=None, ret=[]):
        if not curr:
            curr = self.root

        if curr.left:
            self.postorder(curr.left)
        
        if curr.right:
            self.postorder(curr.right)

        ret.append(curr.data[-1])
        return ret

def solution(nodeinfo):
    answer = []
    meta_data = defaultdict(list)
    tree = Tree()
    
    for idx, info in enumerate(nodeinfo):
        x, y = info 
        meta_data[y].append((x, y, idx + 1))

    meta_data = dict(sorted(meta_data.items(), key=lambda x: -x[0]))
    
    for layer in meta_data:
        nodes = meta_data[layer]
        
        for node in nodes:
            tree.insert(node)
    
    answer.append(tree.preorder())
    answer.append(tree.postorder())
    
    return answer

if __name__ == "__main__":

    test = 1
    
    if test == 1:
        nodeinfo = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
    
    print(solution(nodeinfo))