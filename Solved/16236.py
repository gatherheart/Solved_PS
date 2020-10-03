import sys 
from collections import deque, defaultdict
import heapq
'''CONSTANTS'''

OFFSET = [[-1, 0], [0, -1], [0, 1], [1, 0]]

SHARK = 9
EMPTY = 0
NO_MORE_FISH = (-1, -1)

'''VARIABLES'''
N  = 0
board = []
shark_position = None
shark_level = 2
point = 0
answer = 0

'''UTILS'''
def is_bigger_fish(shark_level, x, y, arr):
    return shark_level < arr[x][y]

def is_overflow(x, y, N, M):
    return x < 0 or x >= N or y < 0 or y >= M

def find_min_fish(level, N, arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] != EMPTY and arr[i][j] < level:
                return (i, j)
    return (-1, -1)

def print_arr(arr, N, M):
    for i in range(N):
        for j in range(M):
            print("{:3}".format(arr[i][j]), end=" ")
        print()

def BFS(shark, N, arr):
    
    shark_position, shark_level = shark
    board[shark_position[0]][shark_position[1]] = EMPTY
    queue = [[0, shark_position]]
    visited = defaultdict(bool)
    visited[shark_position] = True
    
    while queue:
        
        distance, curr = heapq.heappop(queue)
        x, y = curr
        #print("CURR", curr, "DIST", distance)
        
        if arr[x][y] != EMPTY and arr[x][y] < shark_level:
            board[x][y] = SHARK
            #print("FOUND, ", (x, y))
            return (x, y), distance
        
        for _dir in range(len(OFFSET)):
            new_x = x + OFFSET[_dir][0]
            new_y = y + OFFSET[_dir][1]
            
            if is_overflow(new_x, new_y, N, N) or \
                is_bigger_fish(shark_level, new_x, new_y, arr):
                continue
            
            if not visited[(new_x, new_y)]:
                heapq.heappush(queue, [distance+1, (new_x, new_y)])
                visited[(new_x, new_y)] = True
    
    return (-1, -1), 0

'''INPUT'''
N = int(sys.stdin.readline())

for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    for j, fish in enumerate(line):
        if fish == SHARK:
            shark_position = (i, j)
            
    board.append(line)


'''COMPUTE'''

while True:
        
    #print("*"*20)
    #print("SHARK LEVEL", shark_level)
    new_shark_position, distance = \
        BFS((shark_position, shark_level), N, board)
    
    if new_shark_position == NO_MORE_FISH:
        break
    
    #print(new_shark_position, distance, answer)
    #print_arr(board, N, N)
    #print()
    
    shark_position = new_shark_position
    answer += distance
    point += 1
    
    if shark_level == point:
        shark_level += 1
        point = 0
        
'''OUTPUT'''

print(answer)