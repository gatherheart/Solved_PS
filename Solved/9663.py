''' VARIABLES '''
N = 0
arr = []

# for Memoization
prev_col = []
left_prevs = []
right_prevs = []
OFFSET = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
QUEEN = 1
BLANK = 0
SAFE = True
UNSAFE = False


'''
N = 4

0 1 0 0    0 0 1 0
0 0 0 1    1 0 0 0
1 0 0 0    0 0 0 1
0 0 1 0    0 1 0 0

N = 5 

1 0 0 0 0   1 0 0 0 0
0 0 1 0 0   0 0 0 1 0
0 0 0 0 1   0 1 0 0 0
0 1 0 0 0   0 0 0 0 1    ... 
0 0 0 1 0   0 0 1 0 0

'''


''' UTILS '''

def print_arr(_arr, N, M):
    for i in range(N):
        for j in range(M):
            print(_arr[i*N+j], end=" ")
        print()

def is_overflow(x, y, N, M):
    if x < 0 or x >= N or y < 0 or y >= M:
        return True
    return False

def is_safe(arr, x, y, left_prevs, right_prevs, N):

    val1 = x - y
    val2 = N - x - y
    if val1 in left_prevs:
        return False
    if val2 in right_prevs:
        return False

    return True


'''
@params 
arr = [] map array
row = current row position
count = [0] the # of ways to position, using list object for pass by reference
N = max position
'''
def n_Queens(arr, row, count, prev_col, left_prevs, right_prevs, N):
    
    # Base Case
    if row >= N:
        _count = count.pop(0)
        count.append(_count + 1)
        
        return True

    # check columns using Recursive loop, Backtracking
    for i in range(N):
        
        if i in prev_col:
            continue

        if not is_safe(arr, row, i, left_prevs, right_prevs, N):
            continue

        arr[row*N + i] = QUEEN
        
        # Save impossible positions 
        prev_col.append(i)
        left_prevs.append(row - i)
        right_prevs.append(N - row - i)

        n_Queens(arr, row + 1, count, prev_col, left_prevs, right_prevs, N)

        arr[row*N + i] = BLANK
        prev_col.pop(-1)
        left_prevs.pop(-1)
        right_prevs.pop(-1)
            
    return False

''' INPUT '''
N = int(input())
arr = [0 for _ in range(N*N)]
count = [0]

''' COMPUTE '''

n_Queens(arr, 0, count, prev_col, left_prevs, right_prevs, N)

''' OUTPUT '''

print(count[0])