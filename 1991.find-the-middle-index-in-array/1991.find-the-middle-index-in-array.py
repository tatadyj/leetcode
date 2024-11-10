#
# @lc app=leetcode id=1991 lang=python3
#
# [1991] Find the Middle Index in Array
#

# @lc code=start
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        sums = sum(nums)
        prefix_sum = 0 # -1 index 

        for i in range(len(nums)):
            if 2 * prefix_sum + nums[i] == sums:
                return i 
            prefix_sum += nums[i]
        return -1
        
# @lc code=end

