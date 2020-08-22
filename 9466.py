import sys 

'''CONSTANTS'''

IN_CYCLE = -1

'''VARIABLES'''
# T = # of test, n (2 ≤ n ≤ 100,000), # of students 
T, n = 0, 0
arr = []
results = []

'''UTILS'''

def check_cycles(n, arr):
  
    # Optimization #1, included in cycle
    incycle = [0] * (n + 1)

    for student in range(1, n + 1):

        # Optimization #2
        if incycle[student]:
            continue
        
        group_leader = student
        next_student = student

        while not incycle[next_student]:
            incycle[next_student] = group_leader
            next_student = arr[next_student]

        while incycle[next_student] == group_leader:
            incycle[next_student] = IN_CYCLE
            next_student = arr[next_student]
        
    return n - incycle.count(IN_CYCLE)

'''INPUT'''
'''COMPUTE'''   
'''OUTPUT'''

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    line = list(map(int, sys.stdin.readline().split()))
    arr = [0] + line
    results.append(str(check_cycles(n, arr))+"\n")

for result in results:
    sys.stdout.write(result)

'''

CASE 1. 
2
7
3 1 3 7 3 4 6
8
1 2 3 4 5 6 7 8

1
7
3 1 3 7 3 4 6

1 2 3 4 5 6 7
3 1 3 7 3 4 6

1
8
1 2 3 4 5 6 7 8

1 2 3 4 5 6 7 8
1 2 3 4 5 6 7 8

1
4
1 2 3 4
3 1 2 3

1
5
1 2 3 4 5
3 1 2 3 4

1
5
3 1 2 3 4

1
5
1 2 3 4 5
2 4 4 5 3

1
5
2 4 4 5 3

1
4
3 1 2 4 

1
100
1 1 1 1 1 1 7 8 9 10 12 11 13 14 15 16 17 18 21 19 20 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100

'''