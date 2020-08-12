import itertools

inp = [2,4, 5,3,1,5]

print(list(itertools.combinations(inp, 2)))

print(list(itertools.permutations(inp, 2)))   