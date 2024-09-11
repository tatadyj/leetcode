#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                res = max(res, right - left + 1)
            if nums[right] == 0:
                left = right
            if nums[left] == 0:
                left += 1
        return res 
        
# @lc code=end

