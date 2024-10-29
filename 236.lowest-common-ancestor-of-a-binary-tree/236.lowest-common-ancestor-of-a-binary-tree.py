#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def postorder(curr, p, q):
    if not curr:
        return None

    if curr.val == p.val or curr.val == q.val:
        return curr

    left = postorder(curr.left, p, q)
    right = postorder(curr.right, p, q)

    if left and right:
        return curr 
    else:
        return left if left else right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return postorder(root, p, q)
# @lc code=end

