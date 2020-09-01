test = [1, 2, 3, 4]
test.append(None)

for i, j in zip(test, test[1:]):
    print(i, j)
    
    
print("Hello World"+None+"DODO")