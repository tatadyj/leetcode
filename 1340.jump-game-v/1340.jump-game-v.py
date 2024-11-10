#
# @lc app=leetcode id=1340 lang=python3
#
# [1340] Jump Game V
#

# @lc code=start
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        memo = [None] * len(arr)

        def dfs(i):
            if memo[i]:
                return memo[i]

            ret = 1
            for x in range(1, d+1):
                if i + x >= len(arr): break 
                if arr[i + x] >= arr[i]: break 
                ret = max(ret, 1 + dfs(i + x))

            for x in range(1, d+1):
                if i - x < 0: break 
                if arr[i - x] >= arr[i]: break 
                ret = max(ret, 1 + dfs(i - x))

            memo[i] = ret 
            return ret

        for i in range(len(arr)):
            dfs(i)
        return max(memo)        
# @lc code=end

