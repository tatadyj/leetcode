#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.insert(0, 0)
        for i in range(1, len(nums)):
            while i != nums[i] and nums[i] >= 0 and nums[i] < len(nums) and nums[i] != nums[nums[i]]:
                tmp = nums[i]
                nums[i] = nums[tmp]
                nums[tmp] = tmp 


        for i in range(1, len(nums)):
            if i != nums[i]:
                return i 
        return len(nums)       
# @lc code=end

