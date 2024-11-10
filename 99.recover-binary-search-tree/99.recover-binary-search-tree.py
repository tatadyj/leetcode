#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = TreeNode(float('-inf'))
        first, second = None, None 
        def inOrder(curr):
            nonlocal prev, first, second 
            if not curr:
                return 
            
            inOrder(curr.left)
            



        inOrder(root)
        
# @lc code=end

