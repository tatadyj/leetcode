#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def is_twice(idx):
            if idx - 1 >= 0 and idx + 1 < len(nums):
                return nums[idx-1] == nums[idx] or nums[idx] == nums[idx+1]
            
            if idx - 1 >= 0:
                return nums[idx-1] == nums[idx]
            
            if idx + 1 < len(nums):
                return nums[idx] == nums[idx+1]

            
        def in_left(idx):
            if idx - 1 >= 0:
                if nums[idx-1] == nums[idx]:
                    if (idx + 1) % 2 == 0:
                        return False 
                    else:
                        return True 
                else:
                    if idx % 2 == 0:
                        return False 
                    else:
                        return True 
            else:
                return False 
        
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if not is_twice(mid):
                return nums[mid]
            else:
                if in_left(mid):
                    right = mid 
                else:
                    left = mid + 1
        return nums[left]
# @lc code=end

