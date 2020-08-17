from collections import deque 
import sys 
for tc in range(int(sys.stdin.readline())): 
    v, e = map(int, sys.stdin.readline().split()) 
    link = [[] for _ in range(v+1)] 
    for _ in range(e): 
        a, b = map(int, sys.stdin.readline().split()) 
        link[a].append(b) 
        link[b].append(a) 
        color = [0] * (v+1) 
        STOP = False 
        for i in range(1, v+1): 
            if STOP: 
                break 
            if color[i] > 0: 
                continue 
            color[i] = 1 
            queue = deque([i]) 
            while queue and not STOP: 
                q = queue.popleft() 
                c = 3 - color[q] 
                for l in link[q]: 
                    if color[l] == 0: 
                        color[l] = c 
                        queue.append(l) 
                    elif color[l] == color[q]: 
                        STOP = True 
                        break 
                    
    print("YES" if not STOP else "NO")

