from collections import deque

test = "12314"

print(test[::-1])

test = deque(map(int, test))

print(test)