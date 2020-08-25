import sys
sys.setrecursionlimit(10**6)

PAREN_OPEN = '('
PAREN_CLOSE = ')'
ERROR = -1

def divide(w):
    open_count = 0
    close_count = 0
    for paren in w:
        if paren == PAREN_OPEN:
            open_count += 1
        else:
            close_count += 1
        
        if open_count == close_count:
            break
    return w[:open_count+close_count], w[open_count+close_count:]

def is_right_parens(w):
    stack = [ERROR]
    for paren in w:
        if paren == PAREN_OPEN:
            stack.append(paren)
        else:
            top = stack.pop()
            if top == ERROR:
                return False
    return True

def recursive(w):
    if w == "":
        return ""
    
    u, v = divide(w)

    if is_right_parens(u):
        return u + recursive(v)
    else:
        _u = u[1:-1]
        _u = "".join(list(map(lambda x: PAREN_CLOSE if x == PAREN_OPEN else PAREN_OPEN, _u)))
        return PAREN_OPEN + recursive(v) + PAREN_CLOSE + _u

def solution(p):
    answer = recursive(p)
    return answer