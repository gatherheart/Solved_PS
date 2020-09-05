from collections import defaultdict
import sys
sys.setrecursionlimit(10000)


class DisjoinSet:
    
    def __init__(self, items=[]):
        super().__init__()
        self.parent = defaultdict(int)
        
        for item in items:
            self.parent[item] = item
            
    def find(self, item, size=0):
        if self.parent[item] == 0:
            return item, size
        
        parent, parent_size = self.find(self.parent[item], size+1)
        self.parent[item] = parent
        return parent, parent_size

    def set_parent(self, child, parent):
        self.parent[child] = parent

    def union(self, item1, item2):
        
        root1, size1 = self.find(item1)
        root2, size2 = self.find(item2)
        
        if item1 >= item2:
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2
                    
    
def solution(k, room_number):
    answer = []
    allocated = defaultdict(bool)
    rooms_set = DisjoinSet()
    
    for room in room_number:
        #print(room, end=" ")
        new_room, _ = rooms_set.find(room)    
        #print(room)
        if not allocated[new_room]:
            allocated[new_room] = True
            answer.append(new_room)
        
        else:            
            while allocated[new_room]:
                rooms_set.set_parent(new_room, new_room + 1)
                new_room, _ = rooms_set.find(new_room)
                #print(new_room)
            
            allocated[new_room] = True
            answer.append(new_room)
    
    #print(rooms_set.parent)
    #print()
    #print(allocated)
        
    return answer

if __name__ == "__main__":

    test = 1
    
    if test == 1:
        k, room_number = 20, [1,3,4,1,3,1,10, 5, 4, 3, 2, 1, 10, 10, 10, 3]	
        
    print(solution(k, room_number))