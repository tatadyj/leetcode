#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def recur(preorder, inorder):
    if not preorder or not inorder:
        return None

    rootIndex = inorder.index(preorder[0])
    root = TreeNode(preorder[0])

    root.left = recur(preorder[1:rootIndex+1], inorder[:rootIndex])
    root.right = recur(preorder[rootIndex+1:], inorder[rootIndex+1:])

    return root

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        return recur(preorder, inorder)
# @lc code=end

