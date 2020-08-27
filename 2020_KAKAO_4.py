PILLAR = 0
BEAM = 1
CREATE = 1
DELETE = 0

def check_build_validity(x, y, structure, answer):

    if structure == PILLAR:
        if y == 0 or [x, y - 1, PILLAR] in answer or \
            [x, y, BEAM] in answer or [x - 1, y, BEAM] in answer:
            return True
        else:
            return False
    else:
        if [x, y - 1, PILLAR] in answer or [x + 1, y - 1, PILLAR] in answer or \
            ([x - 1, y, BEAM] in answer and [x + 1, y, BEAM] in answer):
            return True
        else:
            return False
            
    return True

def check_delete_validity(x, y, structure, answer):

    if structure == PILLAR:
        checks = [[x, y + 1, PILLAR], [x - 1, y + 1, BEAM], [x, y + 1, BEAM]]
        
    else:
        checks = [[x + 1, y, PILLAR], [x, y, PILLAR], [x - 1, y, BEAM], [x + 1, y, BEAM]]
    
    for check in checks:
        _x, _y, _structure = check

        if not check in answer:
            continue
        if _structure == PILLAR:
            if _y == 0 or [_x, _y - 1, PILLAR] in answer or \
                [_x, _y, BEAM] in answer or [_x - 1, _y, BEAM] in answer:
                continue
            else:
                return False
        else:
            if [_x, _y - 1, PILLAR] in answer or [_x + 1, _y - 1, PILLAR] in answer or \
                ([_x - 1, _y, BEAM] in answer and [_x + 1, _y, BEAM] in answer):
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
            if check_build_validity(x, y, structure, answer):
                continue
            else:
                answer.pop()
        
        elif command == DELETE:
            answer.remove([x, y, structure])
            if check_delete_validity(x, y, structure, answer):
                continue
            else:
                answer.append([x, y, structure])
    
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