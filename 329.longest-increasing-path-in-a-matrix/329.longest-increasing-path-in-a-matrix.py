#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        memo = [[None] * n for _ in range(m)]

        def dfs(r, c):
            if memo[r][c]:
                return memo[r][c]

            ret = 1 # 至少是1
            for d in dir:
                nxt_r, nxt_c = r + d[0], c + d[1]
                if nxt_r >= 0 and nxt_r < m and nxt_c >= 0 and nxt_c < n \
                            and matrix[nxt_r][nxt_c] > matrix[r][c]:
                    ret = max(ret, 1 + dfs(nxt_r, nxt_c))

            memo[r][c] = ret
            return ret 

        ans = 0
        for i in range(m):
            for j in range(n):
                ret = dfs(i, j)
                ans = max(ans, ret)
        return ans         
# @lc code=end

