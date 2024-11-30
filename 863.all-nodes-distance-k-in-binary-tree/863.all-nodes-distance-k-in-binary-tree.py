#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []

        def go_forward(curr, step):
            if not curr:
                return 

            if step == 0:
                ans.append(curr.val)
                return 

            go_forward(curr.left, step-1)
            go_forward(curr.right, step-1)


        def dfs(curr):
            if not curr:
                return -1

            if curr == target:
                go_forward(curr, k)
                return 0 

            left_depth = dfs(curr.left)
            if left_depth != -1:
                if left_depth + 1 == k:
                    ans.append(curr.val)
                else:
                    go_forward(curr.right, k - (left_depth + 1) - 1)
                return left_depth + 1

            right_depth = dfs(curr.right)
            if right_depth != -1:
                if right_depth + 1 == k:
                    ans.append(curr.val)
                else:
                    go_forward(curr.left, k - (right_depth + 1) - 1)
                return right_depth + 1

            return -1

        dfs(root)
        return ans 
# @lc code=end

