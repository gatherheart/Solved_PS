test = [[1,2], [3, 4]]

test2 = [*test]
test3 = test[:]

test[0][0] = -1
print(test2)
print(test3)