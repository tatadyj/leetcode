#
# @lc app=leetcode id=1580 lang=python3
#
# [1580] Put Boxes Into the Warehouse II
#

# @lc code=start
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort()
        res = 0
        left = 0 
        right = len(warehouse)-1

        while left <= right:
            if warehouse[left] >= warehouse[right]:
                while boxes and boxes[-1] > warehouse[left]:
                    boxes.pop()
                if boxes:
                    boxes.pop()
                    res += 1
                left += 1
            else:
                while boxes and boxes[-1] > warehouse[right]:
                    boxes.pop()
                if boxes:
                    boxes.pop()
                    res += 1
                right -= 1
        return res
# @lc code=end

