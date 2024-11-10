#
# @lc app=leetcode id=1838 lang=python3
#
# [1838] Frequency of the Most Frequent Element
#

# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        left = 0
        curr_sum = 0 
        for right in range(len(nums)):
            rval = nums[right]
            curr_sum += rval

            # target_sum - curr_sum > k
            while rval * (right - left + 1) - curr_sum > k:
                lval = nums[left]
                left += 1
                # update window 
                curr_sum -= lval 

            res = max(res, right - left + 1)  
        return res 
# @lc code=end

