#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def build(lo, hi):
    res = []
    if lo > hi:
        res.append(None)
        return res 

    for i in range(lo, hi+1):
        leftTrees = build(lo, i-1)
        rightTrees = build(i+1, hi)

        for left in leftTrees:
            for right in rightTrees:
                root = TreeNode(i)
                root.left = left 
                root.right = right 
                res.append(root)

    return res 

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return build(1, n)
        
# @lc code=end

