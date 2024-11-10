#
# @lc app=leetcode id=990 lang=python3
#
# [990] Satisfiability of Equality Equations
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
    def equationsPossible(self, equations: List[str]) -> bool:
        queries = []
        uf = Union_Find(26)

        for eq in equations:
            a = eq[0]
            b = eq[-1]
            comp = eq[1:-1]
            if comp == '!=':
                queries.append([ord(a)-ord('a'), ord(b)-ord('a')])
            else:
                uf.union(ord(a)-ord('a'), ord(b)-ord('a'))
        
        for p, q in queries:
            if uf.find(p) == uf.find(q):
                return False 
        return True 



        
# @lc code=end

