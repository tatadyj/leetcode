#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = None
        def dfs(curr):
            nonlocal ans, prev
            if not curr: 
                return 

            dfs(curr.left)
            if not prev:
                prev = curr 
            else:
                ans = min(ans, abs(curr.val - prev.val))
                prev = curr
            dfs(curr.right)

        ans = inf 
        dfs(root)
        return ans
# @lc code=end

