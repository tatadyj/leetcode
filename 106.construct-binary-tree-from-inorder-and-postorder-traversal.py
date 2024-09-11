#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def recur(inorder, postorder):
    if not inorder or not postorder:
        return None
    
    rootIndex = inorder.index(postorder[-1])
    root = TreeNode(postorder[-1])

    root.left = recur(inorder[:rootIndex], postorder[:rootIndex])
    root.right = recur(inorder[rootIndex+1:], postorder[rootIndex:-1])

    return root

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return recur(inorder, postorder)
# @lc code=end

