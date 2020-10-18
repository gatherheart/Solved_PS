import sys 
from collections import deque, defaultdict
import heapq

'''CONSTANTS'''
EMPTY = 0
WALL = 1
OFFSET = [[-1, 0], [0, 1], [1, 0], [0, -1]]
OUT_OF_GAS = -1

'''VARIABLES'''
N, M = 0, 0
fuel = 0
start_position = None
board = []
passengers = deque([])
'''UTILS'''

def is_invalid_pos(x, y, N, M, board):
    return x < 0 or y < 0 or x > N or y > M or board[x][y] == WALL

def BFS(current, fuel, dests, board, N, refill=False):
    
    queue = []
    visited = defaultdict(bool)
    heapq.heappush(queue, (0, current, fuel))
    
    while queue:
        distance, curr, curr_fuel = heapq.heappop(queue)
        
        if curr in dests:
            new_fuel = curr_fuel + distance * 2 if refill else curr_fuel
            return curr, new_fuel, distance
        elif curr_fuel == 0:
            return curr, OUT_OF_GAS, distance
        
        x, y = curr
        for _dir in range(len(OFFSET)):
            new_x = x + OFFSET[_dir][0]
            new_y = y + OFFSET[_dir][1]
            
            if is_invalid_pos(new_x, new_y, N, N, board):
                continue
            
            if not visited[(new_x, new_y)]:
                heapq.heappush(queue, (distance +1, (new_x, new_y), curr_fuel-1))
                visited[(new_x, new_y)] = True 
    
    return (0, 0), OUT_OF_GAS, 0

def find_shortest_path(current, fuel, passengers, board, N):
    
    dests = list(map(lambda x: (x[0], x[1]), passengers))    
    curr, new_fuel, length = BFS(current, fuel, dests, board, N)
    
    if new_fuel == OUT_OF_GAS:
        return (0, 0, 0, 0), OUT_OF_GAS
    
    passenger = next(filter(lambda x: x[0:2] == curr, passengers))
        
    return passenger, new_fuel
        
'''INPUT'''

N, M, fuel = list(map(int, sys.stdin.readline().split()))
board.append([WALL for _ in range(N+1)])
for _ in range(N):
    board.append([WALL, *list(map(int, sys.stdin.readline().split()))])

start_position = tuple(map(int, sys.stdin.readline().split()))

for _ in range(M):
    line = tuple(map(int, sys.stdin.readline().split()))
    passengers.append(line)

'''COMPUTE'''
while passengers:
    next_passenger, fuel = find_shortest_path(start_position, fuel, passengers, board, N)
    if fuel == OUT_OF_GAS:
        break
    
    start_position, fuel, _ = BFS(next_passenger[:2], fuel, [next_passenger[2:]], board, N, refill=True)
    if fuel == OUT_OF_GAS:
        break
    
    passengers.remove(next_passenger)

print(fuel)
'''OUTPUT'''