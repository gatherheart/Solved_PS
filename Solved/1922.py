import sys 
'''CONSTANTS'''

'''VARIABLES'''
N = 0 # N (1 ≤ N ≤ 1000)
M = 0 # (1 ≤ M ≤ 100,000)
edges = []

class DisjointSet:

    def __init__(self, vertices):
        super().__init__()
        self.parent = {}
        for v in vertices:
            self.parent[v] = v

    def find(self, vertex, size=0):
        if self.parent[vertex] == vertex:
            return vertex, size
        
        return self.find(self.parent[vertex], size + 1)

    def union(self, vertex1, vertex2):
        root1, size1 = self.find(vertex1)
        root2, size2 = self.find(vertex2)
        if size1 >= size2:
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2            
        return

    def is_same_root(self, vertex1, vertex2):
        root1, size1 = self.find(vertex1)
        root2, size2 = self.find(vertex2)
        return root1 == root2

    def __str__(self):
        return super().__str__()

    def __len__(self):
        return len(self.parent)

'''UTILS'''

def MST(edges, disjoint_set):
    edges.sort(key=lambda x: x[2])    
    weight_sum = 0
    selected = []

    for e in edges:
        vertex1, vertex2, weight = e

        if disjoint_set.is_same_root(vertex1, vertex2):
            continue

        disjoint_set.union(vertex1, vertex2)
        weight_sum += weight
        selected.append(e)
        
        if len(selected) == len(disjoint_set):
            break

    return weight_sum, selected

'''INPUT'''

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

for i in range(M):
    vertex1, vertex2, weight = list(map(int, sys.stdin.readline().split()))
    edges.append((vertex1, vertex2, weight)) 

'''COMPUTE'''

disjoint_set = DisjointSet([i for i in range(1, N+1)])

weight, selected = MST(edges, disjoint_set)

'''OUTPUT'''

print(weight)

'''

CASE 1

6
9
1 2 5
1 3 4
2 3 2
2 4 7
3 4 6
3 5 11
4 5 3
4 6 8
5 6 8

3 
3
1 3 3
1 2 1
2 3 2

5 
7
1 3 1
1 2 2
2 3 3
3 4 4
4 3 5
4 5 6
1 5 7 

'''