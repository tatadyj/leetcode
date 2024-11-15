#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
def searchInsert1(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)
    while l < r:
        m = (l + r) // 2
        if nums[m] >= target:
            r = m
        else:
            l = m + 1
    return l

   

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #return bisect.bisect_left(nums, target)
        return searchInsert1(nums, target)
        
# @lc code=end

