from collections import deque

test = deque([1])

test.appendleft(0)
print(test)

test.append(-1)

print(test)

test.popleft()
print(test)
test.pop()

print(test)