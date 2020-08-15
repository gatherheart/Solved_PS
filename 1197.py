import sys 
from collections import defaultdict

'''MACROS'''

'''VARIABLES'''
# V(1 ≤ V ≤ 10,000) E(1 ≤ E ≤ 100,000)
V, E = 0, 0
edges = []

class DisjointSet:

    def __init__(self, vertices):
        super().__init__()
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
    
    def is_same_root(self, a, b):
        root1, size1 = self.find(a)
        root2, size2 = self.find(b)

        return root1 == root2

    def find(self, v, size=0):
        if self.parent[v] == v:
            return v, size
        return self.find(self.parent[v], size+1)
        
    def union(self, a, b):
        root1, size1 = self.find(a)
        root2, size2 = self.find(b)

        if size1 >= size2:
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2
        return

    def __str__(self):
        return 'disjoint set: {}'.format(self.parent)

'''UTILS'''
def mst(edges, disjoint_set):
    edges.sort(key=lambda x: x[2])
    weight_sum = 0
    selected_edges = []
    for e in edges:
        # Check parent 
        vertex1, vertex2, weight = e
        if disjoint_set.is_same_root(vertex1, vertex2):
            continue
            
        disjoint_set.union(vertex1, vertex2)
        weight_sum += weight
        selected_edges.append(e)

    return weight_sum, selected_edges

'''INPUT'''

V, E = list(map(int, sys.stdin.readline().split()))

for _ in range(E):
    A, B, C = list(map(int, sys.stdin.readline().split()))
    edges.append((A, B, C))

'''COMPUTE'''

disjoint_set = DisjointSet([i for i in range(1, V+1)])

weight, selected = mst(edges, disjoint_set)

'''OUTPUT'''

print(weight)

'''
CASE 1. Normal case

3 3
1 2 1
2 3 2
1 3 3

3 3
1 3 3
1 2 1
2 3 2

CASE 2. Negative value 

5 6
1 3 3
1 2 1
2 3 -1
3 4 -2
4 3 -3
4 5 2

CASE 3. All same weight value

5 7
1 3 0
1 2 0
2 3 0
3 4 0
4 3 0
4 5 0
1 5 0 

'''