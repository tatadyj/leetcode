#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
       
        def search_lb(target):
            # first index >= target
            # aka left bound
            left, right = 0, len(nums)-1 
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid 
                else:
                    left = mid + 1
            if nums[left] == target:
                return left 
            else:
                return -1
        
        def search_rb(target):
            # right bound
            left, right = 0, len(nums)-1 
            while left < right:
                mid = (left + right + 1) // 2
                if nums[mid] <= target:
                    left = mid 
                else:
                    right = mid - 1
            if nums[left] == target:
                return left 
            else:
                return -1

        lb = search_lb(target)
        rb = search_rb(target)
        return [lb, rb]  
# @lc code=end

