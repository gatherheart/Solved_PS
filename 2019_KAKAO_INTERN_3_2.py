import re
from collections import defaultdict
from itertools import combinations, product

MARKED = "*"

class PoorId:
    def __init__(self, _id):
        super().__init__()
        self.len = len(_id)
        self.count = 0
        self.id = _id
        self.pattern = "\\b" + re.sub("[*]", "[a-z0-9]", _id) + "$" +"\\b"
        self.matches = []
        
    def __len__(self):
        return self.len    
    
    def match(self, _id):
        
        if re.search(self.pattern, _id):
            self.count += 1
            self.matches.append(_id)
            return True
        
        return False 
    
    def decrease(self):
        self.count -= 1
     

def DFS(idx, visited, poors, banned_id, matches, result):
    
    if idx == len(banned_id):
        #print("COUNT ")
        #print(idx, len(banned_id))
        result.add(tuple(sorted(matches)))
        return 1
    
    ret = 0
    
    for match in poors[banned_id[idx]].matches:
        
        if not visited[match]:
            visited[match] = True
            matches.add(match)
            #print(idx, banned_id[idx], match, matches)
            ret += DFS(idx+1, visited, poors, banned_id, matches, result)
            #print(" ")
            matches.discard(match)
            visited[match] = False
        
    return ret
        
def solution(user_id, banned_id):
    answer = 1
    poors = {}
    result_set = set()
    
    for _id in banned_id:
        #print(_id)
        poors[_id] = PoorId(_id)
    
    for _id in poors:
        #print(poors[_id].id, poors[_id].pattern, end=" ")
        for u in user_id:
            #print(u, end=": ")
            poors[_id].match(u)
        #print()
    
    visited = defaultdict(bool)
    matches = set()
    result = set()
    
    iterables = []

    for _id in banned_id:
        iterables.append(poors[_id].matches)
    
    
    result = []
    cache = defaultdict(bool)
    
    for _set in product(*iterables):
        duplicated_flag = False
        new_set = tuple(sorted(_set))    
        
        if cache[new_set]:
            continue
        
        for i in range(len(_set)):
            for j in range(i+1, len(_set)):
                if _set[i] == _set[j]:
                    duplicated_flag = True
                    break 
            
            if duplicated_flag:
                break
                
        if not duplicated_flag:
            result.append(new_set)
        
        cache[new_set] = True
        
    #print(result)
    return len(result)

if __name__ == "__main__":

    test = 3
    
    if test == 1:
        user_id, banned_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]
    elif test == 2:
        user_id, banned_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]	
    elif  test == 3:
        user_id, banned_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]		
    elif  test == 4:
        user_id, banned_id = ["424", "321", "2", "1"], ["*", "*", "*"]		
    
    print(solution(user_id, banned_id))