#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = 0 
        res = float('-inf')
        for g in gain:
            prefix_sum += g 
            res = max(res, prefix_sum)

        return max(res, 0) 

        
# @lc code=end

