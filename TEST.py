import heapq

a = [(4, 5), (3, 3), (6, 10), (1, 100), (7, 2), (6, 6), (3, 100)]

b = heapq.heapify(a)

print(a)
print(b)