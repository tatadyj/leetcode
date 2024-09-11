#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])
        while queue:
            size = len(queue)
            for _ in range(size):
                curr, depth = queue.popleft()
                if not curr.left and not curr.right:
                    return depth
                if curr.left:
                    queue.append((curr.left, depth+1))
                if curr.right:
                    queue.append((curr.right, depth+1))


        
# @lc code=end

