import re

SINGLE = 'S'
DOUBLE = 'D'
TRIPLE = 'T'

STAR = "*"
MISS = "#"

def parse(score, domain, option):
    ret = 1

    if domain == SINGLE:
        ret = score ** 1
    elif domain == DOUBLE:
        ret = score ** 2
    elif domain == TRIPLE:
        ret = score ** 3

    if option == STAR:
        ret *= 2
    elif option == STAR + STAR:
        ret *= 4
    elif option == MISS:
        ret *= -1
    elif option == MISS + STAR:
        ret *= -2

    return ret

def solution(dartResult):
    dartResult = re.findall(r"[0-9][0]?[S|D|T][*|#]?", dartResult)
    answer = 0
    dartParsed = []
    option_cache = ""
    for dart in dartResult[::-1]:
        score = int(re.findall(r"[0-9]+", dart)[0])
        domain = re.findall(r"[S|D|T]", dart)[0]
        option = re.findall(r"[*|#]", dart)        
        option.append("")
        _option = option[0]

        if option_cache:
            _option += option_cache
            option_cache = ""

        if option[0] == STAR:
            option_cache += option[0]

        dartParsed.append((score, domain, _option))

    for dart in dartParsed:
        answer += parse(*dart)

    return answer

if __name__ == "__main__":

    dartResult = "1D2S0T"
    print(solution(dartResult))