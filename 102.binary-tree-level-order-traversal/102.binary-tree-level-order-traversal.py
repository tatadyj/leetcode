#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

def dfs(ans, curr, depth):
    if len(ans) == depth:
        ans.append([])
    ans[depth].append(curr.val)

    if curr.left:
        dfs(ans, curr.left, depth+1)
    if curr.right:
        dfs(ans, curr.right, depth+1)





class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #ans = []
        #if not root:
        #    return ans
        #dfs(ans, root, 0)
        #return ans

        # bfs
        
        ans = []
        if not root:
            return ans
        queue = deque([root])
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                curr = queue.popleft()
                level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            ans.append(level)
        return ans
        
# @lc code=end

