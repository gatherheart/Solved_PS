from typing import List
from collections import defaultdict

class Node:
    def __init__(self, val) -> None:
        self.parent = None
        self.childrens = []
        self.val = val
    
    def __str__(self) -> str:
        return "{}, {}".format(self.val, self.childrens)
    
    def __repr__(self) -> str:
        return "{}".format(self.val)
        
class Tree:
    def __init__(self, edges, cost) -> None:
        self.graph = defaultdict(list)
        self.cost = [0, *cost]
        self.dp = self.cost[:]
         
        for edge in edges:
            x, y = edge
            self.graph[x].append(y)
        
        self.root = self._get_node(edges[0][0])
        self.build(self.root, self.graph[self.root.val])
        
    def build(self, root, childrens) -> List[Node]:
        
        if childrens == []:
            return self.dp[root.val]
        
        for child in childrens:
            root.childrens.append(self._get_node(child))
            self.dp[root.val] = max(self.dp[root.val],
                                      self.cost[root.val] + \
                                      self.build(root.childrens[-1], self.graph[child]))
            
        return self.dp[root.val]
        
    def _get_node(self, val) -> Node:
        return Node(val)
    
    def pre_order(self, curr=None) -> None:
        if curr == None:
            curr = self.root
            
        print(curr, self.dp[curr.val])
        
        for child in curr.childrens:
            self.pre_order(child)
        
        return
    
    def in_order(self, curr=None) -> None:
        
        if curr == None:
            curr = self.root
        
        if curr.childrens == []:
            print(curr)
        
        checked = False
        for child in curr.childrens:
            self.in_order(child)
            if not checked:
                print(curr)
                checked = True
        
        return
    
    def post_order(self, curr=None) -> None:
    
        if curr == None:
            curr = self.root
            
        for child in curr.childrens:
            self.post_order(child)
        
        print(curr)
        
        return
    
    
    
edges = [(1, 2), 
         (1, 3),
         (1, 4),
         (2, 5),
         (2, 6),
         (3, 7),
         (4, 8),
         (4, 9),
         (4, 10),
         (5, 11),
         (5, 12),
         (7, 13),
         (7, 14)]

cost = [ 3, 2, 1, 10, 1, 3, 9, 1, 5, 3, 4, 5, 9, 8 ]
tree = Tree(edges, cost)

tree.pre_order()
print(tree.dp)