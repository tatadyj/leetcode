#
# @lc app=leetcode id=270 lang=python3
#
# [270] Closest Binary Search Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        temp = inf
        while root:
            if abs(temp - target) > abs(root.val - target):
                temp = root.val
            if abs(temp - target) == abs(root.val - target):
                temp = min(temp, root.val)
                
            if root.val == target:
                return root.val
            elif root.val < target:
                root = root.right 
            else:
                root = root.left 
        return temp 
# @lc code=end

