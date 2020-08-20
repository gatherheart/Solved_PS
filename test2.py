test = [{1: 2}, {3: 4}]

print(test)

test2 = test[:]

print(test2)

test[0][1] = -2

print(test)
print(test2)