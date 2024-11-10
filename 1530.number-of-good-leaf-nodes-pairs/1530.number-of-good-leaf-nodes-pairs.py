#
# @lc app=leetcode id=1530 lang=python3
#
# [1530] Number of Good Leaf Nodes Pairs
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        res = 0
        def dfs(curr):
            nonlocal res
            if not curr:
                return {}

            if not curr.left and not curr.right:
                return {0:1}
            
            ret = defaultdict(int)
            left = dfs(curr.left)
            right = dfs(curr.right)
          
            for d2 in right:
                if d2 + 1 > distance: continue 
                ret[d2+1] += right[d2]
          
            for d1 in left:
                if d1 + 1 > distance: continue 
                ret[d1+1] += left[d1]
      
            for d1 in left:
                for d2 in right:
                    if d1 + d2 + 2 <= distance: 
                        res += left[d1] * right[d2]
            return ret 

        dfs(root)
        return res

# @lc code=end

