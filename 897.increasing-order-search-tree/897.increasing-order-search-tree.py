#
# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        
        if root.left:
            left_head = self.increasingBST(root.left)
            left_tail = left_head
            while left_tail.right:
                left_tail = left_tail.right

            left_tail.right = root 
            root.left = None
            root.right = self.increasingBST(root.right)
            return left_head
        else:
            root.right = self.increasingBST(root.right)
            return root 
# @lc code=end

