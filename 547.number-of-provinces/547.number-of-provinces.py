#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start

class Union_Find:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n

    def find(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node_i, node_j):
        root_i = self.find(node_i)
        root_j = self.find(node_j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j 
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_j] += 1
            self.count -= 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = Union_Find(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        return uf.count
        
        
# @lc code=end

