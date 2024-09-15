#
# @lc app=leetcode id=2863 lang=python3
#
# [2863] Maximum Length of Semi-Decreasing Subarrays
#

# @lc code=start
class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        # keep monotonic increasing stack 
        stack = []
        for i in range(len(nums)):
            if not stack or nums[stack[-1]] < nums[i]:
                stack.append(i)

        res = 0
        for j in range(len(nums)-1, -1, -1):
            while stack and nums[j] < nums[stack[-1]]:
                k = stack.pop()
                res = max(res, j-k+1)

        return res
# @lc code=end

