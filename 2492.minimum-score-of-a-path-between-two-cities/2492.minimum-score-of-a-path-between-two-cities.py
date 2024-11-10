#
# @lc app=leetcode id=2492 lang=python3
#
# [2492] Minimum Score of a Path Between Two Cities
#

# @lc code=start
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
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = Union_Find(n+1)
        for a,b,_ in roads:
            uf.union(a, b)
        
        ans = float('inf')
        p = uf.find(1)
        for a,b,e in roads:
            if a != 1:
                if p == uf.find(a):
                    ans = min(ans, e)
            else:
                if p == uf.find(b):
                    ans = min(ans, e)
        return ans
# @lc code=end

