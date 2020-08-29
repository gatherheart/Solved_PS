import re
from collections import defaultdict

UNIT = 65536

def jacard(A, B):
    if len(A) == 0 and len(B) == 0:
        return 1 * UNIT

    numerator = 0
    denominator = 0

    union = defaultdict(int)
    intersection = defaultdict(int)

    for a in A:
        if a in B:
            intersection[a] += 1
        union[a] += 1

    for b in B:
        if b in A:
            intersection[b] = min(intersection[b], B.count(b))
        union[b] = max(union[b], B.count(b))

    for key in union:
        denominator += union[key]

    for key in intersection:
        numerator += intersection[key]
    
    return int(UNIT * (numerator / denominator))


def solution(str1, str2):
    answer = 0

    word1 = str1.lower()
    word2 = str2.lower()
    
    word_set1 = []
    word_set2 = []
    for one, two in zip(word1[:-1], word1[1:]):
        if not one.isalpha() or not two.isalpha():
            continue
        word_set1.append(one+two)
    
    for one, two in zip(word2[:-1], word2[1:]):
        if not one.isalpha() or not two.isalpha():
            continue
        word_set2.append(one+two)
    
    return jacard(word_set1, word_set2)
    

if __name__ == "__main__":
    str1 = "aa1+aa2"
    str2 = "AAAA12"

    print(solution(str1, str2))