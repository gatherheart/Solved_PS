from collections import defaultdict
# [3차] 압축


def char_to_index(ch):
    return ord(ch) - ord('A') + 1
 
def binary_search(indexes, msg):
    
    left, right = 0, len(msg) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if indexes[msg[:mid+1]]:
            left = mid + 1
        else:
            right = mid - 1
    
    return left

def solution(msg):
    answer = []
    indexes = defaultdict(int)
    last_index = 27
    for i in range(26):
        indexes[chr(ord('A')+i)] = i + 1
        
    padded_msg = msg[1:] + " "

    i = 0    
    while i < len(msg):
        
        w_index = binary_search(indexes, msg[i:])
        w = msg[i:i+w_index]
        answer.append(indexes[w])
        
        if i + w_index < len(msg) and not indexes[w+msg[i+w_index]]:
            indexes[w+msg[i+w_index]] = last_index
            last_index += 1

        i = i + w_index
    
    return answer

if __name__ == "__main__":

    test = 3
    
    if test == 1:
        msg = "KAKAO"
        
    if test == 2:
        msg = "TOBEORNOTTOBEORTOBEORNOT"
    
    if test == 3:
        msg = "ABABABABABABABAB"
        
    print(solution(msg))
