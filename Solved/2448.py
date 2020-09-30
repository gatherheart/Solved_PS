import sys 
import math
'''MACROS'''

'''VARIABLES'''
# 3.pow(2k) = (3, 6, 12, 24, 48, ...) (k ≤ 10)
N = 3
arr = []
tree = ["  *   ", " * *  ", "***** "]

'''UTILS'''
'''
@Params 
N: int = # of lines
h: int = current height (0 <= h <= N)
'''

def draw_tree(arr):
    for row in arr:
        print(row)
    return

def append_two_tree(tree, shift):
    len_tree = len(tree)
    for i in range(len_tree):
        tree.append(tree[i]+tree[i])
        tree[i] = " " * shift + tree[i] + " " * shift

    return

'''INPUT'''

N = int(sys.stdin.readline())
K = int(math.log(N // 3, 2))

'''COMPUTE'''

for i in range(K):
    # shift = 21 18 12
    append_two_tree(tree, int(3 * math.pow(2, i)))


'''OUTPUT'''
draw_tree(tree)