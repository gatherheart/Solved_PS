from itertools import permutations
INF = 0xFFFFFFFF
def solution(n, weak, dist):
    answer = INF
    weaks = []

    for start_index in range(len(weak)):
        _weak = [weak[start_index]]
        for j in range(1, len(weak)):
            index = (start_index + j) % len(weak)

            if weak[index] < weak[start_index]:
                _weak.append(weak[index] + n)
            elif weak[index] > weak[start_index]:
                _weak.append(weak[index])
        
        weaks.append(_weak)
    
    #print(weaks)
    sorted_dist = sorted(dist, reverse=True)
    #print(sorted_dist)
    
    if n <= sorted_dist[0]:
        return 1
    
    for _weak in weaks:
        #print()
        #print("NEW WEAK", _weak)
        for new_dist in permutations(dist, len(dist)):
            #print("DIST",new_dist)
            count = 0
            new_weak = _weak[:]
            while new_weak:
                start = new_weak[0]
                end = start + new_dist[count]
                #print("start", start, "end", end, "count", count)
                while new_weak:
                    if new_weak[0] <= end:
                        new_weak.pop(0)
                    else:
                        count += 1
                        break
                    
                if count >= len(new_dist):
                    count = INF
                    break
        
            answer = min(answer, count+1)
        
    answer = -1 if answer == INF else answer
    return answer

if __name__ == "__main__":
    
    test = 3
    if test == 1:
        n = 12	
        weak = [1, 5, 6, 10]	
        dist = [1, 2, 3, 4]	
        
    elif test == 2:
        n = 12
        weak = [1, 3, 4, 9, 10]	
        dist = [3, 5, 7]
    
    elif test == 3:
        n = 12
        weak = [1, 3, 4, 9, 11]	
        dist = [1, 1, 1]   
    
    elif test == 4:
        n = 12
        weak = [1, 3, 4, 9, 11]	
        dist = [1]   
    # 3
    print(solution(n, weak, dist))
    

