#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
from typing import List

def recur(nums, left, right):
    if left + 1 == right:
        return min(nums[left], nums[right])

    if nums[left] <= nums[right]:
        return nums[left]

    mid = (left + right) // 2

    lval = recur(nums, left, mid-1)
    rval = recur(nums, mid, right)
    return min(lval, rval)


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        if nums[l] < nums[r]:
            return nums[l]

        while l < r - 1:
            mid = (l + r) // 2
            if nums[mid] > nums[l]:
                l = mid 
            else:
                r = mid 

        return nums[l] if nums[l] < nums[r] else nums[r] 
        
# @lc code=end

