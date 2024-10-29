#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
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

    ans.append(curr.val)
    traversal(ans, curr.left)
    traversal(ans, curr.right)

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #ans = []
        #traversal(ans, root)
        #return ans

        # non-recursion
        ans = []
        if not root:
            return ans

        stack = [(root, 1)]
        while stack:
            node, count = stack.pop()
            if count == 1:
                ans.append(node.val)
                stack.append((node, count + 1))
                if node.left:
                    stack.append((node.left, 1))
            if count == 2:
                if node.right:
                    stack.append((node.right, 1))
        return ans
# @lc code=end

