#
# @lc app=leetcode id=1110 lang=python3
#
# [1110] Delete Nodes And Return Forest
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfs_method(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    to_delete = set(to_delete)
    ans = []

    def dfs(curr):
        if not curr:
            return 
        
        if not curr.left and not curr.right:
            if curr.val in to_delete:
                return 
            else:
                return curr 

        left = dfs(curr.left)
        right = dfs(curr.right)
        
        if curr.val in to_delete:
            if left:
                ans.append(left)
            if right:
                ans.append(right)
            return
        else:
            curr.left, curr.right = None, None 
            if left:
                curr.left = left 
            if right:
                curr.right = right 
            return curr
    
    ret = dfs(root)
    if ret: 
        ans.append(ret)
    return ans 
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        ans = []

        queue = deque()
        queue.append(root)
        while queue:
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
                if curr.left.val in to_delete:
                    curr.left = None
            if curr.right:
                queue.append(curr.right)
                if curr.right.val in to_delete:
                    curr.right = None 
            if curr.val in to_delete:
                if curr.left:
                    ans.append(curr.left)
                if curr.right:
                    ans.append(curr.right)
        
        if root.val not in to_delete:
            ans.append(root)
        return ans        
# @lc code=end

