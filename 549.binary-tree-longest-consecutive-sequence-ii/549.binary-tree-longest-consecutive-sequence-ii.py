#
# @lc app=leetcode id=549 lang=python3
#
# [549] Binary Tree Longest Consecutive Sequence II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        def dfs(curr): 
            nonlocal max_val 
            if not curr:
                return [0, 0]

            incr, decr = 1, 1
            if curr.left:
                left = dfs(curr.left)
                if curr.val == curr.left.val + 1:
                    decr = left[1] + 1
                if curr.val == curr.left.val - 1:
                    incr = left[0] + 1
    
            if curr.right:
                right = dfs(curr.right)
                if curr.val == curr.right.val + 1:
                    decr = max(decr, right[1] + 1)
                if curr.val == curr.right.val - 1:
                    incr = max(incr, right[0] + 1) 

            max_val = max(max_val, incr + decr - 1)
            return [incr, decr]

        max_val = 0
        dfs(root)
        return max_val

# @lc code=end

