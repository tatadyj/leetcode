#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs_double(curr):
    if not curr:
        return (0, 0) # 打劫和不打劫所得

    left = dfs(curr.left)
    right = dfs(curr.right)
    
    # 打劫当前节点
    rob = curr.val + left[1] + right[1]
    # 不打劫当前节点
    not_rob = max(left) + max(right)
    return (rob, not_rob) # return max(dfs(root))

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo_flag1 = {}
        memo_flag0 = {}

        def dfs(curr, flag): # 1: free to robb; 0: can't to robb
            if not curr:
                return 0

            if flag == 0:
                if curr in memo_flag0:
                    return memo_flag0[curr]

                res = dfs(curr.left, 1) + dfs(curr.right, 1)
                
                memo_flag0[curr] = res
                return res
            else:
                if curr in memo_flag1:
                    return memo_flag1[curr]
                    
                opt1 = curr.val + dfs(curr.left, 0) + dfs(curr.right, 0)
                opt2 = dfs(curr.left, 1) + dfs(curr.right, 1)
                res = max(opt1, opt2)
                
                memo_flag1[curr] = res
                return res

    
        ret = dfs(root, 1) # free to rob
        return ret
            
             
# @lc code=end

