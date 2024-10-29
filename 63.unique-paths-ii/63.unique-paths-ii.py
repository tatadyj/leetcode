#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[None]*n for i in range(m)]
        
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        elif obstacleGrid[0][0] == 1:
            dp[0][0] = 0
            
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = (dp[i-1][0] != 0)*1
            elif obstacleGrid[i][0] == 1:
                dp[i][0] = 0
    
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = (dp[0][j-1] != 0)*1
            elif obstacleGrid[0][j] == 1:
                dp[0][j] = 0
                
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    
        return dp[-1][-1]
                
# @lc code=end

