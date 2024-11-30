#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        find_none = False
        while queue:
            curr = queue.popleft()

            if not curr:
                find_none = True 
            else:
                if find_none:
                    return False
                queue.append(curr.left)
                queue.append(curr.right)
                
        return True     
# @lc code=end

