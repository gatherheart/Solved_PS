import sys 
from collections import defaultdict, deque

'''CONSTANTS'''
TREE = '1'
EMPTY = '0'
LOG = 'B'
END = 'E'

OFFSET = [[-1, 0], [0, 1], [1, 0], [0, -1]]
ROTATION = [1, -1]

'''VARIABLES'''
# (4<=N<=50)
N = 0
arr = []
start = []
end = []

'''UTILS'''

def print_arr(_arr, N, M):
    for i in range(N):
        for j in range(M):
            print(_arr[i][j], end=" ")
        print()

def is_safe_for_ratate(current, arr):
    cord1, cord2, cord3 = current
    start = cord2[0] - 1, cord2[1] - 1
    for i in range(start[0], start[0] + 3):
        for j in range(start[1], start[1] + 3):
            if (i, j) in current:
                continue
            
            if arr[i][j] == TREE:
                #print("UNSAFE", current, start, (i, j), arr[i][j] == TREE)
                return False
            
    return True
        
    
def BFS(start, end, N, arr):
    
    if type(start) is not tuple:
        start = tuple(start)
    
    visited = defaultdict(bool)
    queue = deque([[start, 0]])
    
    while queue:
        current, distance = queue.popleft()
        cord1, cord2, cord3 = current
        
        if visited[tuple(current)]:
            continue

        #print(current, distance)
        if current[0] == end[0] and current[1] == end[1] and current[2] == end[2]:
            return distance
            
        visited[tuple(current)] = True
        
        for _dir in range(len(OFFSET)):
            new_cord1 = (cord1[0] + OFFSET[_dir][0], cord1[1] + OFFSET[_dir][1])
            new_cord2 = (cord2[0] + OFFSET[_dir][0], cord2[1] + OFFSET[_dir][1])
            new_cord3 = (cord3[0] + OFFSET[_dir][0], cord3[1] + OFFSET[_dir][1])
            
            if arr[new_cord1[0]][new_cord1[1]] != TREE and \
                arr[new_cord2[0]][new_cord2[1]] != TREE and \
                arr[new_cord3[0]][new_cord3[1]] != TREE:
                    queue.append([(new_cord1, new_cord2, new_cord3), distance+1])
                    #print("NEW MOVE", _dir, sorted((new_cord1, new_cord2, new_cord3)), distance+1)

        # Is_horizontal?
        if cord1[0] == cord2[0] == cord2[0]:
            for r in ROTATION:
                if is_safe_for_ratate(current, arr):
                    new_cord1 = (cord2[0] - r, cord2[1])
                    new_cord2 = (cord2[0], cord2[1])
                    new_cord3 = (cord2[0] + r, cord2[1])
                    #print("NEW rotate HORI", r, sorted((new_cord1, new_cord2, new_cord3)), distance+1)
                    queue.append([sorted((new_cord1, new_cord2, new_cord3)), distance+1])
        
        elif cord1[1] == cord2[1] == cord3[1]:
            for r in ROTATION:
                if is_safe_for_ratate(current, arr):
                    new_cord1 = (cord2[0], cord2[1] - r)
                    new_cord2 = (cord2[0], cord2[1])
                    new_cord3 = (cord2[0], cord2[1] + r)
                    #print("NEW rotate VERTI", r, sorted((new_cord1, new_cord2, new_cord3)), distance+1)
                    queue.append([sorted((new_cord1, new_cord2, new_cord3)), distance+1])

    return 0
     
'''INPUT'''

N = int(sys.stdin.readline())

arr.append([TREE for i in range(N + 2)])
for i in range(N):
    line = [TREE, *list(str(sys.stdin.readline().strip())), TREE]
    for j, c in enumerate(line):
        if c == LOG:
            start.append((i+1, j))
        
        if c == END:
            end.append((i+1, j))

    arr.append(line)
arr.append([TREE for i in range(N + 2)])

'''COMPUTE'''

#print_arr(arr, N+2, N+2)
#print(start)
#print(end)

print(BFS(start, end, N, arr))

'''OUTPUT'''



'''
CASE 
5
B0011
B0000
B0000
11000
EEE00

9
'''