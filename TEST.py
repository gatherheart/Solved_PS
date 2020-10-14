def transpose(k, N, arr):
    if k >= N:
        return
    
    index = k
    while index >= 0:
        arr[index][k], arr[k][index] = arr[k][index], arr[index][k]
        index -= 1 
    
    transpose(k+1, N, arr)

size = 4
arr = [[i*size+j for j in range(1, size+1)] for i in range(0, size)]

def print_arr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print("{:5}".format(arr[i][j]), end="")
        print()

print_arr(arr)
transpose(0, size, arr)
print_arr(arr)
