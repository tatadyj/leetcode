#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p1 = curr = 0 
        p2 = n - 1

        while curr <= p2:
            if nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            elif nums[curr] == 0:
                nums[curr], nums[p1] = nums[p1], nums[curr]
                p1 += 1
                curr += 1 
            else:
                curr += 1
        
# @lc code=end

