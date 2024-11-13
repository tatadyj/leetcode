#
# @lc app=leetcode id=1283 lang=python3
#
# [1283] Find the Smallest Divisor Given a Threshold
#

# @lc code=start
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        min_val = 1
        max_val = max(nums)

        def is_valid(nums, threshold, divisor):
            total = 0
            for num in nums:
                total += ceil(num / divisor)
                if total > threshold:
                    return False
            return True

        left, right = min_val, max_val 
        while left < right:
            mid = (left + right) // 2 
            if is_valid(nums, threshold, mid):
                right = mid
            else:
                left = mid + 1 
        return left
        
# @lc code=end

