#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        res = 0
        i = 0 
        for j in range(len(nums)):
            product *= nums[j]
            while i <= j and product >= k:
                product /= nums[i]
                i += 1
            res += j-i + 1
        return res
# @lc code=end

