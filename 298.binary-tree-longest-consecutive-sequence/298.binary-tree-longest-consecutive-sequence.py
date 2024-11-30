#
# @lc app=leetcode id=298 lang=python3
#
# [298] Binary Tree Longest Consecutive Sequence
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(curr):
            nonlocal ans
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            dist = 1
            if curr.left and curr.val + 1 == curr.left.val:
                dist = max(dist, left + 1)
            if curr.right and curr.val + 1 == curr.right.val:
                dist = max(dist, right + 1)

            ans = max(ans, dist)
            return dist

        ans = 0
        dfs(root)
        return ans
        
# @lc code=end

