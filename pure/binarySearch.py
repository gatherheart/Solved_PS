
def binary_search_recursive(left, right, x, arr):
    
    print("LEFT", left, "RIGHT",right)
    
    if left > right:
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
    answer = 0
    while left <= right:
        
        mid = (left + right) // 2
        
        if arr[mid] <= x:
            answer = mid
            left = mid + 1
            
        elif arr[mid] > x:
            right = mid - 1
            
    
    return answer
    

arr = [1, 3, 4, 5, 10, 12, 15, 20, 24, 0XFFFFF]
find = 28

print(arr[binary_search_recursive(0, len(arr)-1, find, arr)])
print()
print(arr[binary_search(find, arr)])
