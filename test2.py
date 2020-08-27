test = 1


def tt():
    global test
    print("int tt", test)
    test += 1

print(test)
tt()

print(test)

tt()

print(test)