BEAM = 1
PILLAR = 0
BEAM_AND_PILLAR = 2
EMPTY = -1
CREATE = 1
DELETE = 0

def print_arr(_arr, N, M):
    for i in range(N):
        for j in range(M):
            print("{:3}".format(_arr[i][j]), end=" ")
        print()

def is_overflow(x, y, N, M):
    return x < 0 or x >= N or y < 0 or y >= M
    
def is_safe(x, y, structure, command, n, arr):
    
    if structure == BEAM:
        return is_safe_for_beam(x, y, command, n, arr)
    elif structure == PILLAR:
        return is_safe_for_pillar(x, y, command, n, arr)
    
    return False

def is_safe_for_beam(x, y, command, n, arr):
    
    if command == CREATE:
        
        # Check under whether there is a pillar 
        if arr[y - 1][x] == PILLAR or arr[y - 1][x] == BEAM_AND_PILLAR:
            return True
        
        # check right under whether there is a pillar or not
        if arr[y - 1][x + 1] == PILLAR or arr[y - 1][x + 1] == BEAM_AND_PILLAR:
            return True
        
        # Check Both side Wether there are beams
        if (not is_overflow(x - 1, y, n, n) and not is_overflow(x + 1, y, n, n)) and \
            arr[y][x - 1] >= BEAM and arr[y][x + 1] >= BEAM:
            return True
        
    elif command == DELETE:
        # check right and current and up
        tmp = arr[y][x] 
        build_structure(x, y, BEAM, DELETE, n, arr)
        ret = True

        # Check Left Beam
        if not is_overflow(x - 1, y, n, n) and arr[y][x - 1] >= BEAM:
            ret = ret & is_safe_for_beam(x - 1, y, CREATE, n, arr)
        
        # Check Right Beam
        if not is_overflow(x + 1, y, n, n) and arr[y][x + 1] >= BEAM:
            ret = ret & is_safe_for_beam(x + 1, y, CREATE, n, arr)

        # Check current Pillar
        if arr[y][x] == PILLAR or arr[y][x] == BEAM_AND_PILLAR:
            ret = ret & is_safe_for_pillar(x, y, CREATE, n, arr)

        # Check Right Pillar
        if not is_overflow(x + 1, y, n, n) and \
            (arr[y][x + 1] == PILLAR or arr[y][x + 1] == BEAM_AND_PILLAR):
            ret = ret & is_safe_for_pillar(x + 1, y, CREATE, n, arr)

        arr[y][x] = tmp
        return ret 
    
    return  False

def is_safe_for_pillar(x, y, command, n, arr):
    
    if command == CREATE:

        # is_floor
        if y == 0:
            return True
        # is on other pillar
        if arr[y - 1][x] == PILLAR or arr[y - 1][x] == BEAM_AND_PILLAR:
            return True
        # is end of left beam
        if not is_overflow(x - 1, y, n, n) and arr[y][x - 1] >= BEAM:
            return True
        # is on a beam
        if arr[y][x] == BEAM or arr[y][x] == BEAM_AND_PILLAR:
            return True
        
    elif command == DELETE:
        tmp = arr[y][x]
        build_structure(x, y, PILLAR, DELETE, n, arr)
        ret = True

        # Check Pillar dependant on this pillar
        if not is_overflow(x, y + 1, n, n) and \
             (arr[y + 1][x] == PILLAR or arr[y + 1][x] == BEAM_AND_PILLAR):
            ret = ret & is_safe_for_pillar(x, y + 1, CREATE, n, arr)

        # Check up right Beam dependant on this pillar
        if not is_overflow(x, y + 1, n, n) and \
            arr[y + 1][x] >= BEAM:
            ret = ret & is_safe_for_beam(x, y + 1, CREATE, n, arr)

        # Check up left Beam dependant on this pillar
        if not is_overflow(x - 1, y + 1, n, n) and \
            arr[y + 1][x - 1] >= BEAM:
            ret = ret & is_safe_for_beam(x - 1, y + 1, CREATE, n, arr)

        arr[y][x] = tmp
        return ret
        
    return False 

def build_structure(x, y, structure, command, n, arr):
    
    if structure == PILLAR and command == CREATE:
        arr[y][x] = PILLAR if arr[y][x] == EMPTY else BEAM_AND_PILLAR
    elif structure == PILLAR and command == DELETE:
        arr[y][x] = EMPTY if arr[y][x] == PILLAR else BEAM
    elif structure == BEAM and command == CREATE:
        arr[y][x] = BEAM if arr[y][x] == EMPTY else BEAM_AND_PILLAR
    elif structure == BEAM and command == DELETE:
        arr[y][x] = EMPTY if arr[y][x] == BEAM else PILLAR
    
def solution(n, build_frame):
    answer = []
    arr = [[EMPTY for j in range(n + 1)] for i in range(n + 1)]
    
    for build in build_frame:
        x, y, structure, command = build
    
        if is_safe(x, y, structure, command, n + 1, arr):
            build_structure(x, y, structure, command, n + 1, arr)
        

    for i in range(n + 1):
        for j in range(n + 1):
            if arr[i][j] == PILLAR:
                answer.append([j, i, PILLAR])
            elif arr[i][j] == BEAM:
                answer.append([j, i, BEAM])
            elif arr[i][j] == BEAM_AND_PILLAR:
                answer.append([j, i, PILLAR])
                answer.append([j, i, BEAM])
    
    answer.sort()
    return answer


if __name__ == '__main__':
    a = [
        5,
    ]
    b = [
        [[1, 0, 0, 1], [4, 0, 0, 1], [1, 1, 1, 1], [3, 1, 1, 1], [2, 1, 1, 1], [3, 1, 0, 1], [3, 0, 0, 1], [2, 1, 1, 0], [3, 1, 1, 0]]
    ]
    for x, y in zip(a, b):
        print(solution(x, y))