#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        prev = None 
        max_freq = 0 
        curr_freq = 0

        def dfs(curr):
            nonlocal prev, max_freq, curr_freq
            if not curr:
                return 

            dfs(curr.left)
            if prev is None:
                curr_freq += 1 
                max_freq += 1 
                ans.append(curr.val)
            elif curr.val != prev: 
                curr_freq = 1
                if curr_freq == max_freq:
                    ans.append(curr.val)
            else: # == 
                curr_freq += 1
                if curr_freq > max_freq:
                    max_freq = curr_freq
                    ans.clear() # if use = [], -> not find ans
                    ans.append(curr.val)
                elif curr_freq == max_freq:
                    ans.append(curr.val)
            prev = curr.val

            dfs(curr.right)


        dfs(root)
        return ans   
# @lc code=end

