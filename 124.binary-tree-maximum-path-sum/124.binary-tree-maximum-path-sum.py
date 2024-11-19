#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')

        def dfs(curr):
            nonlocal ans
            if not curr:
                return 0 

            left = dfs(curr.left)
            right = dfs(curr.right)
            total = max(0, left) + max(0, right) + curr.val 
            ans = max(ans, total)
            return max(0, max(left, right)) + curr.val

        dfs(root)
        return ans    
# @lc code=end

