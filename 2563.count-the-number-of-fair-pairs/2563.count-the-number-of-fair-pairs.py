#
# @lc app=leetcode id=2563 lang=python3
#
# [2563] Count the Number of Fair Pairs
#

# @lc code=start
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        res = 0
        for i in range(len(nums)):
            # [lower-nums[i], upper-nums[i]]
            # # of elements < lower - nums[i]
            lo = bisect.bisect_left(nums, lower-nums[i])
            # # of elements <= upper - nums[i]
            hi = bisect.bisect_right(nums, upper-nums[i])
            res += hi-lo
            if nums[i] >= lower - nums[i] and nums[i] <= upper - nums[i]:
                res -= 1
        return res // 2

        
# @lc code=end

