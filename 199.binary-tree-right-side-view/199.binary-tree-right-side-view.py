#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

# dfs
def dfs(ans, curr, depth):
    if not curr:
        return 

    if len(ans) == depth:
        ans.append(curr.val)
    dfs(ans, curr.right, depth+1)
    dfs(ans, curr.left, depth+1)


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # dfs
        ans = []
        dfs(ans, root, 0)
        return ans

        # bfs
        '''
        ans = []
        if not root:
            return ans

        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if i == size - 1:
                    ans.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return ans
        '''                    
        
# @lc code=end

