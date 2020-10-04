from collections import deque

class Node:
    def __init__(self, key) -> None:
        self.data = key
        self.childrens = []
        
    
class Tree:
    def __init__(self, key) -> None:
        self.root = self.get_node(key)
    
    def get_node(self, key):
        return Node(key)
    
    def post_order(self):
        
        s1, s2 = [], []
        
        s1.append(self.root)
        
        while s1:
            node = s1.pop()
            s2.append(node)            
            for child in node.childrens:
                s1.append(child)

        while s2:
            print(s2.pop().data)
        
    def pre_order(self):
        
        s1, s2 = [], deque([])
        s1.append(self.root)
        
        while s1:
            node = s1.pop()
            s2.append(node)
            for child in node.childrens[::-1]:
                s1.append(child)
        
        while s2:
            print(s2.popleft().data)
            
    def level_order(self):
        
        s1, s2 = deque([]), deque([])
        s1.append(self.root)
        
        while s1:
            node = s1.popleft()
            s2.append(node)
            
            for child in node.childrens:
                s1.append(child)
        
        while s2:
            print(s2.popleft().data)
        
# Driver program to test above function 
tree = Tree(1) 
tree.root.childrens = [Node(2), Node(3)]
tree.root.childrens[0].childrens = [Node(4), Node(5)]
tree.root.childrens[1].childrens = [Node(6), Node(7)]

tree.level_order()