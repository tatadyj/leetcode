#
# @lc app=leetcode id=272 lang=python3
#
# [272] Closest Binary Search Tree Value II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        queue = deque()

        def dfs(curr):
            if not curr:
                return

            dfs(curr.left)
            if len(queue) < k:
                queue.append(curr.val)
            elif abs(curr.val - target) <= abs(queue[0] - target):
                queue.append(curr.val)
                queue.popleft()
            dfs(curr.right)

        dfs(root)
        return list(queue)

# @lc code=end

