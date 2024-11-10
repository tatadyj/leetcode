#
# @lc app=leetcode id=1802 lang=python3
#
# [1802] Maximum Value at a Given Index in a Bounded Array
#

# @lc code=start
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def is_valid(max_val):
            total = -max_val
            if max_val <= index + 1:
                total += (max_val + 1) * max_val/2 + index + 1 - max_val 
            else:
                total += (max_val + max_val - index) * (index + 1) / 2

            if max_val <= n - index:
                total += (max_val + 1) * max_val/2 + n - index - max_val 
            else:
                total += (max_val + max_val - (n - index - 1)) * (n - index) / 2
            return total <= maxSum
            
        left = 1
        right = maxSum 
        while left < right:
            mid = (left + right + 1) // 2
            if is_valid(mid):
                left = mid 
            else:
                right = mid - 1
        return left
# @lc code=end

