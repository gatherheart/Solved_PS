PILLAR = 0
BEAM = 1
CREATE = 1
DELETE = 0

def check_validity(answer):
    for x, y, structure in answer:
        if structure == PILLAR:
            if y == 0 or [x, y - 1, PILLAR] in answer or \
                [x, y, BEAM] in answer or [x - 1, y, BEAM] in answer:
                continue
            else:
                return False
        else:
            if [x, y - 1, PILLAR] in answer or [x + 1, y - 1, PILLAR] in answer or \
                ([x - 1, y, BEAM] in answer and [x + 1, y, BEAM] in answer):
                continue
            else:
                return False
            
    return True

def solution(n, build_frame):
    answer = []
    
    for build in build_frame:
        x, y, structure, command = build
        
        if command == CREATE:
            answer.append([x, y, structure])
            if check_validity(answer):
                continue
            else:
                answer.pop()
        
        elif command == DELETE:
            answer.remove([x, y, structure])
            if check_validity(answer):
                continue
            else:
                answer.append([x, y, structure])
    
    answer.sort()
    return answer