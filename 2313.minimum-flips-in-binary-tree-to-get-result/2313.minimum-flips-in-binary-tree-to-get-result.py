#
# @lc app=leetcode id=2313 lang=python3
#
# [2313] Minimum Flips in Binary Tree to Get Result
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:
        memo = defaultdict(dict)
        def dfs(curr, expected):
            if not curr.left and not curr.right:
                if expected == True:
                    if curr.val == 1:
                        return 0
                    else:
                        return 1 
                else:
                    if curr.val == 1:
                        return 1
                    else:
                        return 0

            if curr in memo and expected in memo[curr]:
                return memo[curr][expected]

            ans = float('inf')
            if curr.val == 2: # OR 
                if expected == True:
                    ans = min(ans, dfs(curr.left, True) + dfs(curr.right, False))
                    ans = min(ans, dfs(curr.left, False) + dfs(curr.right, True))                    
                    ans = min(ans, dfs(curr.left, True) + dfs(curr.right, True))
                else:
                    ans = min(ans, dfs(curr.left, False) + dfs(curr.right, False))
            if curr.val == 3: # AND
                if expected == True:
                    ans = min(ans, dfs(curr.left, True) + dfs(curr.right, True))
                else:
                    ans = min(ans, dfs(curr.left, True) + dfs(curr.right, False))
                    ans = min(ans, dfs(curr.left, False) + dfs(curr.right, True))
                    ans = min(ans, dfs(curr.left, False) + dfs(curr.right, False))
            if curr.val == 4: # XOR 
                if expected == True:
                    ans = min(ans, dfs(curr.left, True) + dfs(curr.right, False))
                    ans = min(ans, dfs(curr.left, False) + dfs(curr.right, True))
                else:
                    ans = min(ans, dfs(curr.left, False) + dfs(curr.right, False))
                    ans = min(ans, dfs(curr.left, True) + dfs(curr.right, True))
            if curr.val == 5: # NOT
                if curr.left:
                    child = curr.left 
                else:
                    child = curr.right
                if expected == True:
                    ans = min(ans, dfs(child, False))
                else:
                    ans = min(ans, dfs(child, True))
            memo[curr][expected] = ans
            return ans

        return dfs(root, result)
   
# @lc code=end

