import heapq
from collections import defaultdict
def solution(stones, k):
    answer = 0
    bitmask = 0
    heap = [(remains, index) for index, remains in enumerate(stones)]
    
    disappeared = set()
    heapq.heapify(heap)
    cumulative = 0
    #print(heap)
    while heap: 
        min_stone, index = heapq.heappop(heap)
        #print(min_stone, index, cumulative)
        
        if min_stone <= cumulative:
            bitmask |= 1 << index
            
        elif min_stone > cumulative:
            cumulative += min_stone - cumulative
            bitmask |= 1 << index
            answer = cumulative

        # check 
        _bitmask = bitmask
        #print(bin(_bitmask))
        while _bitmask:
            if _bitmask & 1:
                mask = pow(2, k) - 1
                #print(bin(_bitmask), bin(mask), bin(_bitmask & mask))
                if _bitmask & mask == mask:
                    return answer
            
            _bitmask = _bitmask >> 1
            
    #print(disappeared)
        
    return answer



if __name__ == "__main__":

    test = 1
    
    if test == 1:
        stones, k = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3
    
    print(solution(stones, k))