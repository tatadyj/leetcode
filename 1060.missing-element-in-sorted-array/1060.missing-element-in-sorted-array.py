#
# @lc app=leetcode id=1060 lang=python3
#
# [1060] Missing Element in Sorted Array
#

# @lc code=start
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        def count_missing(val):
            idx = bisect.bisect_left(nums, val)
            return (val-1) - (nums[0]-1) - idx

       
        left = min(nums)
        right = max(nums) + k
        while left < right:
            mid = (left + right + 1) // 2
            count = count_missing(mid)
            if count < k - 1:
                left = mid + 1
            elif count > k - 1:
                right = mid - 1
            else:
                left = mid
        return left
# @lc code=end

