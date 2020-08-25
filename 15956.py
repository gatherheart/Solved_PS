import sys 
from collections import defaultdict

'''CONSTANTS'''

AMPERSAND = "&&"
EQUAL = "=="
NOT_EQUAL = "!="
NEGATIVE_SIGN = "-"
ALWAYS_FALSE = "1==0&&"
ALWAYS_TRUE = "1==1&&"

CHECK_EQUATION_SAFE = 0
CHECK_EQUATION_EXIST = 1
CHECK_EQUATION_UNSAFE = -1

'''VARIABLES'''
check = {}
equation_check = defaultdict(dict)
input_line = ""
equations = []
result = set([])

def is_number(item):
    return item.strip(NEGATIVE_SIGN).isnumeric()

class DisjointSet:
    def __init__(self, items=[]):
        super().__init__()
        self.parent = {}
        for item in items:
            self.parent[item] = item

    def __str__(self):
        return "{}".format(self.parent)

    def find(self, item, size=0):
        if not item in self.parent:
            self.parent[item] = item
            return item, size

        if self.parent[item] == item:
            return item, size

        return self.find(self.parent[item], size + 1)
    
    def union(self, item1, item2):

        if not item1 in self.parent:
            self.parent[item1] = item1

        if not item2 in self.parent:
            self.parent[item2] = item2
            
        root1, size1 = self.find(item1)
        root2, size2 = self.find(item2)
        
        if len(root1) <= len(root2):
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2

        return

    def setParent(self, parent, child):

        if not parent in self.parent:
            self.parent[parent] = parent

        root1 = self.find(parent)
        self.parent[child] = root1

    def keys(self):
        return self.parent.keys()

'''
cond1
case 1. var == var 
case 2. var != var

cond2
case 3. var == num
case 4. var != num

cond3
case 5. num == num
case 6. num != num
'''
conds = DisjointSet()

'''UTILS'''

def set_equation(lhs, rhs, sign, equation):
    equation[lhs][rhs] = sign == EQUAL

# return 
# -1 == False, 0 == No Info, 1 == True
def check_equation(lhs, rhs, sign, equation):
    if not lhs in equation:
        return CHECK_EQUATION_SAFE
    
    if not rhs in equation[lhs]:
        return CHECK_EQUATION_SAFE
    
    if sign == EQUAL and equation[lhs][rhs]:
        return CHECK_EQUATION_EXIST
    elif sign == NOT_EQUAL and not equation[lhs][rhs]:
        return CHECK_EQUATION_EXIST
    else:
        return CHECK_EQUATION_UNSAFE

def is_paradox(lhs, rhs, equal_sign, equation_check):
    # Check Paradox    
    _check_paradox = check_equation(lhs, rhs, equal_sign, equation_check)
    print(_check_paradox, lhs, rhs, equal_sign)
    if _check_paradox == CHECK_EQUATION_UNSAFE:
        return True
    _check_paradox = check_equation(rhs, lhs, equal_sign, equation_check)
    if _check_paradox == CHECK_EQUATION_UNSAFE:
        return True

    return False

def is_already_defined(lhs, rhs, equal_sign, equation_check):
    _check_duplicates = check_equation(lhs, rhs, equal_sign, equation_check)
    if _check_duplicates == CHECK_EQUATION_EXIST:
        return True
    return False

'''INPUT'''

input_line = sys.stdin.readline().strip()
equations = input_line.split(AMPERSAND)

for eqn in equations:
    equal_sign = EQUAL if EQUAL in eqn else NOT_EQUAL
    lhs, rhs = eqn.split(equal_sign)

    lhs_is_number = is_number(lhs)
    rhs_is_number = is_number(rhs)

    # condition #1
    # condition #2
    if equal_sign == EQUAL and (not lhs_is_number or not rhs_is_number):
        if lhs == rhs:
            result.add(ALWAYS_TRUE)
        conds.union(lhs, rhs)
    elif equal_sign == NOT_EQUAL:
        if lhs == rhs:
            result.add(ALWAYS_FALSE)
    # condition #3 => Always true or false
    elif lhs_is_number and rhs_is_number:
        if equal_sign == EQUAL:
            if int(lhs) == int(rhs):
                result.add(ALWAYS_TRUE)
            else:
                result.add(ALWAYS_FALSE)
        elif equal_sign == NOT_EQUAL:
            if int(lhs) != int(rhs):
                result.add(ALWAYS_TRUE)
            else:
                result.add(ALWAYS_FALSE)

'''COMPUTE'''

check = dict.fromkeys(conds.keys())
for i in check:
    check[i] = False

print(conds)

for eqn in equations:
    equal_sign = EQUAL if EQUAL in eqn else NOT_EQUAL
    lhs, rhs = eqn.split(equal_sign)

    lhs_is_number = is_number(lhs)
    rhs_is_number = is_number(rhs)
    
    # condition #1 var == var
    if not lhs_is_number and not rhs_is_number:
        if not lhs in check:
            check[lhs] = False
        if not rhs in check:
            check[rhs] = False

        if is_paradox(lhs, rhs, equal_sign, equation_check):
            result.add(ALWAYS_FALSE)
            break
        
        if check[lhs] and check[rhs]:
            print("CHECK", check[lhs], check[rhs], lhs, rhs)
            continue


        if not check[lhs]:
            check[lhs] = True
            _rhs, _ = conds.find(rhs)
            if lhs != _rhs:
                if is_paradox(lhs, _rhs, equal_sign, equation_check):
                    result.add(ALWAYS_FALSE)
                    break
                result.add(lhs + equal_sign + _rhs + AMPERSAND)
                set_equation(lhs, _rhs, equal_sign, equation_check)


        if not check[rhs]:
            check[rhs] = True
            _lhs, _ = conds.find(lhs)

            if is_already_defined(_lhs, rhs, equal_sign, equation_check):
                continue

            if _lhs != rhs:
                if is_paradox(rhs, _lhs, equal_sign, equation_check):
                    result.add(ALWAYS_FALSE)
                    break
                result.add(rhs + equal_sign + _lhs + AMPERSAND)
                set_equation(rhs, _lhs, equal_sign, equation_check)
                    
        continue

    # condition #2 var = num
    if lhs_is_number and not rhs_is_number:
        lhs, rhs = rhs, lhs
    
    if not lhs_is_number and rhs_is_number:

        if not lhs in check:
            check[lhs] = False
        if not rhs in check:
            check[rhs] = False
            
        if not check[lhs] and not check[rhs]:
            if is_paradox(lhs, rhs, equal_sign, equation_check):
                result.add(ALWAYS_FALSE)
                break
            result.add(lhs + equal_sign + rhs + AMPERSAND)
            set_equation(lhs, rhs, equal_sign, equation_check)

        elif (check[lhs] and not check[rhs]) or (not check[lhs] and check[rhs]):
            _rhs, _ = conds.find(rhs)
            if is_paradox(lhs, _rhs, equal_sign, equation_check):
                result.add(ALWAYS_FALSE)
                break
            result.add(lhs + equal_sign + _rhs + AMPERSAND)
            set_equation(lhs, _rhs, equal_sign, equation_check)

        check[lhs] = True
        check[rhs] = True

'''OUTPUT'''

if len(result) > 1:
    if ALWAYS_FALSE in result:
        result = {ALWAYS_FALSE}
    if ALWAYS_TRUE in result:
        result.remove(ALWAYS_TRUE)

print("".join(list(result))[:-2])

'''

1. DFS to find the shortest one
2. Make Acyclic
CASE 1.

festival==kakao&&festival==2018&&haha==123456&&hoho!=123456

festival==2018&&kakao==2018&&haha==123456&&hoho!=haha

festival -> 2018
haha -> 123456
hoho -> not 123456
kakao -> 2018
123456 -> haha, hoho

CASE 2.

kakaocodefestival==-20180804&&hello!=-20180804

kakao==-20180804&&hello!=-20180804


CASE 3. 

a==b&&b==c&&c==a


CASE 4.

int==float

CASE 5.

a==A&&B==b

CASE 6.
a==b&&b==c&&a==c

a==b&&c!=c&&a!=a

Paradox
a==b&&a!=b
a==b&&b==c&&a!=c
abc==123&&abc!=b&&b==123
abc==123&&b==123&&abc!=b


Duplicated
a!=b&&a!=b&&a==c
ab!=b&&ab!=b&&ab==c


'''
