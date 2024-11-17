#
# @lc app=leetcode id=2779 lang=python3
#
# [2779] Maximum Beauty of an Array After Applying Operation
#

# @lc code=start
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # nums[i] + k >= nums[j] - k
        # nums[j] - nums[i] <= 2*k 
        nums.sort()
        n = len(nums)
        res = 0
        l = 0 
        for r in range(n):
            while nums[r] - nums[l] > 2*k:
                l += 1
            res = max(res, r-l+1)
        return res
   
# @lc code=end

