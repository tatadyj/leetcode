#
# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#

# @lc code=start
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort()
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        n = len(matchsticks)
        visited = [None] * n
        def dfs(start, count, sum):
            if count == 4:
                return True 

            if sum > total / 4:
                return False 

            if sum == total / 4:
                return dfs(0, count+1, 0)

            for i in range(start, n):
                if not visited[i]:
                    if i-1 >= 0 and matchsticks[i] == matchsticks[i-1] and not visited[i-1]:
                        continue
                    visited[i] = True 
                    if dfs(i+1, count, sum+matchsticks[i]):
                        return True 
                    visited[i] = False
            return False
        
        return dfs(0, 0, 0) 
# @lc code=end

