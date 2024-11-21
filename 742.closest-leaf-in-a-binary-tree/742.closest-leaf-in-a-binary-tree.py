#
# @lc app=leetcode id=742 lang=python3
#
# [742] Closest Leaf in a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        # for each node, we record:
        dist_to_nearest_leaf = defaultdict(int) # distance to the nearest leaf
        nearest_leaf = defaultdict(int) # the nearest leaf
        min_dist = inf 
        res = None

        def dfs_find_nearest_leaf(curr):
            if not curr:
                return inf 
        
            if not curr.left and not curr.right:
                dist_to_nearest_leaf[curr] = 0
                nearest_leaf[curr] = curr.val
                return 0
            
            L = dfs_find_nearest_leaf(curr.left)
            R = dfs_find_nearest_leaf(curr.right)
            
            if L > R:
                dist_to_nearest_leaf[curr] = R + 1
                nearest_leaf[curr] = nearest_leaf[curr.right]           
            else:
                dist_to_nearest_leaf[curr] = L + 1
                nearest_leaf[curr] = nearest_leaf[curr.left]           
            
            return dist_to_nearest_leaf[curr]

        def dfs_find_k(curr): # return dist to k 
            nonlocal min_dist, res

            if not curr:
                return -1
            
            if curr.val == k:
                if min_dist > dist_to_nearest_leaf[curr]:
                    min_dist = dist_to_nearest_leaf[curr]
                    res = nearest_leaf[curr]
                return 0
            
            L = dfs_find_k(curr.left)
            if L != -1:
                if curr.right and min_dist > L + 2 + dist_to_nearest_leaf[curr.right]:
                    min_dist = L + 2 + dist_to_nearest_leaf[curr.right]
                    res = nearest_leaf[curr.right]                   
                return L + 1
            
            R = dfs_find_k(curr.right)
            if R != -1:
                if curr.left and min_dist > R + 2 + dist_to_nearest_leaf[curr.left]:
                    min_dist = L + 2 + dist_to_nearest_leaf[curr.left]
                    res = nearest_leaf[curr.left]                 
                return R + 1
            return -1

        dfs_find_nearest_leaf(root)
        dfs_find_k(root)
        return res
        
# @lc code=end

