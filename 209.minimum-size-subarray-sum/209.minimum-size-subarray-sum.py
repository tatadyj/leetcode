#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        left = 0
        window_sum = 0

        for right in range(len(nums)):
            rval = nums[right]
            # update window
            window_sum += rval 

            while window_sum >= target:
                res = min(res, right - left + 1)
                lval = nums[left]
                left += 1

                # update window
                window_sum -= lval 
                
        return  res if res != float('inf') else 0     
# @lc code=end

