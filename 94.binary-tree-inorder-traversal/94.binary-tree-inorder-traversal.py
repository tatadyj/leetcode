#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def traversal(ans: List[int], curr: TreeNode):
    if curr == None:
        return 

    traversal(ans, curr.left)
    ans.append(curr.val)
    traversal(ans, curr.right)


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        traversal(ans, root)
        return ans
# @lc code=end

