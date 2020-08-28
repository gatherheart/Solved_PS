from collections import defaultdict

test = defaultdict(int)

print(test[(1, 2)])

test[((1, 2), (3, 4))] = 1

print(test[((1, 2), (3, 4))])


x, y, z, w = ((1, 2), (3, 4))

print(x, y, z,  w)