import sys

WHITE = 'w'
YELLOW = 'y'
RED = 'r'
ORANGE = 'o'
GREEN = 'g'
BLUE = 'b'
RIGHT = '+'
LEFT = '-'

class Cube:
    def __init__(self) -> None:
        self.cube = {
        'U' : [None, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
        'D' : [None, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW], 
        'F' : [None, RED, RED, RED, RED, RED, RED, RED, RED, RED],
        'B' : [None, ORANGE, ORANGE, ORANGE, ORANGE, ORANGE, ORANGE, ORANGE, ORANGE, ORANGE],
        'L' : [None, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN],
        'R' : [None, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE], 
        }
        self.neighrbors = {
        'U' : ['B', 'R', 'F', 'L'],
        'D' : ['B', 'L', 'F', 'R'],
        'F' : ['U', 'R', 'D', 'L'],
        'B' : ['U', 'L', 'D', 'R'],
        'L' : ['U', 'F', 'D', 'B'],
        'R' : ['U', 'B', 'D', 'F'],
        }
        
    def rotate_neighbors(self, side, direction):
        
        c = self.cube
        if side == 'U':
            if direction == RIGHT:
                c['B'][7], c['R'][1], c['F'][3], c['L'][9] =\
                     c['L'][9], c['B'][7], c['R'][1], c['F'][3]
                c['B'][8], c['R'][4], c['F'][2], c['L'][6] =\
                     c['L'][6], c['B'][8], c['R'][4], c['F'][2]
                c['B'][9], c['R'][7], c['F'][1], c['L'][3] =\
                     c['L'][3], c['B'][9], c['R'][7], c['F'][1]
                
            else:
                c['B'][7], c['R'][1], c['F'][3], c['L'][9] =\
                     c['R'][1], c['F'][3], c['L'][9], c['B'][7]
                c['B'][8], c['R'][4], c['F'][2], c['L'][6] =\
                     c['R'][4], c['F'][2], c['L'][6], c['B'][8]        
                c['B'][9], c['R'][7], c['F'][1], c['L'][3] =\
                     c['R'][7], c['F'][1], c['L'][3], c['B'][9]
                
        if side == 'R':
            if direction == RIGHT:
                c['B'][9], c['D'][1], c['F'][9], c['U'][9] =\
                    c['U'][9], c['B'][9], c['D'][1], c['F'][9]
                c['B'][6], c['D'][4], c['F'][6], c['U'][6] =\
                    c['U'][6], c['B'][6], c['D'][4], c['F'][6]
                c['B'][3], c['D'][7], c['F'][3], c['U'][3] =\
                    c['U'][3], c['B'][3], c['D'][7], c['F'][3]
            
            else:
                c['B'][9], c['D'][1], c['F'][9], c['U'][9] =\
                    c['D'][1], c['F'][9], c['U'][9], c['B'][9]
                c['B'][6], c['D'][4], c['F'][6], c['U'][6] =\
                    c['D'][4], c['F'][6], c['U'][6], c['B'][6]
                c['B'][3], c['D'][7], c['F'][3], c['U'][3] =\
                    c['D'][7], c['F'][3], c['U'][3], c['B'][3]
        
        if side == 'F':
            if direction == RIGHT:
                c['U'][7], c['R'][7], c['D'][7], c['L'][7] =\
                    c['L'][7], c['U'][7], c['R'][7], c['D'][7]
                c['U'][8], c['R'][8], c['D'][8], c['L'][8] =\
                    c['L'][8], c['U'][8], c['R'][8], c['D'][8]
                c['U'][9], c['R'][9], c['D'][9], c['L'][9] =\
                    c['L'][9], c['U'][9], c['R'][9], c['D'][9]
            else:
                c['U'][7], c['R'][7], c['D'][7], c['L'][7] =\
                    c['R'][7], c['D'][7], c['L'][7], c['U'][7]
                c['U'][8], c['R'][8], c['D'][8], c['L'][8] =\
                    c['R'][8], c['D'][8], c['L'][8], c['U'][8]
                c['U'][9], c['R'][9], c['D'][9], c['L'][9] =\
                    c['R'][9], c['D'][9], c['L'][9], c['U'][9]
                
        if side == 'D':
            if direction == RIGHT:
                c['B'][3], c['L'][1], c['F'][7], c['R'][9] =\
                    c['R'][9], c['B'][3], c['L'][1], c['F'][7]
                c['B'][2], c['L'][4], c['F'][8], c['R'][6] =\
                    c['R'][6], c['B'][2], c['L'][4], c['F'][8]
                c['B'][1], c['L'][7], c['F'][9], c['R'][3] =\
                    c['R'][3], c['B'][1], c['L'][7], c['F'][9]
            else:
                c['B'][3], c['L'][1], c['F'][7], c['R'][9] =\
                    c['L'][1], c['F'][7], c['R'][9], c['B'][3]
                c['B'][2], c['L'][4], c['F'][8], c['R'][6] =\
                    c['L'][4], c['F'][8], c['R'][6], c['B'][2]
                c['B'][1], c['L'][7], c['F'][9], c['R'][3] =\
                    c['L'][7], c['F'][9], c['R'][3], c['B'][1]
                
        if side == 'B':
            if direction == RIGHT:
                c['D'][3], c['R'][3], c['U'][3], c['L'][3] =\
                    c['L'][3], c['D'][3], c['R'][3], c['U'][3]
                c['D'][2], c['R'][2], c['U'][2], c['L'][2] =\
                    c['L'][2], c['D'][2], c['R'][2], c['U'][2]
                c['D'][1], c['R'][1], c['U'][1], c['L'][1] =\
                    c['L'][1], c['D'][1], c['R'][1], c['U'][1]
            else:
                c['D'][3], c['R'][3], c['U'][3], c['L'][3] =\
                    c['R'][3], c['U'][3], c['L'][3], c['D'][3]
                c['D'][2], c['R'][2], c['U'][2], c['L'][2] =\
                    c['R'][2], c['U'][2], c['L'][2], c['D'][2]
                c['D'][1], c['R'][1], c['U'][1], c['L'][1] =\
                    c['R'][1], c['U'][1], c['L'][1], c['D'][1]
        
        if side == 'L':
            if direction == RIGHT:
                c['B'][1], c['U'][1], c['F'][1], c['D'][9] =\
                    c['D'][9], c['B'][1], c['U'][1], c['F'][1]
                c['B'][4], c['U'][4], c['F'][4], c['D'][6] =\
                    c['D'][6], c['B'][4], c['U'][4], c['F'][4]
                c['B'][7], c['U'][7], c['F'][7], c['D'][3] =\
                    c['D'][3], c['B'][7], c['U'][7], c['F'][7]
            else:
                c['B'][1], c['U'][1], c['F'][1], c['D'][9] =\
                    c['U'][1], c['F'][1], c['D'][9], c['B'][1]
                c['B'][4], c['U'][4], c['F'][4], c['D'][6] =\
                    c['U'][4], c['F'][4], c['D'][6], c['B'][4]
                c['B'][7], c['U'][7], c['F'][7], c['D'][3] =\
                    c['U'][7], c['F'][7], c['D'][3], c['B'][7]

    def rotate_itself(self, side, direction):
        c = self.cube
        if direction == RIGHT:
            c[side][1], c[side][2], c[side][3], c[side][4],\
            c[side][6], c[side][7], c[side][8], c[side][9] =\
                c[side][7], c[side][4], c[side][1], c[side][8], c[side][2], c[side][9], c[side][6], c[side][3]
        else:
            c[side][1], c[side][2], c[side][3], c[side][4],\
            c[side][6], c[side][7], c[side][8], c[side][9] =\
                c[side][3], c[side][6], c[side][9], c[side][2], c[side][8], c[side][1], c[side][4], c[side][7]
                
    def print_cube(self, sides):
        for side in sides:
            for i in range(3):
                for j in range(1, 4):
                    print("{}".format(self.cube[side][i * 3 + j]), end="")
                print()
        

T = int(sys.stdin.readline())

for _ in range(T):
    cube = Cube()
    n = int(sys.stdin.readline())
    comd = list(sys.stdin.readline().split())
    for c in comd:
        side, direction = list(c)
        cube.rotate_neighbors(side, direction)
        cube.rotate_itself(side, direction)
    
    cube.print_cube(['U'])