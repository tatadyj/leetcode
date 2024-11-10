#
# @lc app=leetcode id=685 lang=python3
#
# [685] Redundant Connection II
#

# @lc code=start
class Union_Find:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.count = n-1

    def find(self, x):
        if self.parent[x] == x:
            return x 
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y): # x->y
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False 
        else:
            self.parent[y_root] = x_root
            self.count -= 1
            return True 

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        candidates = []
        parent = defaultdict(list)
        for a, b in edges:
            parent[b].append(a)
        for child in parent:
            if len(parent[child]) == 2:
                for p in parent[child]:
                    candidates.append((p, child))
        
        uf = Union_Find(n+1)
        # 有环
        if len(candidates) == 0:
            for a, b in edges:
                if uf.union(a, b):
                    continue 
                else:
                    return [a, b]

        # 节点有两个parent
        if len(candidates) == 2:
            for a, b in edges:
                if (a, b) in candidates: continue
                uf.union(a, b)

        a, b = candidates[0]
        uf.union(a, b)
        if uf.count != 1:
            return [a, b]
        return list(candidates[1])
        
# @lc code=end

