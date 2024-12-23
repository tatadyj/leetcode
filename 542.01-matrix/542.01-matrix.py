#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]    
        queue = deque()
        res = [[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0: 
                    queue.append((i, j, 0))
                    res[i][j] = 0

        while queue:
            x, y, level = queue.popleft()
            for dx, dy in dir:
                nxt_x, nxt_y = x + dx, y + dy
                if nxt_x < 0 or nxt_x >= m or nxt_y < 0 or nxt_y >= n: continue 
                if res[nxt_x][nxt_y] != -1: continue 
                if mat[nxt_x][nxt_y] == 1:
                    res[nxt_x][nxt_y] = level + 1   
                    queue.append((nxt_x, nxt_y, level+1))

        return res
# @lc code=end

