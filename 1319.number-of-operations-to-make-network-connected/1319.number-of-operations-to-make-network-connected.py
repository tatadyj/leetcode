#
# @lc app=leetcode id=1319 lang=python3
#
# [1319] Number of Operations to Make Network Connected
#

# @lc code=start
class Union_Find:
    def __init__(self, n):
        self.n = n 
        self.parent = [i for i in range(n)]
        self.count = n
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.parent[y_root] = x_root
            self.count -= 1
            self.size[x_root] += self.size[y_root]

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        uf = Union_Find(n)
        for a, b in connections:
            uf.union(a, b)
        
        freq = defaultdict(int)
        for a, b in connections:
            p = uf.find(a)
            freq[p] += 1
        
        count = 0
        for p in freq:
            count += freq[p] - (uf.size[p] - 1)
        if count >= uf.count - 1:
            return uf.count - 1
        else:
            return -1
        
# @lc code=end

