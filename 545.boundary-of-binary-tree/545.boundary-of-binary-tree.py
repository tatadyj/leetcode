#
# @lc app=leetcode id=545 lang=python3
#
# [545] Boundary of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        def dfs_left(curr):
            if not curr:
                return 
            
            left.append(curr.val)
            if curr.left:
                dfs_left(curr.left)
            elif curr.right:
                dfs_left(curr.right)

        def dfs_right(curr):
            if not curr:
                return 

            right.append(curr.val)
            if curr.right:
                dfs_right(curr.right)
            elif curr.left:
                dfs_right(curr.left)

        def dfs_bottom(curr):
            if not curr:
                return 

            if not curr.left and not curr.right:
                bottom.append(curr.val)
                return 
            
            dfs_bottom(curr.left)
            dfs_bottom(curr.right)

        left, right, bottom = [], [], []

        if root.left:
            dfs_left(root.left)
            left.pop() 

        if root.right:
            dfs_right(root.right)
            right.pop()
        
        if root.left or root.right:
            dfs_bottom(root)

        res = [root.val] + left + bottom + right[::-1]
        return res    
# @lc code=end

