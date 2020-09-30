import sys

'''MACROS'''
COMMAND_UNION = 0
COMMAND_FIND = 1
RET_TRUE = "YES"
RET_FALSE = "NO"

'''VARIABLES'''
# n(1≤n≤1,000,000), m(1≤m≤100,000)
n, m = 0, 0

class DisjointSet:

    def __init__(self, vertices, parent={}):
        super().__init__() 
        self.vertices = vertices
        self.parent = parent
        for v in vertices:
            self.parent[v] = v

    def find_set(self, item, size):
        if self.parent[item] == item:
            return item, size
        else:
            return self.find_set(self.parent[item], size + 1)

    def union(self, item1, item2):
        root1, size1 = self.find_set(item1, 0)
        root2, size2 = self.find_set(item2, 0)

        if size1 >= size2:
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2
        return

    def is_same_parent(self, item1, item2):
        root1, size1 = self.find_set(item1, 0)
        root2, size2 = self.find_set(item2, 0)
        return root1 == root2

'''UTILS'''

'''INPUT'''

n, m = list(map(int, sys.stdin.readline().split()))

'''COMPUTE'''

tree_set = DisjointSet([i for i in range(n+1)], {})
results = []
for i in range(m):
    command, a, b = list(map(int, sys.stdin.readline().split()))

    if command == COMMAND_UNION:
        tree_set.union(a, b)
    elif command == COMMAND_FIND:
        if tree_set.is_same_parent(a, b):
            results.append(RET_TRUE)
        else:
            results.append(RET_FALSE)

'''OUTPUT'''
for r in results:
    print(r)