

def rotate_90_right(x, y, N, M):
    return y, N - 1 - x,

def rotate_90_left(x, y, N, M):
    # (0, 0) => (2, 0)
    # (0, 2) => (0, 0)
    # (1, 2) => (0, 1)
    return N - 1 - y, x 

def rotate_180_right(x, y, N, M):
    # (0, 0) => (2, 2)
    # (0, 1) => (2, 1)
    # (1, 0) => (1, 2)
    # (2, 1) => (0, 1)
    return N - 1 - x, N - 1 - y

def rotate_180_left(x, y, N, M):
    return rotate_180_right(x, y, N, M)

def rotate_270_right(x, y, N, M):
    return rotate_90_left(x, y, N, M)

for i in range(3):
    for j in range(2):
        print(rotate_90_right(i, j, 3, 2))