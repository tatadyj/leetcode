#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0 

        def dfs(curr):
            nonlocal ans
            if not curr:
                return 0 
            
            l = dfs(curr.left)
            r = dfs(curr.right)

            left, right = 0, 0
            if curr.left and curr.left.val == curr.val:
                left = l
            if curr.right and curr.right.val == curr.val:
                right = r

            ans = max(ans, left + right)
            return max(left, right) + 1

        dfs(root)
        return ans
# @lc code=end

