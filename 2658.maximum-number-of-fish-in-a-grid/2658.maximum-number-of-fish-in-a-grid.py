#
# @lc app=leetcode id=2658 lang=python3
#
# [2658] Maximum Number of Fish in a Grid
#

# @lc code=start
class Union_Find:
    def __init__(self, m, n, grid):
        self.parent = [i for i in range(m*n)]
        self.size = [0 for i in range(m*n)]
        for i in range(m):
            for j in range(n):
                self.size[i*n+j] = grid[i][j]


    def find(self, x):
        if self.parent[x] == x:
            return x 
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return 
        if x_root > y_root:
            x_root, y_root = y_root, x_root
        self.parent[y_root] = x_root
        self.size[x_root] += self.size[y_root]

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        uf = Union_Find(m, n, grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue 
                for k in range(4):
                    new_i, new_j = i + d[k][0], j + d[k][1]
                    if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n and grid[new_i][new_j] != 0:
                        uf.union(i*n+j, new_i*n+new_j)

        return max(uf.size)

        
        
# @lc code=end

