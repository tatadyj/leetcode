#
# @lc app=leetcode id=1339 lang=python3
#
# [1339] Maximum Product of Splitted Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtree = defaultdict(int)
        def dfs_sum(curr):
            if not curr:
                return 0

            sum = dfs_sum(curr.left) + dfs_sum(curr.right) + curr.val
            subtree[curr] = sum
            return sum

        dfs_sum(root)
        total = subtree[root]
        ans = 0
        for s in subtree.values():
            ans = max(ans, s * (total - s))
        return ans % (10**9 + 7) 
# @lc code=end

