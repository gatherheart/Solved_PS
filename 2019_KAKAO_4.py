# 무지의 먹방 라이브

from collections import deque

def solution(food_times, k):
    answer = -1
    remains = deque(list(map(lambda x: (x[1], x[0]+1), enumerate(food_times))))

    while remains:
        min_food, _ = min(remains)
        len_of_remains = len(remains)
        #print(remains)
        #print(k, len_of_remains, min_food)
        
        if k < min_food * len_of_remains:
            return remains[k % len_of_remains][1]
    
        k = k - min_food * len_of_remains
        for i in range(len_of_remains):
            food, index = remains.popleft()
            food -= min_food
            if food != 0:
                remains.append((food, index))
        
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
