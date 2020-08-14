# Python3 program to print DFS traversal  
# from a given given graph 
from collections import defaultdict 
  
# This class represents a directed graph using 
# adjacency list representation 
class Graph: 
  
    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list)
  
    # function to add an edge to graph 
    def addEdge(self, u, v): 
        self.graph[u].append(v) 
  
    # A function used by DFS 
    def DFSUtil(self, v, visited, prev_path, end_point): 
  
        # Mark the current node as visited  
        # and print it 
        visited[v] = True
        if v == end_point:
            return

        # Recur for all the vertices  
        # adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                prev_path[i] = v
                self.DFSUtil(i, visited, prev_path, end_point)
                visited[i] = False
        
        print("LAST:", v)
        
    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 
    def DFS(self, v, end_point): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (max(self.graph)+1) 
        prev_path = [-1] * (max(self.graph)+1)
        # Call the recursive helper function  
        # to print DFS traversal 
        self.DFSUtil(v, visited, prev_path, end_point) 
        print(prev_path)
        print(visited)
  
# Driver code 
  
# Create a graph given  
# in the above diagram 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2)
g.addEdge(2, 0) 
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(4, 5) 
g.addEdge(5, 5)
  
print("Following is DFS from (starting from vertex 2)") 
g.DFS(0, 5) 

# This code is contributed by Neelam Yadav 