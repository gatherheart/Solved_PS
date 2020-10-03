WALL = 1
EMPTY = 0

def rotate_90(M, keys):
    new_keys = []
    
    while keys:
        i, j = keys.pop()
        new_keys.append((j, M-i-1))
        
    return new_keys

def is_solved(lock):
    return

def is_overflow(x, y, N, M):
    return x < 0 or x >= N or y < 0 or y >= M

def solution(key, lock):
    answer = False
    M, N = len(key), len(lock)
    key_cords = []
    lock_cords = []
    
    # get cords of key
    for i in range(M):
        for j in range(M):
            if key[i][j] == WALL:
                key_cords.append((i, j))
    
    # get cords of Lock
    for i in range(N):
        for j in range(N):
            if lock[i][j] == EMPTY:
                lock_cords.append((i, j))
        
    for r in range(4):
        for i in range(1-M, N):
            for j in range(1-M, N):
                start_offset = (i, j)
                new_key_cords = []
                for key_cord in key_cords:
                    new_x = key_cord[0] + start_offset[0]
                    new_y = key_cord[1] + start_offset[1]
                    if not is_overflow(new_x, new_y, N, N):
                        new_key_cords.append((new_x, new_y))
                
                new_key_cords.sort()
                if new_key_cords == lock_cords:
                    answer = True
                
        key_cords = rotate_90(M, key_cords)
    
    return answer