import sys 

'''MACROS'''

'''VARIABLES'''
# 3.pow(2k) = (3, 6, 12, 24, 48, ...) (k ≤ 10)
N = 3
arr = []
'''UTILS'''
'''
@Params 
N: int = # of lines
h: int = current height (0 <= h <= N)
'''

def draw_tree(arr):
    for row in arr:
        sys.stdout.write("".join(row)+'\n')
    return

def traverse(N, h, vertex_pos, arr):
    # BASE CASE    
    if h >= N:
        return

    if arr[h][vertex_pos] == " ":
        arr[h][vertex_pos] = "*"
        arr[h+1][vertex_pos-1], arr[h+1][vertex_pos+1] = "*", "*"
        arr[h+2][vertex_pos-2:vertex_pos+3] = ["*"]*5
    else:
        arr[h][vertex_pos] = " "
        arr[h+1][vertex_pos-1], arr[h+1][vertex_pos+1] = " ", " "
        arr[h+2][vertex_pos-2:vertex_pos+3] = [" "]*5

    
    # height = 0 3 6 12 24 ...
    # vertex_pos = 24 (21, 27) ((19), (30)) ((13), (25)) ((24), (36))
    traverse(N, h+3, vertex_pos-3, arr)
    traverse(N, h+3, vertex_pos+3, arr)

'''INPUT'''

N = int(sys.stdin.readline())
arr = [[" " for _ in range(2*N - 1)] for _ in range(N)]

'''COMPUTE'''
traverse(N, 0, N-1, arr)
draw_tree(arr)

'''OUTPUT'''