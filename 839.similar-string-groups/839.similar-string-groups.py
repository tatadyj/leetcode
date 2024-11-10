#
# @lc app=leetcode id=839 lang=python3
#
# [839] Similar String Groups
#

# @lc code=start
class Union_Find:
    def __init__(self, n):
        self.n = n 
        self.parent = [i for i in range(n)]
        self.count = n

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

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def is_similar(s, t):
            count = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    count += 1
                    if count > 2:
                        return False 
            return True

        n = len(strs)
        uf = Union_Find(n)
        for i in range(n):
            for j in range(i+1, n):
                if is_similar(strs[i], strs[j]):
                    uf.union(i, j)

        return uf.count
        
# @lc code=end

