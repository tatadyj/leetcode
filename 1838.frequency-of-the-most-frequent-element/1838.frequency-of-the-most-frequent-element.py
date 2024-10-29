#
# @lc app=leetcode id=1838 lang=python3
#
# [1838] Frequency of the Most Frequent Element
#

# @lc code=start
from typing import List 

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort() # !!
        res = 0
        left = 0
        window_sum = 0 
        for right in range(len(nums)):
            rval = nums[right]
            # update window
            target_sum = rval * (right - left + 1)
            window_sum += rval
            if target_sum - window_sum <= k:
                res = max(res, right-left)  

            while target_sum - window_sum > k:
                lval = nums[left]
                left += 1

                # update window 
                window_sum -= lval 
                target_sum = rval * (right - left + 1)

        return res 

Solution().maxFrequency([1,4,8,13], 5)
# @lc code=end

