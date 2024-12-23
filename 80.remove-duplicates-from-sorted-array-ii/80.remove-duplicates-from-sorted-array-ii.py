#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0 

        writer = 1
        count = 1 
        for reader in range(1, len(nums)):
            if nums[reader] == nums[reader - 1]:
                count += 1
                if count <= 2:
                    nums[writer] = nums[reader]
                    writer += 1
                else:
                    # only case writer stays
                    continue
            else:
                count = 1
                nums[writer] = nums[reader]
                writer += 1
        return writer

# @lc code=end

