import sys 

'''CONSTANTS'''
LEAF_NODE = {}
DEFAULT_CACHE_VALUE = sys.maxsize

'''VARIABLES'''
#  n(1 ≤ n ≤ 10,000)
n = 0
tree = []

'''UTILS'''

def tree_traversal(root, V, tree):
    
    parent = root
    stack1 = [(0, root, -1)]
    stack2 = []
    cache = [0] * (V + 1)
    diameter = [-DEFAULT_CACHE_VALUE, -DEFAULT_CACHE_VALUE]

    # fill up nodes
    while stack1:
        
        weight, curr, parent = stack1.pop()
        stack2.append((weight, curr, parent))

        parent = curr

        childs = list(tree[curr].keys())
        for child in childs:
            stack1.append((tree[parent][child], child, parent))

    # Pop up nodes
    while stack2:
        weight, curr, parent = stack2.pop()

        if sum(diameter) < cache[parent] + cache[curr] + weight:
            diameter = [cache[parent], cache[curr] + weight]

        cache[parent] = max(cache[parent], cache[curr] + weight)
    
    return sum(diameter)

'''INPUT'''

n = int(sys.stdin.readline())

tree = [{} for _ in range(n + 1)]

for i in range(n - 1):
    parent, child, weight = list(map(int, sys.stdin.readline().split()))
    tree[parent][child] = weight

'''COMPUTE'''

print(tree_traversal(1, n, tree))

'''OUTPUT'''

'''
CASE 1.
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10

=> 45

CASE 2. 
One node that have the longgest Left path but short right path, 
The other Node that have the longgest right path but short left path

12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 40
5 10 4
6 11 6
6 12 10

=> 70

CASE 3. 
One node that have the longgest Left path and the longgest right path, 

12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 40
5 10 38
6 11 6
6 12 10

=> 78

CASE 4.
Only two nodes

2
1 2 1

CASE 5.
Only Left nodes

6
1 2 1
2 3 1
3 4 1
3 5 1
4 6 1

CASE 6.
Not Binary Tree 

13
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10
6 13 30

5
1 2 33
2 3 34
1 4 22
1 5 10

CASE 7.
BIG SIZE

https://doyak.s-ul.eu/cU2LvUpF

'''
