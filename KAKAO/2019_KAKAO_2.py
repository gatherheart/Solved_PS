from collections import defaultdict, deque

def solution(N, stages):
    answer = []
    result = []
    KAKAO_UNIT = 1 << 8
    numerators = defaultdict(float)
    denominators = defaultdict(float)
    
    for i in range(1, N + 1):
        numerators[i] = 0
        denominators[i] = 1
    
    stages.sort()
    prev_stage = stages[0]
    denominators[prev_stage] = len(stages)
    stages = deque(stages)
    
    while stages:
        stage = stages.popleft()
        if stage == N + 1:
            break
        if prev_stage != stage:
            denominators[stage] = denominators[prev_stage] - numerators[prev_stage]
        numerators[stage] += 1
        prev_stage = stage

    for i, j in zip(numerators, denominators):
        result.append((numerators[i] * KAKAO_UNIT / denominators[j], i))
    
    result.sort(reverse=True, key=lambda x: x[0])
    
    answer = list(map(lambda x: x[1], result))
    
    return answer

if __name__ == "__main__":

    test = 1
    
    if test == 1:
        N, stages = 5, [2, 1, 2, 6, 2, 4, 3, 3]

    print(solution(N, stages))
