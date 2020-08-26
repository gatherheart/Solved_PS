def rotate_90(M, key):
    ret = [[0 for _ in range(M)] for i in range(M)]

    for i in range(M):
        for j in range(M):
            ret[j][M-i-1] = key[i][j]

    return ret

test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(rotate_90(len(test), test))
