#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 如果fast遇到需要去除的元素，则直接跳过，否则就告诉slow指针，并让slow前进一步
        # 注意这里和有序数组去重的解法有一个重要不同，我们这里是先给 nums[slow] 赋值然后再给 slow++，
        # 这样可以保证 nums[0..slow-1] 是不包含值为 val 的元素的，最后的结果数组长度就是 slow。
        fast = slow = 0
        
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            
            fast += 1
            
        return slow        
# @lc code=end

