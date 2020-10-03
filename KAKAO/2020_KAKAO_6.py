from itertools import permutations

def solution(n, weak, dist):
    
    weaks = []
    count = -1
    for i in range(len(weak)):
        _weak = weak[:]
        for j in range(i, len(weak) - 1):
            top = _weak.pop(0)
            _weak.append(top + n)
        
        weaks.append(_weak)
    
    dist.sort(reverse=True)
    weaks.sort()
    #print(weaks)
    
    for num in range(1, len(dist)+1):
        for perm in permutations(dist, num):
            for _weak in weaks:
                start = _weak[0]
                for step in perm:
                    new_pos = start + step
                    _weak = _weak[:]
                    while _weak:
                        if _weak[0] <= new_pos:
                            _weak.pop(0)
                        else:
                            break
                    #print("new", new_pos, "start", start, "step: ", step, "weak", _weak)
                    if not _weak:
                        count = len(perm)
                        break
                    start = _weak[0]
                    
                #print("perm", perm, "stepped", _weak)

                if count != -1:
                    break
            if count != -1:
                break
        if count != -1:
            break

    return count

if __name__ == "__main__":
    n = 12	
    weak = [1, 5, 6, 10]	
    dist = [1, 2, 3, 4]	
    # 3
    print(solution(n, weak, dist))
    

