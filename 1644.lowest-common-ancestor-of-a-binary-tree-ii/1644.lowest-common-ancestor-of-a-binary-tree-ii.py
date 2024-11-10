#
# @lc app=leetcode id=1644 lang=python3
#
# [1644] Lowest Common Ancestor of a Binary Tree II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def dfs(curr, p, q):
            nonlocal ans
            if not curr:
                return 0

            left = dfs(curr.left, p, q)
            right = dfs(curr.right, p, q)

            # postorder
            count = 0
            if curr.val == p.val or curr.val == q.val:
                count += 1
            count += left + right
            if count == 2:
                ans = curr
                return 0
            else:
                return count
         
        ret = dfs(root, p, q)
        #print(ret)
        return ans 
            
# @lc code=end

