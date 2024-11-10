#
# @lc app=leetcode id=1382 lang=python3
#
# [1382] Balance a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        ans = []
        def dfs(curr):
            nonlocal ans
            if not curr:
                return 
            
            dfs(curr.left)
            ans.append(curr.val)
            dfs(curr.right)

        def buildBST(ans, left, right):
            if left > right:
                return 
            
            mid = (left + right) // 2 
            root = TreeNode(ans[mid])
            root.left = buildBST(ans, left, mid-1)
            root.right = buildBST(ans, mid+1, right)
            return root

        dfs(root)
        return buildBST(ans, 0, len(ans)-1)

        
# @lc code=end

