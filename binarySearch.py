def binary_search_recursive(left, right, x, arr):
    
    print("LEFT", left, "RIGHT",right)
    
    if left + 1 >= right:
        print("RET", left, right)
        return left
    
    mid = (left + right) // 2
    print("MID", mid)
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        left = mid + 1
    elif arr[mid] > x:
        right = mid - 1
        
    return binary_search_recursive(left, right, x, arr)



def binary_search(x, arr): 
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        
        mid = (left + right) // 2
        
        if arr[mid] == x:
            return mid
        
        elif arr[mid] < x:
            left = mid + 1
            
        elif arr[mid] > x:
            right = mid - 1
            
    
    return left
    

arr = [1, 3, 4, 5, 10, 12, 15, 20, 24]
find = 0

print(binary_search_recursive(0, len(arr)-1, find, arr))
print()
print(binary_search(find, arr))
