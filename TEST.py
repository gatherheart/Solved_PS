from collections import deque
import heapq

test = [(4, 2), (4, 1), (1, 2), (3, 4), (4, 0)]

heapq.heapify(test)


print(heapq.heappop(test))

print(heapq.heappop(test))
print(heapq.heappop(test))
print(heapq.heappop(test))