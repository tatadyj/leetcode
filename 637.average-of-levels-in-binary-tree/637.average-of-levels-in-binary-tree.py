#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        ans = []
        queue = deque([root])
        while queue:
            size = len(queue)
            total = 0
            for _ in range(size):
                curr = queue.popleft()
                total += curr.val
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            ans.append(total/size)
        return ans

# @lc code=end

