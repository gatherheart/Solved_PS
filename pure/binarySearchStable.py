def binary_search(x, arr): 
    
    left, right = 0, len(arr) - 1
    answer = 0
    while left <= right:
        
        mid = (left + right) // 2
        print(left, right, mid, arr[mid])
        if arr[mid][0] < x:

            left = mid + 1
            
        elif arr[mid][0] >= x:
            answer = mid
            right = mid - 1
            
    
    print(left, right)    
    return answer


arr = [(1, 1), (3, 1), (4, 1), (5, 1), (10, 1), (10, 2), (10, 3), (12, 1), (12, 2), (24, 1)]
find = 10

print(arr[binary_search(find, arr)])