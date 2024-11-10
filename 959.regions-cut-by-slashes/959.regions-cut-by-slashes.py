#
# @lc app=leetcode id=959 lang=python3
#
# [959] Regions Cut By Slashes
#

# @lc code=start
class Union_Find:
    def __init__(self, n):
        self.n = n 
        self.parent = [[(i,j) for j in range(n)] for i in range(n)]
        for i in range(n):
            self.parent[i][0] = (0, 0)
            self.parent[i][n-1] = (0, 0) 
        for j in range(n):
            self.parent[0][j] = (0, 0)
            self.parent[n-1][j] = (0, 0)


    def find(self, x):
        i, j = x
        if self.parent[i][j] == x:
            return x
        else:
            self.parent[i][j] = self.find(self.parent[i][j])
            return self.parent[i][j]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        self.parent[y_root[0]][y_root[1]] = x_root 


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        uf = Union_Find(n + 1) # n+1 points, n squares

        count = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == ' ':
                    continue 
                if grid[i][j] == '/':
                    a, b = (i+1, j), (i, j+1)
                if grid[i][j] == '\\':
                    a, b = (i, j), (i+1, j+1)
                if uf.find(a) == uf.find(b):
                    count += 1 
                else:
                    uf.union(a, b)
        return count


        
# @lc code=end

