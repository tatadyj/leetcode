#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def preorder(ans, path, curr):
    if not curr:
        return 
    path.append(str(curr.val))

    # 叶子
    if not curr.left and not curr.right:
        ans.append("->".join(path))
        return

    #if curr.left:
    preorder(ans, path, curr.left)
    if curr.left: path.pop()
    #if curr.right:
    preorder(ans, path, curr.right)
    if curr.right: path.pop()


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans, path = [], []
        if not root:
            return ans
        preorder(ans, path, root)
        return ans
        
        # bfs 


# @lc code=end

