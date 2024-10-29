#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def preorderInvert(curr):
    if curr == None:
        return

    curr.left, curr.right = curr.right, curr.left
    preorderInvert(curr.left)
    preorderInvert(curr.right)

def postorderInvert(curr):
    if curr == None:
        return

    postorderInvert(curr.left)
    postorderInvert(curr.right)
    curr.left, curr.right = curr.right, curr.left

def inorderInvert(curr):
    if curr == None:
        return 

    inorderInvert(curr.left)
    curr.left, curr.right = curr.right, curr.left
    inorderInvert(curr.left)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inorderInvert(root)
        return root
# @lc code=end

