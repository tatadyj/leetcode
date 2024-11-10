#
# @lc app=leetcode id=765 lang=python3
#
# [765] Couples Holding Hands
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
        if x_root > y_root:
            x_root, y_root = y_root, x_root
        self.parent[y_root] = x_root

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        N = len(row)
        uf = Union_Find(N)
        for i in range(0, N, 2):
            uf.union(i, i+1)

        for i in range(0, N, 2):
            uf.union(row[i], row[i+1])

        count = defaultdict(int)
        for i in range(N):
            count[uf.find(i)] += 1
        
        res = 0 
        for x in count:
            res += count[x] // 2 - 1
        return res

        

        
        
# @lc code=end

