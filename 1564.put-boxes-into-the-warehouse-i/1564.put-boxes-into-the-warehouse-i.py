#
# @lc app=leetcode id=1564 lang=python3
#
# [1564] Put Boxes Into the Warehouse I
#

# @lc code=start
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort()
        res = 0
        for height in warehouse:
            while boxes and boxes[-1] > height:
                boxes.pop()
            if boxes:
                boxes.pop() # place largest box at current room
                res += 1
        return res    
# @lc code=end

