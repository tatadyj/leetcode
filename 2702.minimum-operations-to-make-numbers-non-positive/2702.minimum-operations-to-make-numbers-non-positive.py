#
# @lc app=leetcode id=2702 lang=python3
#
# [2702] Minimum Operations to Make Numbers Non-positive
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        def is_ok(k, arr):
            count = 0
            for n in nums:
                n = n - k*y
                if n > 0:
                    count += ceil(n / (x-y))
            return count <= k  

        left = 0 
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if is_ok(mid, nums[:]):
                right = mid 
            else:
                left = mid + 1 
        return left  
# @lc code=end

