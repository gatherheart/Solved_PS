import sys 
from collections import deque, defaultdict
'''CONSTANTS'''
EMPTY = "."
WALL = "#"
RED = "R"
BLUE = 'B'
GOAL = 'O'
OFFSET = [[-1, 0], [0, 1], [1, 0], [0, -1]]

'''VARIABLES'''
N, M = 0, 0
board = []
red, blue, goal = None, None, None

'''UTILS'''

def BFS(red, blue, goal, N, M, board):
    
    queue = deque([(red, blue, 0)])
    visited = defaultdict(bool)
    board[red[0]][red[1]] = EMPTY
    board[blue[0]][blue[1]] = EMPTY
    
    while queue:
        current_red, current_blue, distance = queue.popleft()
        red_x, red_y = current_red
        blue_x, blue_y = current_blue
            
        if red_x == goal[0] and red_y == goal[1]:
            return distance
        elif distance > 10:
            return -1 
            
        if visited[(current_red, current_blue)]:
            continue
    
        #print(current_red, current_blue, distance)

        visited[(current_red, current_blue)] = True
        
        for _dir in range(len(OFFSET)):
            new_red_x, new_red_y = red_x, red_y
            new_blue_x, new_blue_y = blue_x, blue_y
            prev_red, prev_blue = current_red, current_blue
            
            while board[new_red_x][new_red_y] == EMPTY and \
                not (new_red_x, new_red_y) == prev_blue:
                prev_red = (new_red_x, new_red_y)
                new_red_x = new_red_x + OFFSET[_dir][0]
                new_red_y = new_red_y + OFFSET[_dir][1]
            
            while board[new_blue_x][new_blue_y] == EMPTY and \
                not (new_blue_x, new_blue_y) == prev_red:
                prev_blue = (new_blue_x, new_blue_y)
                new_blue_x = new_blue_x + OFFSET[_dir][0]
                new_blue_y = new_blue_y + OFFSET[_dir][1]
                
            while board[new_red_x][new_red_y] == EMPTY and \
                not (new_red_x, new_red_y) == prev_blue:
                prev_red = (new_red_x, new_red_y)
                new_red_x = new_red_x + OFFSET[_dir][0]
                new_red_y = new_red_y + OFFSET[_dir][1]
                
            #print("DIR", _dir, (new_red_x, new_red_y), (new_blue_x, new_blue_y))
            if board[new_red_x][new_red_y] == WALL and \
                board[new_blue_x][new_blue_y] == WALL:
                    queue.append((prev_red, prev_blue, distance+1))
            
            elif board[new_red_x][new_red_y] == WALL and \
                (new_blue_x, new_blue_y) == prev_red:
                    queue.append((prev_red, prev_blue, distance+1))
            
            elif board[new_blue_x][new_blue_y] == WALL and \
                (new_red_x, new_red_y) == prev_blue:
                    queue.append((prev_red, prev_blue, distance+1))
                
            elif board[new_red_x][new_red_y] == GOAL and \
                board[new_blue_x][new_blue_y] == WALL:
                    queue.append(((new_red_x, new_red_y), prev_blue,
                                 distance+1))
                    
    return -1


'''INPUT'''

N, M = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    line = list(sys.stdin.readline().strip())
    board.append(line)
    for j, c in enumerate(line):
        if c == RED:
            red = (i, j)
        
        elif c == BLUE:
            blue = (i, j)
            
        elif c == GOAL:
            goal = (i, j)

'''COMPUTE'''

print(BFS(red, blue, goal, N, M, board))

'''OUTPUT'''

'''
CASE 


5 5
#####
#RB.#
#..##
#.O.#
#####

5 5
#####
#R#.#
#B#.#
#O..#
#####


10 10
##########
#R#B.....#
#...#.##.#
#####.##.#
#......#.#
#.######.#
#.#...O#.#
#.#.##...#
#...#....#
##########

'''