#
# @lc app=leetcode id=351 lang=python3
#
# [351] Android Unlock Patterns
#

# @lc code=start
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1), \
                (-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
        def dfs(i, j, step):
            nonlocal ans 
            if step >=m and step <= n:
                ans += 1

            if step > n:
                return

            for dx, dy in dir:
                nxt_i, nxt_j = i + dx, j + dy
                if nxt_i < 0 or nxt_i >= 3 or nxt_j < 0 or nxt_j >= 3: continue 
                if visited[nxt_i][nxt_j] == False:
                    visited[nxt_i][nxt_j] = True
                    dfs(nxt_i, nxt_j, step+1)
                    visited[nxt_i][nxt_j] = False
                else:
                    nxt_i, nxt_j = nxt_i + dx, nxt_j + dy
                    if nxt_i < 0 or nxt_i >= 3 or nxt_j < 0 or nxt_j >= 3: continue 
                    if visited[nxt_i][nxt_j] == False:
                        visited[nxt_i][nxt_j] = True
                        dfs(nxt_i, nxt_j, step+1)
                        visited[nxt_i][nxt_j] = False



        ans = 0
        visited = [[False]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                visited[i][j] = True 
                dfs(i, j, 1)
                visited[i][j] = False
        return ans
# @lc code=end

