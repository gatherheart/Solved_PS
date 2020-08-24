import sys
import heapq

'''CONSTANTS'''
OFFSET = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
DEFAULT_NUTRITION = 5

'''VARIABLES'''
# 1 ≤ N ≤ 10,  = # of row
# 1 ≤ M ≤ N^2 = # of tree 
# 1 ≤ K ≤ 1,000 = after year
N, M, K = 0, 0, 0
arr = []
tree = []
alives, deads = [], []

'''UTILS'''
def print_arr(_arr, N, M):
    for i in range(1, N):
        for j in range(1, M):
            print(_arr[i][j], end=" ")
        print()

def is_overflow(x, y, N, M):
    return x <= 0 or x >= N + 1 or y <= 0 or y >= M + 1

# Get Nutrition and get Age
def spring_season(tree, arr):

    heap = tree[:]
    alives, deads = [], []

    def is_sufficient(age, amount):
        return amount - age >= 0

    while heap:
        x, y, age = heapq.heappop(heap)
        
        if is_sufficient(age, arr[x][y]):
            heapq.heappush(alives, (x, y, age + 1))
            arr[x][y] -= age
            
        else:
            deads.append((x, y, age))

    return alives, deads

# Provide Nutrition of dead trees
def summer_season(deads, arr):

    while deads:
        x, y, age = deads.pop()
        new_nutrition = age // 2
        arr[x][y] += new_nutrition

    return

# add New trees
def autumn_season(alives, N):
    stack = alives[:]
    NEW_TREE_AGE = 1

    while stack:
        x, y, age = stack.pop()
        if age % 5 != 0:
            continue

        for _dir in range(len(OFFSET)):
            new_x = x + OFFSET[_dir][0]
            new_y = y + OFFSET[_dir][1]
            
            if is_overflow(new_x, new_y, N, N):
                continue

            heapq.heappush(alives, (new_x, new_y, NEW_TREE_AGE))

    return

# Addition to nutrition
def winter_season(addition, arr, N):

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            arr[i][j] += addition[i][j]

    return


'''INPUT'''

N, M, K = list(map(int, sys.stdin.readline().split()))
nutrition = [[DEFAULT_NUTRITION for j in range(N + 1)] for i in range(N + 1)]
addition = [[0 for j in range(N + 1)]]

for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    addition.append([0, *line])

for i in range(M):
    x, y, age = list(map(int, sys.stdin.readline().split()))
    heapq.heappush(tree, (x, y, age))

'''COMPUTE'''

for i in range(K):
    alives, deads = spring_season(tree, nutrition)
    summer_season(deads, nutrition)
    autumn_season(alives, N)
    winter_season(addition, nutrition, N)
    tree = alives

'''OUTPUT'''

print(len(alives))
'''
CASE 1. Normal


CASE 2. duplicated corrdinates

5 2 1
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 2
2 1 3


CASE 3.
5 2 10
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3

'''