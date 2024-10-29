#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
from typing import List 

def reverse(nums, l, r):
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 1:
            return 

        i = len(nums) - 2

        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1 
        
        if i < 0:
            return reverse(nums, 0, len(nums)-1)

        j = len(nums) - 1

        while j >= 0 and nums[j] <= nums[i]:
            j -= 1 
       
        nums[i], nums[j] = nums[j], nums[i]
        return reverse(nums, i+1, len(nums)-1)

# @lc code=end

