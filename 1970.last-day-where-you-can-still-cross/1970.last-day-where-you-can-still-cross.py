#
# @lc app=leetcode id=1970 lang=python3
#
# [1970] Last Day Where You Can Still Cross
#

# @lc code=start
class Union_Find:
    def __init__(self, m, n):
        self.parent = [[(i, j) for j in range(n)] for i in range(m)]
        self.m = m
        self.n = n 
        self.parent.append([(m, 0), (m, 1)])
        for i in range(n):
            self.parent[0][i] = (m, 0)
            self.parent[m-1][i] = (m, 1) # 添加连个node 分别连接第一排和最后一排所有node

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
        if x_root[0]*self.n + x_root[1] > y_root[0]*self.n + y_root[1]:
            x_root, y_root = y_root, x_root
        self.parent[y_root[0]][y_root[1]] = x_root


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        uf = Union_Find(row, col)
        mat = [[0] * col for _ in range(row)]

        for x, y in cells:
            mat[x-1][y-1] = 1

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1: continue 
                for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_i, new_j = i+dir[0], j+dir[1]
                    if new_i >= 0 and new_i < row and new_j >= 0 and new_j < col and mat[new_i][new_j] == 0:
                        uf.union((i,j), (new_i, new_j))

        def is_ok():
            return uf.find((row, 0)) == uf.find((row, 1))
            

        for day in range(len(cells)-1, -1, -1):
            if is_ok():
                return day + 1
            else:
                i = cells[day][0] - 1
                j = cells[day][1] - 1
                mat[i][j] = 0 
                for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_i, new_j = i+dir[0], j+dir[1]
                    if new_i >= 0 and new_i < row and new_j >= 0 and new_j < col and mat[new_i][new_j] == 0:
                        uf.union((i,j), (new_i, new_j))  
# @lc code=end

