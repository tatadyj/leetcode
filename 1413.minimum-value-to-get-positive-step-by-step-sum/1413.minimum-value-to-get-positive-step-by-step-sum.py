#
# @lc app=leetcode id=1413 lang=python3
#
# [1413] Minimum Value to Get Positive Step by Step Sum
#

# @lc code=start
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # find the minimal prefix_sum and 0
        res = 0 

        prefix_sum = 0 # at -1 
        for n in nums:
            prefix_sum += n 
            res = min(res, prefix_sum)
        return -res + 1 

        
# @lc code=end

