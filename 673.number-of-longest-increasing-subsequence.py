#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        dp = [1] * len(nums)
        count = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[i] == dp[j] + 1:
                        count[i] += count[j] # 需要累加
                    else:
                        continue 

        max_len = 1
        res = 0
        for i in range(len(nums)):
            if dp[i] > max_len:
                max_len = dp[i]
                res = count[i]
            elif dp[i] == max_len:
                res += count[i] # 需要累加
                
        return res 

# @lc code=end

