#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r - 1:
            mid = (l + r) // 2 
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                l = mid 
            else:
                r = mid 
        
        if nums[l] < target <= nums[r]:
            return r 
        elif target <= nums[l]:
            return l 
        else: # target > nums[r]
            return r+1

        
# @lc code=end

