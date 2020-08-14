import sys
 
N,M=map(int,sys.stdin.readline().split())
 
map=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
 
 
 
 
result=[[0 for _ in range(M)] for _ in range(N)]
result[0][0]=1
 
 
 
for i in range(N):
    if i==0:
        for j in range(1,M):#첫줄 처리 오른쪽으로만 확인하고 중간에 끊어지면 끝
            if map[i][j-1]>map[i][j]:
                result[i][j]+=result[i][j-1]
            else:
                break
 
    else:
        for d in range(M):#아래로 이동하면서 비교
            if map[i][d]<map[i-1][d]:
                result[i][d]+=result[i-1][d]
        for r in range(1,M):#우로 이동하면서 비교
            if map[i][r - 1] > map[i][r]:
                result[i][r] += result[i][r - 1]
        for l in range(M-1,0,-1):#좌로 이동하면서 비교
            if map[i][l]>map[i][l-1]:
                result[i][l-1]+=result[i][l]
 
print(result[-1][-1])
