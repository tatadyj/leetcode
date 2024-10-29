#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def postorder(curr):
    if not curr:
        return 0

    left = postorder(curr.left)
    right = postorder(curr.right)

    mid = 0
    if curr.left and not curr.left.left and not curr.left.right:
        mid = curr.left.val

    return left + right + mid

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return postorder(root)    
# @lc code=end

