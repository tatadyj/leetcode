#
# @lc app=leetcode id=865 lang=python3
#
# [865] Smallest Subtree with all the Deepest Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # aka LC.1123
        depths = defaultdict(int)
        count = defaultdict(int)
        max_depth = 0
        def dfs_depth(curr, depth):
            nonlocal max_depth
            if not curr:
                return 
            
            depths[curr.val] = depth
            count[depth] += 1
            max_depth = max(max_depth, depth)
            dfs_depth(curr.left, depth+1)
            dfs_depth(curr.right, depth+1)

        dfs_depth(root, 0)
        #print(depths)
        #print(max_depth)
        k = count[max_depth]
        def dfs(curr):
            nonlocal ret
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            count = left + right 
            if depths[curr.val] == max_depth:
                count += 1

            if count == k:
                ret = curr 
                return 0
            else:
                return count 
        ret = None
        dfs(root) 
        return ret     
# @lc code=end

