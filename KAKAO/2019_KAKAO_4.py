# 무지의 먹방 라이브

import heapq

def solution(food_times, k):
    answer = -1
    remains = list(map(lambda x: (x[1], x[0]+1), enumerate(food_times)))
    heapq.heapify(remains)
    removed_foods = 0
    
    while remains:
        
        min_food, current = remains[0]
        len_of_remains = len(remains)
        #print(remains)
        #print(k, len_of_remains, min_food)
        
        min_food -= removed_foods
        
        if k < min_food * len_of_remains:
            remains.sort(key=lambda x: x[1])
            return remains[k % len_of_remains][1]
    
        k = k - min_food * len_of_remains
        removed_foods += min_food
        heapq.heappop(remains)
        
        #print("Removed", remains, k, min_food)
    
    return answer


if __name__ == "__main__":

    test = 1
    
    if test == 1:
        food_times, k = [1, 2, 2], 3

    if test == 2:
        food_times, k = [7, 6, 5], 5

    if test == 3:
        food_times, k = [3, 1, 2], 5

    print(solution(food_times, k))
