#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iter
        stack = []
        while root:
            stack.append(root)
            root = root.left

        while k > 0:
            ret = stack.pop()
            k -= 1
            if k == 0:
                return ret.val

            node = ret.right
            while node:
                stack.append(node)
                node = node.left 
        

'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = None
        self.inorder(root)
        return self.res 
        
    def inorder(self, curr):
        if not curr:
            return 

        self.inorder(curr.left)
        self.k -= 1
        if self.k == 0:
            self.res = curr.val
        self.inorder(curr.right)
'''
# @lc code=end

