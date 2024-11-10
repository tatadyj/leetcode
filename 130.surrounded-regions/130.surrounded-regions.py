#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Union_Find:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        self.parent[root_y] = root_x

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        uf = Union_Find(m*n+1)
        dummy = m*n
        for i in range(m):
            if board[i][0] == 'O':
                uf.union(i*n, dummy)
            if board[i][n-1] == 'O':
                uf.union(i*n+n-1, dummy)

        for j in range(n):
            if board[0][j] == 'O': 
                uf.union(j, m*n)
            if board[m-1][j] == 'O':
                uf.union((m-1)*n+j, dummy)
        
        d = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O':
                    for k in range(4):
                        x, y = i + d[k][0], j + d[k][1]
                        if board[x][y] == 'O':
                            uf.union(x*n+y, i*n+j)

        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O' and uf.find(i*n+j) != uf.find(dummy):
                    board[i][j] = 'X'
        
# @lc code=end

