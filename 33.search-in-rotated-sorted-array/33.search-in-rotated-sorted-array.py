#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
 
        while l < r - 1:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid 
            elif nums[mid] > nums[l]: # left is sorted
                if nums[l] <= target <= nums[mid]: # target is in left
                    r = mid 
                else:
                    l = mid 
            else:   # right is sorted
                if nums[mid] <= target <= nums[r]:
                    l = mid 
                else:
                    r = mid 

        if nums[l] == target:
            return l 
        elif nums[r] == target:
            return r 
        else: 
            return -1 
# @lc code=end

