#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
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
    traversal(ans, curr.right)
    ans.append(curr.val)


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #ans = []
        #traversal(ans, root)
        #return ans

        # non-recursion
        ans = []
        if not root:
            return ans

        stack = [root]

        while stack:
            node = stack.pop()
            # parent
            ans.append(node.val)
            # left child
            if node.left:
                stack.append(node.left)
            
            if node.right:
                stack.append(node.right)

        return ans[::-1]
# @lc code=end

