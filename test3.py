import re
x = re.search("[$-_]+", "/")
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
