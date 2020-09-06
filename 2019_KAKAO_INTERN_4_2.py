from collections import deque

def solution(stones, k):
    window = deque(stones[0:k])
    max_window = 0
    second_max = 0
    
    for w in window:
        if max_window < w:
            max_window = w
    
    answer = max_window
    
    for i in range(k, len(stones)):
        print("CURR", max_window, second_max)
        print(window)
        left = window.popleft()
        window.append(stones[i])
        
        if left == max_window:
            max_window = max(window)
            answer = min(answer, max_window)
            
    return answer


if __name__ == "__main__":

    test = 1
    
    if test == 1:
        stones, k = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3
    
    print(solution(stones, k))