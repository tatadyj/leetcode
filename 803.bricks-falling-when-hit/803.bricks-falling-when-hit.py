#
# @lc app=leetcode id=803 lang=python3
#
# [803] Bricks Falling When Hit
#

# @lc code=start
class Union_Find:
    def __init__(self, m, n):
        self.parent = [[(i, j) for j in range(n)] for i in range(m)]
        self.size = [[1] * n for i in range(m)]
        self.m = m
        self.n = n 
       
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
        if x_root == y_root:
            return 
        if x_root[0]*self.n + x_root[1] > y_root[0]*self.n + y_root[1]:
            x_root, y_root = y_root, x_root
        self.parent[y_root[0]][y_root[1]] = x_root
        self.size[x_root[0]][x_root[1]] += self.size[y_root[0]][y_root[1]]

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        grid_init = deepcopy(grid)
        m = len(grid)
        n = len(grid[0])
        uf = Union_Find(m, n)

        for x, y in hits:
            grid[x][y] = 0 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_i, new_j = i+dir[0], j+dir[1]
                    if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n and grid[new_i][new_j] == 1:
                        uf.union((i,j), (new_i, new_j))

        ans = []
        for t in range(len(hits)-1, -1, -1):
            i, j = hits[t]
            if grid_init[i][j] == 0: 
                ans.append(0)
                continue 
            grid[i][j] = 1
            count = 0
            flag = 0
            for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_i, new_j = i+dir[0], j+dir[1]
                if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n and grid[new_i][new_j] == 1:
                    if uf.find((i, j)) != uf.find((new_i, new_j)):
                        root_new_i, root_new_j = uf.find((new_i, new_j))
                        if root_new_i == 0 or i == 0:
                            flag = 1
                        if root_new_i > 0:
                            count += uf.size[root_new_i][root_new_j]
                        uf.union((i,j), (new_i, new_j))
            if flag == 0:
                ans.append(0)
            else:
                ans.append(count)
        return ans[::-1]



            
        
# @lc code=end

