#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 快慢指针指向第0个元素
        slow = fast = 0
        # 当快指针在边界内
        while fast < len(nums):
            # 当快指针和慢指针不一样
            if nums[fast] != nums[slow]:
                # 慢指针走一步
                slow += 1
                nums[slow] = nums[fast]
            # 快指针++
            fast += 1
        # 数组长度为索引+1    
        return slow + 1
# @lc code=end

