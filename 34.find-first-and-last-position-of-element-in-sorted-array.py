#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List

    

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        res = []

        l, r = 0, len(nums)-1
        while l < r - 1:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid
            elif nums[mid] > target:
                r = mid 
            else:
                r = mid 
        
        if nums[l] == target:
            res.append(l)
        elif nums[r] == target:
            res.append(r)
        else:
            return [-1, -1]

        r = len(nums)-1
        while l < r - 1:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid 
            else:
                l = mid 
    
        if nums[r] == target:
            res.append(r)
        else:              # nums[l] == target:
            res.append(l)

        return res 

Solution().searchRange([5,7,7,8,8,10], 8)     
# @lc code=end

