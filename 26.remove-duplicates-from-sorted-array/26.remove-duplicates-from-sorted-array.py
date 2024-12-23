#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writer = 1
        for reader in range(1, len(nums)):
            if nums[reader] != nums[reader - 1]:
                nums[writer] = nums[reader]
                writer += 1 
        return writer
# @lc code=end

