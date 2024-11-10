#
# @lc app=leetcode id=2328 lang=python3
#
# [2328] Number of Increasing Paths in a Grid
#

# @lc code=start
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        memo = [[None] * n for _ in range(m)]

        def dfs(r, c):
            if memo[r][c]:
                return memo[r][c]

            ret = 1 # 至少是1
            for d in dir:
                nxt_r, nxt_c = r + d[0], c + d[1]
                if nxt_r >= 0 and nxt_r < m and nxt_c >= 0 and nxt_c < n \
                            and grid[nxt_r][nxt_c] > grid[r][c]:
                    ret += dfs(nxt_r, nxt_c)

            memo[r][c] = ret
            return ret 

        ans = 0
        for i in range(m):
            for j in range(n):
                ans += dfs(i, j)
        return ans % (10**9 + 7)
                
# @lc code=end

