#
# @lc app=leetcode id=889 lang=python3
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def recur(preorder, postorder):
    if not preorder or not postorder:
        return None

    root = TreeNode(preorder[0])
    if len(preorder) == 1:
        return root
        
    idx = postorder.index(preorder[1])

    root.left = recur(preorder[1:idx+2], postorder[:idx+1])
    root.right = recur(preorder[idx+2:], postorder[idx+1:-1])

    return root

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return recur(preorder, postorder)    
# @lc code=end

