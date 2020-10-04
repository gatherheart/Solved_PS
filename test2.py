from collections import defaultdict

test = defaultdict(int)

test[0] += 1
test[1] += 1
test[2] += 1

print(list(map(lambda x: (x[1], x[0]), test.items())))