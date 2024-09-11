#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dfs(curr, p, q):
    if curr.val > p.val and curr.val > q.val:
        return dfs(curr.left, p, q)
    elif curr.val < p.val and curr.val < q.val:
        return dfs(curr.right, p, q)
    else:
        return curr

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return dfs(root, p, q)
# @lc code=end

