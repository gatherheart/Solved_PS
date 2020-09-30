''' Macro '''
# N = 0, E = 1, S = 2, W = 3
OFFSET = [[-1, 0], [0, 1], [1, 0], [0, -1]]
CLEAN = -1
BLANK = 0
WALL = 1

''' Variables '''

# (3 ≤ N, M ≤ 50)
N, M = 0, 0
curr = [0, 0]
head = 0
arr = []
found_blank = False

''' Utils '''
def print_arr(_arr, N, M):
    for i in range(N):
        for j in range(M):
            print(_arr[i][j], end=" ")
        print()

def is_overflow(curr, N, M):
    
    x = curr[0]
    y = curr[1]

    if x >= N or x < 0 or y >= M or y < 0:
        return True
    return False

def is_blank(curr, arr):
        
    x = curr[0]
    y = curr[1]

    if is_overflow([x, y], len(arr), len(arr[0])):
        raise Exception("Index Error: overflow in checking is_wall")
    if arr[x][y] == BLANK:
        return True

    return False

def is_wall(curr, arr):
    
    x = curr[0]
    y = curr[1]

    if is_overflow([x, y], len(arr), len(arr[0])):
        raise Exception("Index Error: overflow in checking is_wall")
    if arr[x][y] == WALL:
        return True

    return False


def simulation_process(curr, head, arr):
    N, M = len(arr), len(arr[0])
    # check # of cleaning
    count = 0

    while True:

        curr_x, curr_y = curr
        found_blank = False

        # 1. Clean Current Position
        if arr[curr_x][curr_y] == BLANK:
            arr[curr_x][curr_y] = CLEAN
            count += 1
        
        for dir in range(len(OFFSET)):
            # 2. Check Left Side
            # 2.a Left === BLANK -> turn Left & go foward 1 step -> go to 1
            
            # Left side head
            new_head = (head + 3) % 4
            new_x = curr[0] + OFFSET[new_head][0]
            new_y = curr[1] + OFFSET[new_head][1]

            if not is_overflow([new_x, new_y], N, M) and is_blank([new_x, new_y], arr):   
                
                curr = [new_x, new_y]
                head = new_head
                found_blank = True
                break

            # 2.b Left !== BLACK -> turn Left -> go to 2 
            else:
                head = new_head

        if found_blank: 
            continue

        # Could not find any BLANK position

        # 2.c all the directions are CLEAN or WALL -> go backward 1 step -> go to 2 (same behavior with "go to 1")
        
        new_x = curr[0] + OFFSET[(head + 2) % 4][0]
        new_y = curr[1] + OFFSET[(head + 2) % 4][1]
        curr = [new_x, new_y]

        # 2.d all the direction are CLEAN or WALL & backward position is WALL

        if is_overflow(curr, N, M) or is_wall(curr, arr):
            break
    
    return count


''' INPUT '''

N, M = input().split(" ")
N, M = int(N), int(M)
read_line = input().split(" ")
curr = list(map(lambda x: int(x), read_line[:2]))
head = int(read_line[2])

for i in range(N):
    read_line = input().split(" ")
    
    if len(read_line) != M: 
        raise Exception("Error: length of input should be same with N")

    arr.append(list(map(lambda x: int(x), read_line)))

''' COMPUTE '''

print(simulation_process(curr, head, arr))

''' OUTPUT '''