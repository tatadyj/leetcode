#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
from typing import List 

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp_i_0, dp_i_1 = 0, float('-inf')

        for i in range(len(nums)):
            dp_i_0 = max(dp_i_0, dp_i_1) 
            dp_i_1 = dp_i_0 + nums[i]
        return dp_i_1

Solution().rob([1,2,3,1])        
# @lc code=end

