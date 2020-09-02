a = 231.3
a = str(a)
print(str(a))

integer, fraction = a.split(".")
base = 7
integer_10, fraction_10 = 0, 0
count = 0
MAX_FRACTION = 30

print(integer, fraction)
print(len(integer), len(fraction))

for i in range(len(integer)):
    integer_10 += int(integer[i]) * pow(4, len(integer)-i-1)

for i in range(len(fraction)):
    fraction_10 += float(fraction[i]) * pow(4, -1-i)
#fraction_10 += float(fraction[i]) * pow(4, -i)

print((integer_10 + fraction_10))

integer_base = ""
fraction_base = ""

while integer_10:
    rem = int(integer_10) % base
    integer_10 //= base
    integer_base = str(rem) + integer_base

while fraction_10 - int(fraction) != 0 and count < MAX_FRACTION:
    fraction_10 *= base
    fraction_base += str(int(fraction_10)) 
    fraction_10 -= int(fraction_10)
    count += 1
    print(fraction_base)

print(integer_base, fraction_base)