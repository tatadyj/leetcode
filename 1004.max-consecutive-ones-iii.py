#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
from typing import List 

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0 
        window_sum = 0
        res = 0
        for right in range(len(nums)):
            rval = nums[right]
            # udpate window
            window_sum += rval                    

            while right - left + 1 - window_sum > k:
                lval = nums[left]
                left += 1
                # update window
                window_sum -= lval 
            
            res = max(res, right - left + 1)
        return res

#Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)
Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)
# @lc code=end

