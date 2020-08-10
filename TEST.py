import heapq

a = [(4, 5), (3, 3), (6, 10), (1, 100), (7, 2), (6, 6), (3, 100)]

HASH_MAX_SIZE = 300000
b = heapq.heapify(a)
salt = 'KoreanCat'

def hash_func(number):
    salt = 'KoreanCat'
    return hash(str(number)+salt) % HASH_MAX_SIZE

print(hash_func(1))
print(hash_func(2))

print(hash_func(1 + hash_func(2)))
print(hash_func(1 + hash_func(2)))
print(hash_func(2 + hash_func(1)))
print(hash_func(2 + hash_func(1)))