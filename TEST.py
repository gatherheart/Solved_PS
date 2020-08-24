from collections import deque
import heapq

test = [(4, 2, 3), (4, 2, 1), (4, 1, 2), (3, 4, 1), (4, 2, 0)]
test2 = {1: 2, 3: 4}

heapq.heapify(test)

print(heapq.heappop(test))

print(heapq.heappop(test))
print(heapq.heappop(test))
print(heapq.heappop(test))
print(heapq.heappop(test))