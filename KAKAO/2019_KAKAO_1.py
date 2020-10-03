from collections import defaultdict
ENTER = "Enter"
LEAVE = "Leave"
CHANGE = "Change"

ENTER_MESSAGE = "님이 들어왔습니다."
LEAVE_MESSAGE = "님이 나갔습니다."

class ChatRoom:
    
    def __init__(self):
        super().__init__()

def operation(result, command, chatRoom, nicknames, uid="", name=""):
    
    if command == ENTER:
        chatRoom.append(uid)
        nicknames[uid] = name
        result.append((uid, ENTER_MESSAGE))
        return
    elif command == LEAVE:
        chatRoom.remove(uid)
        result.append((uid, LEAVE_MESSAGE))
        return
    elif command == CHANGE:
        nicknames[uid] = name
        return
    
    return
      
def solution(record):
    answer = []
    nicknames = defaultdict(str)
    chatRoom = []
    result = []
    command, uid, name = "", "", ""
    
    for r in record:
        splited = r.split()
        if len(splited) == 2:
            command, uid = splited
        else:
            command, uid, name = splited
            
        operation(result, command, chatRoom, nicknames, uid, name)
    
    answer = list(map(lambda x: nicknames[x[0]]+x[1], result))
    return answer

if __name__ == "__main__":

    test = 1
    
    if test == 1:
        record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]

    print(solution(record))
