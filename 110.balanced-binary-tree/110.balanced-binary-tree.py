#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
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
    if left == -1: return -1
    right = postorder(curr.right)
    if right == -1: return -1

    if abs(left - right) > 1:
        return -1
    else:
        return max(left, right) + 1

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = postorder(root)
        if ans == -1:
            return False
        else:
            return True
       
        
# @lc code=end

