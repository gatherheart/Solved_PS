def solution(A):
    answer = 1
    A = list(set(filter(lambda x: x > 0, A)))
    A.sort()
    for i in A:
        if answer == i:
            answer += 1
        else:
            break
        
    return answer
    
    
A = [1, 3, 6, 4, 1, 2]
A = [-1, -3]
print(solution(A))