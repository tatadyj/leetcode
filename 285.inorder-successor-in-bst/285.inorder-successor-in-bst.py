#
# @lc app=leetcode id=285 lang=python3
#
# [285] Inorder Successor in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def iter(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
    res = None
    while root:
        if p.val >= root.val:
            root = root.right
        else:
            res = root
            root = root.left
    return res
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        prev = None
        target = None
        def inOrder(curr):
            nonlocal prev, target

            if not curr:
                return False
            
            if inOrder(curr.left): 
                return True

            if prev == p:
                target = curr
                return True 
            else:
                prev = curr 

            if inOrder(curr.right): 
                return True
        
        inOrder(root)
        return target     
# @lc code=end

