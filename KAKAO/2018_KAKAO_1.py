SYMBOL = "#"
BLANK = " "
def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        line = arr1[i] | arr2[i]
        processed = []
        print(line, end=" ")
        while line:
            if line % 2:
                processed.append(SYMBOL)
            else:
                processed.append(BLANK)
            line = line >> 1
            print(line, end=" ")

        while len(processed) < n:
            processed.append(BLANK)
        print(processed)
        answer.append("".join(processed[::-1]))

    return answer

if __name__ == "__main__":

    n = 6
    arr1 = [46, 33, 33 ,22, 31, 50]
    arr2 = [27 ,56, 19, 14, 14, 10]


    print(solution(n, arr1, arr2))