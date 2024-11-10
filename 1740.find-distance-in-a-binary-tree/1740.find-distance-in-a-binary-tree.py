#
# @lc app=leetcode id=1740 lang=python3
#
# [1740] Find Distance in a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def dfs(curr): # return (dist_p, dist_q)
            nonlocal ans
            if not curr:
                return (-1, -1)

            left = dfs(curr.left)
            right = dfs(curr.right)
            
            dist_p, dist_q = -1, -1 # 没有找到p，q， 其相应的距离就是-1
            # 更新 p 到当前节点距离
            if left[0] != -1:
                dist_p = left[0] + 1
            elif right[0] != -1:
                dist_p = right[0] + 1
            elif curr.val == p:
                dist_p = 0 

            # 更新 q 到当前节点距离
            if left[1] != -1:
                dist_q = left[1] + 1
            elif right[1] != -1:
                dist_q = right[1] + 1
            elif curr.val == q:
                dist_q = 0 

            if dist_p != -1 and dist_q != -1:
                ans = dist_p + dist_q
                return (-1, -1)
            else:
                return (dist_p, dist_q)

        ans = -1
        dfs(root)
        return ans
        
# @lc code=end

