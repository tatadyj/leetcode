#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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

