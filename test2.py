test = [[1,2], [3, 4]]

test2 = [*test]
test3 = test[:]

test[0][0] = -1
print(test2)
print(test3)

if 1:
    print("A")

if 0:
    print("B")

if 10:
    print("C")


for i in range(10, 0):
    print(i)