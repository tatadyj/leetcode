#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 找左边界
        # left, right = 0, len(nums)-1 
        # while left < right:
        #     mid = (left + right) // 2 
        #     if nums[mid] >= target:
        #         right = mid
        #     else:
        #         left = mid + 1 
        
        # if nums[left] == target:
        #     return left 
        # else:
        #     return -1

        # 找右边界
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
         
# @lc code=end

