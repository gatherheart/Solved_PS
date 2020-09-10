## 0. !!! READ CAREFULLY !!!

## 1. Shallow Copy => Deep Copy
board_copy = board [X]
board_copy = board[:] [O]
board_copy = [[board[i][j] for j in range(len(board[i])) for i in range(len(board))]]

## 2. DFS => BFS
Shortest Path => BFS

## 3. INITIALIZATION 
DEFAULT_CACHE_VALUE = -1

## 4. list.pop() == list.get(-1)
list.pop(0) == queue
list.pop(-1) == stack

## 5. Regex
[https://www.w3schools.com/python/python_regex.asp]

## 6. Variable's Name
pos = x + OFFSET [o]
pose = x + OFFSET [x]

