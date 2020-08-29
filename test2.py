cache = {'a': 2, 'c': 1, 'b': 1}


def testf():
    print(cache)
    tt = list(cache.items())
    tt.sort(key=lambda x: (x[1], x[0]))
    print(tt)
    
print(cache)

testf()

print(cache)