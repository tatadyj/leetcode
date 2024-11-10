#
# @lc app=leetcode id=1695 lang=python3
#
# [1695] Maximum Erasure Value
#

# @lc code=start
from collections import defaultdict
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = float('-inf')
        window = defaultdict(int)
        window_sum = 0 
        left = 0 
        for right in range(len(nums)):
            rval = nums[right]
            # update window
            window[rval] += 1
            window_sum += rval 

            while window[rval] > 1:
                lval = nums[left]
                left += 1 
                # update window
                window[lval] -= 1
                window_sum -= lval  

            res = max(res, window_sum)

        return res 
        

        
# @lc code=end

