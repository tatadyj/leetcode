#
# @lc app=leetcode id=1793 lang=python3
#
# [1793] Maximum Score of a Good Subarray
#

# @lc code=start
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = nums[k]
        min_val = nums[k]
        i = k - 1
        j = k + 1
        while i >= 0 or j < n:
            while i >= 0 and nums[i] >= min_val:
                i -= 1
            while j < n and nums[j] >= min_val:
                j += 1
            res = max(res, min_val * (j-i-1))

            if j < n and i >= 0:
                if nums[i] <= nums[j]:
                    min_val = nums[j]
                    j += 1
                else:
                    min_val = nums[i]
                    i -= 1
            elif j < n:
                min_val = nums[j]
                j += 1
            elif i >= 0:
                min_val = nums[i]
                i -= 1
            
        res = max(res, min_val * (j-i-1))
        return res         
  
# @lc code=end

