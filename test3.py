def binary_search(x, arr): 
    
    left, right = 0, len(arr) - 1
    answer = 0
    while left <= right:
        
        mid = (left + right) // 2
        
        if arr[mid] <= x:
            answer = mid
            left = mid + 1
            
        elif arr[mid] > x:
            right = mid - 1
        
    return answer


test = [1, 2, 2, 2, 2, 4, 5, 6, 7]

print(binary_search(3, test))