#
# @lc app=leetcode id=2850 lang=python3
#
# [2850] Minimum Moves to Spread Stones Over Grid
#

# @lc code=start
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        res = float('inf')
        def dfs(curr, moves):
            nonlocal res
            x = curr // 3
            y = curr % 3

            if curr == 9:
                res = min(res, moves)
                #print(moves, grid)
                return 

            if moves > res:
                return 

            if grid[x][y] == 0:
                for i in range(3):
                    for j in range(3):
                        if grid[i][j] >= 2:
                            grid[i][j] -= 1
                            grid[x][y] += 1
                            dfs(curr+1, moves+abs(x-i)+abs(y-j))
                            grid[i][j] += 1
                            grid[x][y] -= 1
            else:
                dfs(curr+1, moves)

        dfs(0, 0)
        return res
             
# @lc code=end

