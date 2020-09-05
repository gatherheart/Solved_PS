a = None
def test(i):
    global a
    a = 1
    return 1

print(test(0))
print(a)