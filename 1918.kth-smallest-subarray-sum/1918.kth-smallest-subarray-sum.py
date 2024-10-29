#
# @lc app=leetcode id=1918 lang=python3
#
# [1918] Kth Smallest Subarray Sum
#

# @lc code=start
class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        max_val = sum(nums)
        prefix_sum = [0] + nums

        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i] + prefix_sum[i-1]

        def count_smaller_or_equal(prefix_sum, val):
            count = 0 
            j = 0
            for i in range(len(prefix_sum)):
                while j < len(prefix_sum) and prefix_sum[j] - prefix_sum[i] <= val:
                    j += 1 
                count += j-i-1
            return count 

        left, right = min_val, max_val 
        while left < right:
            mid = (left + right) // 2 
            res = count_smaller_or_equal(prefix_sum, mid)
            if res >= k:
                right = mid
            else:
                left = mid + 1
        return left
# @lc code=end

