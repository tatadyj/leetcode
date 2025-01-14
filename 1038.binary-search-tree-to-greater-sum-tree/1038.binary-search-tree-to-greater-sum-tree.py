#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(curr):
            nonlocal sum 
            if not curr:
                return
           
            dfs(curr.right)
            curr.val += sum
            sum = curr.val 
            dfs(curr.left)

        sum = 0
        dfs(root)
        return root
# @lc code=end

