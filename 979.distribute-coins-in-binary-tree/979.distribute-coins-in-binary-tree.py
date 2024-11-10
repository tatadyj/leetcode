#
# @lc app=leetcode id=979 lang=python3
#
# [979] Distribute Coins in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(curr):
            nonlocal ans
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            ans += abs(left) + abs(right)
            return left + right + curr.val - 1
        
        dfs(root)
        return ans   
# @lc code=end

