#
# @lc app=leetcode id=1697 lang=python3
#
# [1697] Checking Existence of Edge Length Limited Paths
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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        for i, q in enumerate(queries):
            q.append(i)

        queries.sort(key=lambda x: x[2])
        edgeList.sort(key=lambda x: x[2])
        uf = Union_Find(n)

        ans = [None] * len(queries)
        i = 0 
        for p, q, l, idx in queries:
            while i < len(edgeList) and edgeList[i][2] < l:
                uf.union(edgeList[i][0], edgeList[i][1])
                i += 1
            ans[idx] = uf.find(p) == uf.find(q)
        return ans
# @lc code=end

