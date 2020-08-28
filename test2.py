from itertools import permutations
from itertools import product
test = [1, 2, 3]


for i in range(1, 10):
    test = [i]
    print('a', test)
    for j in range(2, 3):
        test = [1, 2]

        print('b', test)

