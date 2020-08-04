first_line = input()
N, M = first_line.split(' ')

N, M = int(N), int(M)

'''
CASES 

1. There are no Viruses -> No cases
2. There are no more safe spaces after positioning wall
3. 

'''


SAFE_SPACE = 0
LEN_SAFE_SPACE = 0
WALL_SPACE = 1
VIRUS_SPACE = 2
DIRECTION = 4
LEN_NEW_WALL = 3
OFFSET = [[-1, 0], [0, 1], [1, 0], [0, -1]]
# array N X M

arr = []
safe_spaces = []
wall_spaces = []
virus_spaces = []

''' INPUT '''
for i in range(N):
    _input_line = input().split(' ')
    _line = []
    for index, x in enumerate(_input_line):
        _x = int(x)
        
        # Save coordintates
        if _x == SAFE_SPACE:
            safe_spaces.append((i, index))
            LEN_SAFE_SPACE += 1
        elif _x == WALL_SPACE:
            wall_spaces.append((i, index))
        elif _x == VIRUS_SPACE:
            virus_spaces.append((i, index))

        _line.append(_x)

    arr.append(_line)
    
''' COMPUTE '''
def print_arr(_arr, N, M):
    for i in range(N):
        for j in range(M):
            print(_arr[i][j], end=" ")
        print()
 
def after_contagion(arr, N, M):
    queue = []
    count = 0
    # Deep Copy
    _arr = [row[:] for row in arr]

    # Using BFS for each virus position
    for _virus in virus_spaces:
    
        queue.append(_virus)

        while queue:
            i, j = queue.pop(0)
            for d in range(DIRECTION):
                new_i = i + OFFSET[d][0]
                new_j = j + OFFSET[d][1]
                
                # Pass overflow 
                if new_i >= N or new_i < 0 or new_j >= M or new_j < 0:
                    continue

                if _arr[new_i][new_j] == SAFE_SPACE:
                    _arr[new_i][new_j] = VIRUS_SPACE
                    
                    queue.append((new_i, new_j))
                    count += 1

    return count


MAX_CONTAGION_SPACES = after_contagion(arr, N, M)

# MINIMUM CONTAIGION SPACE
min_count = 0xfffe

for i in range(LEN_SAFE_SPACE):
    for j in range(i, LEN_SAFE_SPACE):
        for k in range(j, LEN_SAFE_SPACE):
            # Get New Copied array 
            _arr = [row[:] for row in arr]
            
            # Get safe spaces to position walls
            wall_1, wall_2, wall_3 = safe_spaces[i], safe_spaces[j], safe_spaces[k]
            
            _arr[wall_1[0]][wall_1[1]] = WALL_SPACE
            _arr[wall_2[0]][wall_2[1]] = WALL_SPACE
            _arr[wall_3[0]][wall_3[1]] = WALL_SPACE
            
            ret = after_contagion(_arr, N, M)
            if min_count > ret:
                min_count = ret


''' OUTPUT '''
print(LEN_SAFE_SPACE, min_count, LEN_NEW_WALL)
print(LEN_SAFE_SPACE - min_count - LEN_NEW_WALL)