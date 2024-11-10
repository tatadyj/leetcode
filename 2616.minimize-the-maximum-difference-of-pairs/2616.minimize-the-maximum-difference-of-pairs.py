#
# @lc app=leetcode id=2616 lang=python3
#
# [2616] Minimize the Maximum Difference of Pairs
#

# @lc code=start
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        def is_ok(max_val):
            count = 0
            i = 0 
            while i < n:
                if i+1 < n and abs(nums[i] - nums[i+1]) <= max_val:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= p


        left = 0
        right = nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            if is_ok(mid):
                right = mid
            else:
                left = mid + 1
        return left
        
# @lc code=end

