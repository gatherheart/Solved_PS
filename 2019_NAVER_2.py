from collections import defaultdict, deque

OFFSET = [[-1, 0], [0, 1], [1, 0], [0, -1]]
EMPTY = "."

def print_arr(_arr, N, M):
    for i in range(N):
        for j in range(M):
            print(_arr[i][j], end=" ")
        print()

def is_overflow(x, y, M, N):
    return x < 0 or y < 0 or x >= M or y >= N

def solution(maps):
    
    M, N = len(maps), len(maps[0])
    new_maps = []
    attached = defaultdict(set)
    
    for _map in maps:
        new_maps.append(list(_map))
            
    for i in range(M):
        for j in range(N):
            if new_maps[i][j] == EMPTY:
                continue    
            
            # start BFS
            nation = new_maps[i][j]
            queue = deque([(i, j)])
            visited = defaultdict(bool)
            visited[(i, j)] = True
            new_maps[i][j] = EMPTY

            while queue:
                
                x, y = queue.popleft()
                
                for _dir in range(len(OFFSET)):
                    new_x = x + OFFSET[_dir][0]
                    new_y = y + OFFSET[_dir][1]
    
                    if is_overflow(new_x, new_y, M, N) or \
                        new_maps[new_x][new_y] == EMPTY:
                        continue
                    
                    if nation != new_maps[new_x][new_y]:
                        nation_key, nation_val = sorted([nation, new_maps[new_x][new_y]])
                        attached[nation_key].add(nation_val)
                        continue
                    
                    if not visited[(new_x, new_y)]:
                        queue.append((new_x, new_y))
                        visited[(new_x, new_y)] = True
                        new_maps[x][y] = EMPTY
    
    
    max_attached = 0
    count = 0
    
    for _key in attached:
        max_attached = max(max_attached, len(attached[_key]))
        count += len(attached[_key])
    
    return [count, max_attached]

if __name__ == "__main__":

    test = 1
    
    if test == 1:
        maps = ["..........","AAACC.....",".AAA.....Z","..AAAA..C.","...BBBBB..","....BBB...","...ZBBB...","ZZZZAAAC..",".....CCCC.","QQ......C.",".........."]	

    if test == 2:
        maps = ["A.B.C.D", ".B.C.D."]
        
    print(solution(maps))
