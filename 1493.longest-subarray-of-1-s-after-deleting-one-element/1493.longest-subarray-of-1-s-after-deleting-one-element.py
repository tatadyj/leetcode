#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

# @lc code=start
from typing import List 

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        left = 0 
        window_sum = 0
        for right in range(len(nums)):
            rval = nums[right]
            # update window
            window_sum += rval

            while right - left + 1 - window_sum > 1:
                lval = nums[left]
                left += 1 
                # update window
                window_sum -= lval 
            
            res = max(res, right-left+1)
        
        return res-1 # delete one

Solution().longestSubarray([0,1,1,1,0,1,1,0,1])
# @lc code=end

