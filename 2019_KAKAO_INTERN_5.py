from collections import defaultdict
import heapq

def solution(k, room_number):
    answer = []
    remains = []
    next_room = 0
    max_room = 0
    allocated = defaultdict(bool)
    allocated_range = defaultdict(int)
    
    for room in range(k+1):
        allocated_range[room] = room
    
    for room in room_number:
        
        #print("*" * 10)
        #print("room", room, "to", allocated_range[room])
        
        if allocated[room]:
            start = allocated_range[room] + 1
            #print("cache", start)
            
            i = start    
            while i <= k:
                #print(i, end=" ")
                if not allocated[i]:
                    #print("\n", "allocating", i)
                    allocated[i] = True
                    answer.append(i)
                    allocated_range[room] = i
                    break
                
                else:
                    i = allocated_range[i] + 1
                            
            #print()     
            continue
        
            #print()
        allocated[room] = True
        answer.append(room)
    
    #print(answer)
    return answer

if __name__ == "__main__":

    test = 1
    
    if test == 1:
        k, room_number = 10, [1,3,4,1,3,1]	
        
    print(solution(k, room_number))