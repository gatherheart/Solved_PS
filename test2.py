from collections import OrderedDict

test = OrderedDict()

test[2] = 1
test[3] = 1
test[5] = 10
test[0] = 3

print(test)

test.popitem(last=False)
print(test)
