#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
def by_count():
        count = 0
        res = 0
        left = 0 
        for right in range(len(nums)):
            rval = nums[right]
            if rval == 0:
                count += 1                 

            while left < len(nums) and count > k:
                lval = nums[left]
                if lval == 0:
                    count -= 1
                left += 1
            
            res = max(res, right - left + 1)
        return res

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # by sum
        sum = 0
        res = 0
        left = 0 
        for right in range(len(nums)):
            rval = nums[right]
            sum += rval               

            while left < len(nums) and right - left + 1 - sum > k:
                lval = nums[left]
                sum -= lval
                left += 1
            
            res = max(res, right - left + 1)
        return res
# @lc code=end

