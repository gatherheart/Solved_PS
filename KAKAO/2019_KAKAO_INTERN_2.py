import re

def solution(s):
    answer = []
    _set = []
    
    splited = re.split("},", s)    
    
    #print(splited)
    
    for new_s in splited:
        new_s = re.sub("[{}]+", "", new_s)
        #print(new_s)
        new_s = list(map(int, re.split(",", new_s)))
        #print("LIST", new_s)
        _set.append(new_s)
        #print("____________________-")
    
    _set.sort(key=lambda x: len(x))
    
    #print(_set)
    
    for _s in _set:
        for i in _s:
            if not i in answer:
                answer.append(i)
            #print(answer)
    #print(answer)
    
    return answer


if __name__ == "__main__":

    test = 3
    
    if test == 1:
        s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"	

    elif test == 2:
        s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"	
    elif  test == 3:
        s = "{{20,111},{111}}"	
    elif test == 4:
        s = "{{123}}"

    print(solution(s))