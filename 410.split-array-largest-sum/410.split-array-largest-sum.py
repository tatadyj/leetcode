#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def is_valid(nums, k, val):
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > val:
                    total = num
                    count += 1 
                if count > k:
                    return False 
            return True 

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2 
            if is_valid(nums, k, mid):
                right = mid
            else:
                left = mid + 1
        return left
# @lc code=end

