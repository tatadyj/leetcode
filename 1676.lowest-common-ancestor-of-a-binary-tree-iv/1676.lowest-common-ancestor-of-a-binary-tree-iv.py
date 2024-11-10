#
# @lc app=leetcode id=1676 lang=python3
#
# [1676] Lowest Common Ancestor of a Binary Tree IV
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        all_nodes = set([n.val for n in nodes])
        ans = None
        def dfs(curr):
            nonlocal ans
            if not curr:
                return 0
 
            left = dfs(curr.left)
            right = dfs(curr.right)
            count = left + right 

            if curr.val in all_nodes:
                count += 1

            if count == len(all_nodes):
                ans = curr
                return 0 
            else:
                return count 

        dfs(root)
        return ans     
# @lc code=end

