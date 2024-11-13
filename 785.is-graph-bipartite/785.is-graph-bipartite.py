#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
def bfs():
    n = len(graph)
    visited = [-1] * n
    for i in range(n):
        if visited[i] != -1: continue 
        queue = deque()
        queue.append((i, 0))
        visited[i] = 0 # set to group 0

        while queue:
            curr, gp = queue.popleft()
            for nxt in graph[curr]:
                if visited[nxt] == gp: 
                    return False
                if visited[nxt] == 1-gp:
                    continue 
                if visited[nxt] == -1:
                    queue.append((nxt, 1-gp))
                    visited[nxt] = 1-gp
    return True 

class Union_Find:
    def __init__(self, n):
        self.n = n 
        self.parent = [i for i in range(n)]
    
    def find(self, x):
        if self.parent[x] == x:
            return x 
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        self.parent[y_root] = x_root 

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        uf = Union_Find(n)
        for i in range(n):
            nd = graph[i]
            for i in range(len(nd)-1):
                uf.union(nd[i], nd[i+1])
        for i in range(n):
            if graph[i] != [] and uf.find(i) == uf.find(graph[i][0]):
                return False 
        return True 


        
# @lc code=end

