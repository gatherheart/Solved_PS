
def is_safe(stones, removal, k):
    
    num_disappeard = 0
    for stone in stones:
        if stone - removal < 0:
            num_disappeard += 1
            if num_disappeard == k:
                return False
        else:
            num_disappeard = 0
            
    return True

def solution(stones, k):
    answer = 0
    left, right = 0, max(stones) + 1
        
    while left <= right:
        
        mid = (left + right) // 2
        if is_safe(stones, mid, k):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return answer


if __name__ == "__main__":

    test = 1
    
    if test == 1:
        stones, k = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3
    
    print(solution(stones, k))