#
# @lc app=leetcode id=2439 lang=python3
#
# [2439] Minimize Maximum of Array
#

# @lc code=start
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def is_ok(max_val, nums):
            if nums[0] > max_val:
                return False 

            for i in range(1, len(nums)):
                if nums[i-1] < max_val:
                    nums[i] -= max_val - nums[i-1]
                    nums[i-1] = max_val
                    if nums[i] > max_val: 
                        return False 
            if nums[-1] > max_val:
                return False
            else:
                return True 

        left = min(nums)
        right = max(nums)
        while left < right:
            mid = (left + right) // 2
            if is_ok(mid, nums[:]):
                right = mid 
            else:
                left = mid + 1

        return left 
# @lc code=end

