#
# @lc app=leetcode id=1627 lang=python3
#
# [1627] Graph Connectivity With Threshold
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
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        uf = Union_Find(n+1)
        for k in range(threshold+1, n+1):
            for x in range(2*k, n+1, k):
                uf.union(k, x)

        ans = []
        for p,q in queries:
            ans.append(uf.find(p)==uf.find(q))
        return ans
# @lc code=end

