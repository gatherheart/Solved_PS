import heapq
from collections import defaultdict
def solution(stones, k):
    answer = 0
    
    heap = [(remains, index) for index, remains in enumerate(stones)]
    
    disappeared = set()
    heapq.heapify(heap)
    cumulative = 0
    #print(heap)
    while heap:
        min_stone, index = heapq.heappop(heap)
        #print(min_stone, index, cumulative)
        
        if min_stone <= cumulative:
            disappeared.add(index)
        
        elif min_stone > cumulative:
            cumulative += min_stone - cumulative
            disappeared.add(index)
            answer = cumulative

        
        disappeared_connected = True
        for key in disappeared:
            disappeared_connected = True
            #print("KEY", key, end=" ")
            for next_key in range(key+1, key+k):
                #print(next_key, end=" ")
                if not next_key in disappeared:
                    disappeared_connected = False
                    break
            #print(disappeared_connected)
            if disappeared_connected:
                break
        if disappeared_connected:
            break
    #print(disappeared)
        
    return answer



if __name__ == "__main__":

    test = 1
    
    if test == 1:
        stones, k = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3
    
    print(solution(stones, k))