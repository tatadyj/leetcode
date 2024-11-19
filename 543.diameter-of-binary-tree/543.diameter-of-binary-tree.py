#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0 

        def dfs(curr):
            nonlocal max_diameter
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            max_diameter = max(max_diameter, left + right)
            return max(left,  right) + 1 # max number of nodes

        dfs(root)
        return max_diameter
# @lc code=end

