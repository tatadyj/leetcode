#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([[root, 1]])
        ans = float('-inf')
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node, idx = queue.popleft()
                level.append(idx)
                if node.left:
                    queue.append([node.left, idx*2])
                if node.right:
                    queue.append([node.right, idx*2+1])
            ans = max(ans, level[-1] - level[0] + 1)
        return ans

        
# @lc code=end

