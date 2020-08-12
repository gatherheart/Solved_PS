import sys
import itertools

'''MACROS'''
OFFSET = [[-1, 0], [0, 1], [1, 0], [0, -1]]
INF = 0xFFFFFFFF

'''VARIABLES'''
# (1 ≤ R,C ≤ 20)
R, C = 0, 0
LEN_UNICODE = 255
prevs = [False] * LEN_UNICODE
arr = []
stack = []
max_count = 1

'''UTILS'''
def print_arr(_arr, N, M):
    for i in range(N):
        for j in range(M):
            print(_arr[i][j], end=" ")
        print()

def is_passed(position, prevs, arr):
    return prevs[ord(arr[position[0]][position[1]])]

def is_overflow(position, N, M):
    x, y = position
    return x < 0 or x >= N or y < 0 or y >= M

def DFS(position, arr, prevs, count, N, M):
    
    x, y = position
    max_count = count

    for dir in range(len(OFFSET)):
        new_x = x + OFFSET[dir][0]
        new_y = y + OFFSET[dir][1]
        if is_overflow((new_x, new_y), N, M) or is_passed((new_x, new_y), prevs, arr):
            continue
        
        prevs[ord(arr[new_x][new_y])] = True
        max_count = max(max_count, DFS((new_x, new_y), arr, prevs, count+1, N, M))
        prevs[ord(arr[new_x][new_y])] = False


    return max_count

'''INPUT'''
line = sys.stdin.readline().split()
R, C = list(map(int, line))

for r in range(R):
    line = list(sys.stdin.readline())
    line.remove('\n')
    arr.append(line)

'''COMPUTE'''

START_POSITION = (0, 0)
prevs[ord(arr[START_POSITION[0]][START_POSITION[1]])] = True
max_count = DFS(START_POSITION, arr, prevs, max_count, R, C)    

'''OUTPUT'''

print(max_count)

'''
Condition: 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

CASE 1. 
Normal Case ->     

2 4
CAAB
ADCB

3 4
ABCD
EADE
FGHG

-> 8

4 3
AEF
BAA
CDH
DEG 

-> 7

4 4
ABCD
BCDE
CDEF
DEFG

-> 7

4 4
ABCD
BCDE
CDEH
DEGG

-> 7

4 4
ABCD
BCBB
CDBH
DEGG

CASE 2. 
All Same letters

2 4
AAAA
AAAA

3 4
BBBB
BBBB
BBBB

4 4
ABCD
BCDB
FGHI
JKLM

CASE 3.
All Different letters

2 4
ABCD
EFGH

CASE 4.
Maximun limit 
20 20
AYXWVUTSRQPONMLKJIHG
YXWVUTSRQPONMLKJIHGF
XWVUTSRQPONMLKJIHGFE
WVUTSRQPONMLKJIHGFED
VUTSRQPONMLKJIHGFEDC
UTSRQPONMLKJIHGFEDCB
TSRQPONMLKJIHGFEDCBA
SRQPONMLKJIHGFEDCBAA
RQPONMLKJIHGFEDCBAAA
QPONMLKJIHGFEDCBAAAA
PONMLKJIHGFEDCBAAAAA
ONMLKJIHGFEDCBAAAAAA
NMLKJIHGFEDCBAAAAAAA
MLKJIHGFEDCBAAAAAAAA
LKJIHGFEDCBAAAAAAAAA
KJIHGFEDCBAAAAAAAAAA
JIHGFEDCBAAAAAAAAAAA
IHGFEDCBAAAAAAAAAAAA
HGFEDCBAAAAAAAAAAAAA
GFEDCBAAAAAAAAAAAAAA
'''