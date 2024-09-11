#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

def recur(curr):
    # complete binary tree
    if not curr: 
        return 0

    left, right = curr.left, curr.right
    leftHeight, rightHeight = 0, 0
    while left:
        left = left.left
        leftHeight += 1
    while right:
        right = right.right
        rightHeight += 1

    if leftHeight == rightHeight:
        return (2<<leftHeight) - 1
    return recur(curr.left) + recur(curr.right) + 1

def postorder(curr):
    if not curr:
        return 0

    left = postorder(curr.left)
    right = postorder(curr.right)
    return left + right + 1



class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return recur(root)
        #return postorder(root)
        # bfs
        '''
        ans = 0
        if not root:
            return ans

        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                ans += 1
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        return ans
        '''



# @lc code=end

