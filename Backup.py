PAREN_OPEN = '('
PAREN_CLOSE = ')'
ERROR = -1

def solution(p):
    answer = ''
    stack = [ERROR]
    parens = list(p)
    error = []
    result = ""
    
    for paren in parens:
        if paren == PAREN_OPEN:
            
            if error:
                stack.append(paren)
            else:
                stack.append(paren)
                result += PAREN_OPEN
            
            if len(stack) - 1 == len(error):
                while stack[-1] != ERROR:
                    result += stack.pop()
                while error:
                    result += error.pop()
                    
        elif paren == PAREN_CLOSE:
            top = stack.pop()
            # Error Case
            if top == ERROR:
                stack.append(ERROR)
                error.append(paren)
            # Normal Case
            else:
                result += PAREN_CLOSE
                
    answer = result    
    return answer