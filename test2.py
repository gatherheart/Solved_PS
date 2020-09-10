import itertools




print(list(itertools.accumulate([1, 2, 3])))
print(list(itertools.compress([1, 2, 3], [True, False, True])))
print(list(itertools.repeat(itertools.combinations([1, 2, 3], 2), 2)))