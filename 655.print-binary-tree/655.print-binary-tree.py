#
# @lc app=leetcode id=655 lang=python3
#
# [655] Print Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def dfs(curr):
            if not curr:
                return -1
            
            l = dfs(curr.left)
            r = dfs(curr.right)
            return max(l, r) + 1

        
        height = dfs(root)
        m = height + 1
        n = 2**(height + 1) - 1
        res = [[""]*n for _ in range(m)]
        
        res[0][(n-1)//2] = str(root.val) 
        queue = deque([(0, (n-1)//2, root)])
        while queue:
            r, c, curr = queue.popleft()
            if curr.left:
                nxt_r, nxt_c = r+1, c-2**(height-r-1)
                res[nxt_r][nxt_c] = str(curr.left.val)
                queue.append((nxt_r, nxt_c, curr.left))
            if curr.right:
                nxt_r, nxt_c = r+1, c+2**(height-r-1)
                res[nxt_r][nxt_c] = str(curr.right.val)
                queue.append((nxt_r, nxt_c, curr.right))

        return res 
# @lc code=end

