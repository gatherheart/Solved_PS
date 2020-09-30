import sys 

'''CONSTANTS'''

'''VARIABLES'''
# T = # of test, n (2 ≤ n ≤ 100,000), # of students 
T, n = 0, 0
arr = []
results = []

'''UTILS'''

def DFS(start, arr, group):
    
    def peek(stack):
        return stack[-1]

    stack = [start]

    while stack:
        curr = peek(stack)
        group[curr] = start
        _next = arr[curr]

        # if there is a cycle
        if start == _next:
            # Optimization #1
            for s in stack:
                group[s] = -start

            return stack

        # Optimization #2, not to proceed when encounter "already in Cycle"
        elif start != _next and group[_next] < 0:
            return []

        # if meet already visited student, but Not cycle
        elif start != _next and group[_next] == start:
            # Optimization #1, When found Sub-Cycle, check it            
            stack.clear()

            while group[_next] == start:
                group[_next] = -start
                stack.append(_next)
                _next = arr[_next]
 
            return stack

        stack.append(_next)

    return []

def check_cycles(n, arr):
  
    # Optimization #1
    group = [0] * (n + 1)    
    count = 0

    for student in range(1, n + 1):

        # Optimization #1
        if group[student]:
            continue
        
        group[student] = student
        students_in_cycle = DFS(student, arr, group)
        count += len(students_in_cycle)
        
    return n - count

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