PILLAR = 0
BEAM = 1
DELETE = 0
CREATE = 1

def is_safe(command, frames):
    x, y, which, how = command
    ret = False
    
    if how == DELETE:
        frames.remove((x, y, which))
    
    if which == PILLAR:
        if how == CREATE:
            ret = y == 0 or (x, y, BEAM) in frames or \
                (x-1, y, BEAM) in frames or (x, y-1, PILLAR) in frames 
        elif how == DELETE:
            ret = True
            if (x, y+1, PILLAR) in frames:
                ret = ret & is_safe((x, y+1, PILLAR, CREATE), frames)
            
            if (x, y+1, BEAM) in frames:
                ret = ret & is_safe((x, y+1, BEAM, CREATE), frames)
                
            if (x-1, y+1, BEAM) in frames:
                ret = ret & is_safe((x-1, y+1, BEAM, CREATE), frames)
            
    elif which == BEAM:
        if how == CREATE:
            ret = (x, y-1, PILLAR) in frames or \
                (x+1, y-1, PILLAR) in frames or \
                ((x-1, y, BEAM) in frames and (x+1, y, BEAM) in frames)
        elif how == DELETE:
            ret = True
            if (x, y, PILLAR) in frames:
                ret = ret & is_safe((x, y, PILLAR, CREATE), frames)
            
            if (x+1, y, PILLAR) in frames:
                ret = ret & is_safe((x+1, y, PILLAR, CREATE), frames)
                
            if (x-1, y, BEAM) in frames:
                ret = ret & is_safe((x-1, y, BEAM, CREATE), frames)
                
            if (x+1, y, BEAM) in frames:
                ret = ret & is_safe((x+1, y, BEAM, CREATE), frames)
                    
    if how == DELETE:
        frames.append((x, y, which))
    
    return ret


def solution(n, build_frame):
    answer = []
    
    for command in build_frame:
        if is_safe(command, answer):
            x, y, which, how = command
            #print("COMMAND", command, "SAFE")
            #print(answer)
            if how == CREATE:
                answer.append((x, y, which))
    
            elif how == DELETE:
                answer.remove((x, y, which))

    return sorted(answer)

if __name__ == '__main__':
    test = 3
    
    if test == 1:
        n, build_frame = 5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]	
    
    if test == 2:
        n, build_frame = 5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,2,0,1]]	
    
    if test == 3:
        n, build_frame = 5, [[0, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 0, 0, 1], [1, 1, 1, 1], [1, 1, 0, 1]]	
    
    print(solution(n, build_frame))