import sys 

'''CONSTANTS'''

LEFTMOST = 0
MIDDLE = 1
RIGHTMOST = 2
MAX_CACHE_VALUE = sys.maxsize
MIN_CACHE_VALUE = -MAX_CACHE_VALUE

'''VARIABLES'''
# N(1 ≤ N ≤ 100,000)
N, M = 0, 3
min_score, max_score = MAX_CACHE_VALUE, MIN_CACHE_VALUE
arr = []
cache = []
'''UTILS'''

def go_down(cache, arr):
    
    # (Min, Max) CACHE for 2 rows X 3 columns 
    cache.append([[MAX_CACHE_VALUE, MIN_CACHE_VALUE] for i in range(3)])
    for col, score in enumerate(arr[1]):

        if col == LEFTMOST:
            # Update Min
            cache[1][0][0] = min([cache[1][0][0], cache[0][0][0] + score, cache[0][1][0] + score])
            # Update Max
            cache[1][0][1] = max([cache[1][0][1], cache[0][0][1] + score, cache[0][1][1] + score])

        elif col == MIDDLE:
            cache[1][1][0] = min([cache[1][1][0], cache[0][0][0] + score, \
                cache[0][1][0] + score, cache[0][2][0] + score])
            cache[1][1][1] = max([cache[1][1][1], cache[0][0][1] + score, \
                cache[0][1][1] + score, cache[0][2][1] + score])
    
        elif col == RIGHTMOST:
            cache[1][2][0] = min([cache[1][2][0], cache[0][1][0] + score, cache[0][2][0] + score])
            cache[1][2][1] = max([cache[1][2][1], cache[0][1][1] + score, cache[0][2][1] + score])


'''INPUT'''
'''COMPUTE'''

N = int(sys.stdin.readline())

arr.append(list(map(int, sys.stdin.readline().split())))
first_cache = list(map(lambda x: [x, x], arr[0]))
cache.append(first_cache)

for i in range(N-1):
    arr.append(list(map(int, sys.stdin.readline().split())))
    go_down(cache, arr)
    
    cache.pop(0)
    arr.pop(0)

'''OUTPUT'''

for score in cache[-1]:
    if min_score > score[0]:
        min_score = score[0]

    if max_score < score[1]:
        max_score = score[1]

print(max_score, min_score)

'''
CASE 1.

3
1 2 3
4 5 6
4 9 0

CASE 2.

5
1 2 3
4 5 6
4 9 0
1 2 3
4 5 6

27 12

CASE 3.

4
1 3 3
1 2 3
4 10 6
10 10 0

4
1 2 3 => [1, 1] [2, 2] [3, 3]
4 10 6 => [5, 6] [11, 13] [8, 9]
10 10 0 => [15, 23] [15, 23] [8, 13]




'''